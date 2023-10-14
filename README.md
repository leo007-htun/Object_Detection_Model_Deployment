<div align="center">
  
[![PyPI - Python Version](https://img.shields.io/badge/Python-%3E%3D%203.9-blue)](https://www.python.org/)
[![Docker Version](https://img.shields.io/badge/Docker-%3E%3D%2020.10.5-blue)](https://www.docker.com/)
[![TensorFlow Version](https://img.shields.io/badge/TensorFlow-2.5.0-orange)](https://www.tensorflow.org/)
[![Built with Flask](https://img.shields.io/badge/Built%20with-Flask-red)](https://flask.palletsprojects.com/)
[![Built with TF-Serving](https://img.shields.io/badge/Built%20with-TF--Serving-green)](https://www.tensorflow.org/tfx/guide/serving)
[![TF Object Detection API](https://img.shields.io/badge/TF%20Object%20Detection-API-orange)](https://github.com/tensorflow/models/tree/master/research/object_detection)

</div>

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=leo007-htun&show_icons=true&theme=transparent)

https://github.com/leo007-htun/Object_Detection_Model_Deployment/assets/66962471/3cd7579d-a944-4281-94f7-a3e73f4ae8d1

## Model Changes 

Inside ``saved_model/1/`` , there are two folders named ``variables/`` and  ``saved_model.pb``.

Inside ``variables/`` , there are two files, namely ``variables.index`` and ``variables.data-00000-of-00001``.

Since github doesn't allow large files, ``variables.data-00000-of-00001`` can't be uploaded. Download it from the last Session

We need both ``variables/`` and ``model.pb`` to utilize the model.

Note that in ``saved_model/1/variables/`` we need to add the model's appropriate logged variables

``saved_model.pb`` can be replaced with any pre-trained model. Try using different models e.g ``SSD`` ``RESNET`` but must be provided with according ``variables`` and ``model.pb`` 

## Server Changes

Note that Changing ``Inference Server`` may affect the ``Model Format``

Use the ``Model Format`` accordingly which is supported by the type of ``Inference Server`` 

## RUN MANUALLY
  
1. simply create new directory and pull this repo

2. To run the TF-Serving, you must have already installed docker and TF-Serving image

3. After that bind the ports: and docker run that container by this cmd:

        sudo docker run --gpus all -p 8500:8500 --name od --mount type=bind,source=/home/...USR_DIR.../tf_obj_detect_faster_rcnn/saved_model,target=/models/od -e MODEL_NAME=od -t tensorflow/serving:latest-gpu 

4. At last simply run 'app.py' and upload the images, TF-serving will inference and give back the results

        python app.py 
        
## RUN EASY WAY (DOCKER_COMPOSE)
 
 1. run ```--build``` to build docker compose
 
        sudo docker compose up --build
    
2. run ```docker compose up``` to create container images and up-running, if you have already run ```sudo docker compose up --build``` , you can neglect the below cmd:

        sudo docker compose up
   
3. stop and remove container images:

        sudo docker compose down
        
## [Download ``variables.data-00000-of-00001`` here](https://www.dropbox.com/scl/fi/o5eygjw6h24d2kycsve4e/variables.data-00000-of-00001?rlkey=yl7eksoyjl22k3wx0dcvrjtqt&dl=0)
    
