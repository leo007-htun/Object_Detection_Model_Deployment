~simply create new directory and pull this repo

~Note that in saved_model/1/variables/ ==> we need to add the model's appropriate logged variables

~To run the TF-SErving, you must have already installed docker and TF-Serving image

~ After that bind the ports: and docker run that container by this cmd:

"sudo docker run --gpus all -p 8500:8500 --name od --mount type=bind,source=/home/...USR_DIR/tf_obj_detect_faster_rcnn/saved_model,target=/models/od -e MODEL_NAME=od -t tensorflow/serving:latest-gpu
"

~ at last simply run 'app.py' and upload the images, TF-serving will inference and give back the results
