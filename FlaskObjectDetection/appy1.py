from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import numpy as np
import os
import sys
import tensorflow as tf
from PIL import Image
import time
import cv2 #new
import grpc #new

sys.path.append("..")
from utils import label_map_util
from utils import visualization_utils as viz_utils

tf.get_logger().setLevel('ERROR')


#PATH_TO_SAVED_MODEL = "./saved_model"
PATH_TO_SAVED_MODEL = "/home/msc1/Desktop/Labs/Semester_2/7147COMP/CW3/saved_model/1/"
PATH_TO_LABELS = "./data/label_map.pbtxt"
NUM_CLASSES = 4

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
config = tf.compat.v1.ConfigProto(allow_soft_placement=True)

config.gpu_options.per_process_gpu_memory_fraction = 0.3
tf.compat.v1.keras.backend.set_session(tf.compat.v1.Session(config=config))

print('Loading model...', end='')
start_time = time.time()

# Load saved model and build the detection function
detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)

end_time = time.time()
elapsed_time = end_time - start_time
print('Done! Took {} seconds'.format(elapsed_time))

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def inference(image_np):

    # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
    input_tensor = tf.convert_to_tensor(image_np)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = input_tensor[tf.newaxis, ...]

    # input_tensor = np.expand_dims(image_np, 0)
    detections = detect_fn(input_tensor)

    # All outputs are batches tensors.
    # Convert to numpy arrays, and take index [0] to remove the batch dimension.
    # We're only interested in the first num_detections.
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                   for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    image_np_with_detections = image_np.copy()

    viz_utils.visualize_boxes_and_labels_on_image_array(
          image_np_with_detections,
          detections['detection_boxes'],
          detections['detection_classes'],
          detections['detection_scores'],
          category_index,
          use_normalized_coordinates=True,
          max_boxes_to_draw=200,
          min_score_thresh=.30,
          agnostic_mode=False)
    
    return (image_np_with_detections)
    
def _build_conv_hyperparams(self):
    conv_hyperparams = hyperparams_pb2.Hyperparams()
    conv_hyperparams_text_proto = """
      regularizer {
        l2_regularizer {
        }
      }
      initializer {
        truncated_normal_initializer {
        }
      }
    """
    text_format.Parse(conv_hyperparams_text_proto, conv_hyperparams)
    return hyperparams_builder.KerasLayerHyperparams(conv_hyperparams)

def _build_feature_extractor(self):
    return frcnn_res_fpn.FasterRCNNResnet50FpnKerasFeatureExtractor(
        is_training=False,
        conv_hyperparams=self._build_conv_hyperparams(),
        first_stage_features_stride=16,
        batch_norm_trainable=False,
        weight_decay=0.0)

def test_extract_proposal_features_returns_expected_size(self):
    feature_extractor = self._build_feature_extractor()
    preprocessed_inputs = tf.random_uniform(
        [2, 448, 448, 3], maxval=255, dtype=tf.float32)
    rpn_feature_maps = feature_extractor.get_proposal_feature_extractor_model(
        name='TestScope')(preprocessed_inputs)
    features_shapes = [tf.shape(rpn_feature_map)
                       for rpn_feature_map in rpn_feature_maps]

    self.assertAllEqual(features_shapes[0].numpy(), [2, 112, 112, 256])
    self.assertAllEqual(features_shapes[1].numpy(), [2, 56, 56, 256])
    self.assertAllEqual(features_shapes[2].numpy(), [2, 28, 28, 256])
    self.assertAllEqual(features_shapes[3].numpy(), [2, 14, 14, 256])
    self.assertAllEqual(features_shapes[4].numpy(), [2, 7, 7, 256])

def test_extract_proposal_features_half_size_input(self):
    feature_extractor = self._build_feature_extractor()
    preprocessed_inputs = tf.random_uniform(
        [2, 224, 224, 3], maxval=255, dtype=tf.float32)
    rpn_feature_maps = feature_extractor.get_proposal_feature_extractor_model(
        name='TestScope')(preprocessed_inputs)
    features_shapes = [tf.shape(rpn_feature_map)
                       for rpn_feature_map in rpn_feature_maps]

    self.assertAllEqual(features_shapes[0].numpy(), [2, 56, 56, 256])
    self.assertAllEqual(features_shapes[1].numpy(), [2, 28, 28, 256])
    self.assertAllEqual(features_shapes[2].numpy(), [2, 14, 14, 256])
    self.assertAllEqual(features_shapes[3].numpy(), [2, 7, 7, 256])
    self.assertAllEqual(features_shapes[4].numpy(), [2, 4, 4, 256])

def test_extract_box_classifier_features_returns_expected_size(self):
    feature_extractor = self._build_feature_extractor()
    proposal_feature_maps = tf.random_uniform(
        [3, 7, 7, 1024], maxval=255, dtype=tf.float32)
    model = feature_extractor.get_box_classifier_feature_extractor_model(
        name='TestScope')
    proposal_classifier_features = (
        model(proposal_feature_maps))
    features_shape = tf.shape(proposal_classifier_features)

    self.assertAllEqual(features_shape.numpy(), [3, 1, 1, 1024])


@app.route('/')
def index():
    return render_template('index4.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',
                                filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    PATH_TO_TEST_IMAGES_DIR = app.config['UPLOAD_FOLDER']
    TEST_IMAGE_PATHS = [os.path.join(PATH_TO_TEST_IMAGES_DIR, filename.format(i)) for i in range(1, 2)]
    IMAGE_SIZE = (12, 8)

    for image_path in TEST_IMAGE_PATHS:
        image_np = np.array(Image.open(image_path))
        image_np_inferenced = inference(image_np)
        im = Image.fromarray(image_np_inferenced)
        im.save('uploads/' + filename)

    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
