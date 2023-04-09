#IMPORT NECESSRAY LIBRARIES
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename 
import numpy as np 
import os 
import shutil
import sys 
import tensorflow as tf 
from PIL import Image 
import cv2 
import grpc 

# IMPORT prediction service functions from TF-Serving API 
from tensorflow_serving.apis import predict_pb2 
from tensorflow_serving.apis import prediction_service_pb2_grpc 

from utils import label_map_util
from utils import visualization_utils as viz_utils
from core.standard_fields import DetectionResultFields as dt_fields 

from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from sqlalchemy import text

app = Flask(__name__ )

sys.path.append("..") 
tf.get_logger().setLevel('ERROR') 

PATH_TO_LABELS = "./data/label_map.pbtxt" 
NUM_CLASSES = 4 

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True) 
category_index = label_map_util.create_category_index(categories) 

# root folder "originals/" been solved as requirement in CW
app.config['UPLOAD_FOLDER'] = 'originals/'  
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

#try'n to use sql==8.0.32 server to docker compose alongside but connectin error, need docker networking knowledge!
#Used "host" container networks, yep, it works!!

# to skip warning caused by version 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/obj_det'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

with app.app_context():

    # Create Model
    class Users(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        img_label = db.Column(db.String(200))
        obj_detected = db.Column(db.String(200))
        probability = db.Column(db.String(20))

    def __init__(self, id, img_label, obj_detected, probability):
        self.id= id
        self.img_label = img_label
        self.obj_detected= obj_detected
        self.probability = probability

    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

    def get_stub():
        channel = grpc.insecure_channel('127.0.0.1.:8500')
        stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
        return stub

    def load_image_into_numpy_array(image):
        (im_width, im_height) = image.size
        return np.array(image.getdata()).reshape(
            (im_height,im_width,3)).astype(np.uint8)

    def load_input_tensor(input_image):
        image_np = load_image_into_numpy_array(input_image)
        image_np_expanded = np.expand_dims(image_np,axis=0).astype(np.uint8)
        tensor = tf.make_tensor_proto(image_np_expanded)
        return tensor

    def inference(frame, stub):
        # add the RPC cmd here
        # call tf server
        # channel = grpc.insecure_channel('localhost:8500')
        channel = grpc.insecure_channel('localhost:8500',options=(('grpc.enable_http_proxy',0),))
        print("channel: ",channel)
        stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
        print("Stub: ",stub)
        request = predict_pb2.PredictRequest()
        print("Request: ",request)
        request.model_spec.name = 'od'

        cv2_im = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        image = Image.fromarray(cv2_im)
        input_tensor = load_input_tensor(image)
        request.inputs['input_tensor'].CopyFrom(input_tensor)

        result = stub.Predict(request,60.0)

        image_np = load_image_into_numpy_array(image)

        output_dict = {}
        output_dict['detection_classes'] = np.squeeze(
            result.outputs[dt_fields.detection_classes].float_val).astype(np.uint8)
        output_dict['detection_boxes'] = np.reshape(
            result.outputs[dt_fields.detection_boxes].float_val,(-1,4))
        output_dict['detection_scores'] = np.squeeze(
            result.outputs[dt_fields.detection_scores].float_val)

        frame = viz_utils.visualize_boxes_and_labels_on_image_array(image_np,
                        output_dict['detection_boxes'],
                        output_dict['detection_classes'],
                        output_dict['detection_scores'],
                        category_index,
                        use_normalized_coordinates=True,
                        max_boxes_to_draw=200,
                        min_score_thresh=.55,
                        agnostic_mode=False)

        # caution here, this will only generate the first detection 
        # But we want multiple detections if there exist
        # Problem : it will store chaoticly in database, thus I went for single detections, but I will fix later on               
        class_id = output_dict['detection_classes'][0] 
        class_name = category_index[class_id]['name']

        detection_index = np.where(output_dict['detection_classes'] == class_id)[0][0]
        detection_score = output_dict['detection_scores'][detection_index]
        detection_scores_percent = detection_score * 100.0
        det_score_percent_round = round(detection_scores_percent,2)
        det_score_perc='{}%'.format(det_score_percent_round)
        return frame, class_name, det_score_perc

    @app.route('/')
    def index():
        return render_template('index.html')

    #Flask Form submission
    @app.route('/upload', methods=['GET','POST']) 
    def upload():
        file = request.files['file']  
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path) 
 
        # Copy the file to another directory using shutil.copy() >> 
        #   couldnt find another way, otherwise it will conflict with importing original images, 
        #   on the other hand, CW demands for specific 'originals/' in root folder
        #   wouldn't recommand to create "originals/" under root, instead under "static/originals" which i already did
        destination_path = os.path.join('static', 'originals', filename) 
        shutil.copy(file_path, destination_path)

        #redirect to another flask route, pass 'filename'       
        return redirect(url_for('uploaded_file',filename=filename)) 

    @app.route('/uploads/<filename>')
    # fetches 'filename' passed from upload()
    def uploaded_file(filename): 
        PATH_TO_TEST_IMAGES_DIR = app.config['UPLOAD_FOLDER']
        TEST_IMAGE_PATHS =[os.path.join(PATH_TO_TEST_IMAGES_DIR, filename.format(i)) for i in range(1,2)]

        # connection to TF-inference-server
        stub = get_stub() 

        for image_path in TEST_IMAGE_PATHS:
            image_np = np.array(Image.open(image_path))      
            image_np_inferenced = inference(image_np,stub)[0]
            class_label = inference(image_np,stub)[1]
            det_score = inference(image_np,stub)[2]
            im = Image.fromarray(image_np_inferenced)
            im.save('static/' + filename) 
        
        # add/commit to database
            label = Users(img_label=filename,obj_detected=class_label,probability=det_score)
            db.session.add(label)
            db.session.commit()

        # retrieve the last row from the table 
        result = db.session.execute(text('SELECT * FROM users WHERE id=(SELECT max(id) FROM users);')).fetchone()
        if result:
        # convert the query result to a dictionary for easier access in the template
            row_data = {
                'id': result.id,
                'img_label': result.img_label, 
                'obj_detected': result.obj_detected,
                'probability': result.probability,
            }
        
        # let's render this baby!!!
        # pass the filename as well and fetch it from html for easier fetch, otherwise I'll need to loop the whole DIR for last saved img
        return render_template('result.html',row_data=row_data,filename=filename) 

    @app.route('/database')
    def database():

        # Query the database and retrieve the data
        data = db.session.execute(text("SELECT id, img_label, obj_detected, probability FROM users")).fetchall()
        # Pass the data to the template and render it
        return render_template('database.html', data=data)

    if __name__ == '__main__':
        db.create_all()
        app.run(host='0.0.0.0', port=5000,debug=True) # as mentioned in falsk documentation, "debug=True" might leave vulnerability
