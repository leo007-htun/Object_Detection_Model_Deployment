![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=leo007-htun&show_icons=true&theme=transparent)
## Model Changes 

Inside ``saved_model/1/`` , there are one folder named ``variables/`` and  ``saved_model.pb``.

Inside ``variables/`` , there are two files, namely ``variables.index`` and ``variables.data-00000-of-00001``.

Since github doesn't allow large files, ``variables.data-00000-of-00001`` can't be uploaded. Download it from the last Session.

We need both ``variables/`` and ``model.pb`` to utilize the model.

Note that in ``saved_model/1/variables/`` we need to add the model's appropriate logged variables

``saved_model.pb`` can be replaced with any pre-trained model. Try using different models e.g ``SSD`` ``RESNET`` but must be provided with according ``variables`` and ``model.pb`` 

## Server Changes

Note that Changing ``Inference Server`` may affect the ``Model Format``.

Use the ``Model Format`` which is supported by the ``Inference Server`` that you are gonna use.

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
        
## [Download faster-rcnn-resnet101_brid_detection_model (includes saved_model and variables)](https://drive.google.com/drive/folders/1vUvF9jUEtDo8usxaifAxthUMp1mSxLmT?usp=share_link)
    
