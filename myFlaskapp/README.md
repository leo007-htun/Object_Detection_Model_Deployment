## RUN without docker build or docker compose 

To run flask app to classify bird species, we need to run tf-inference-server and flask python 

Before that, we need to pull ``tensorflow-serving`` image from dockerhub. (https://hub.docker.com/r/bitnami/tensorflow-serving)

    $ docker pull bitnami/tensorflow-serving:latest
    
RUN tf-serving container with specified port from tf-serving with '8500'

        $ sudo docker run --gpus all -p 8500:8500 --name od --mount type=bind,source=/home/msc1/Desktop/Labs/Semester_2/7147COMP/Week_8/saved_model,target=/models/od -e MODEL_NAME=od -t tensorflow/serving:latest-gpu

navigate to the specific directory to run flask python (app.py)

        $ cd [..your home directory..]/Week_8_f/myFlaskapp/FlaskObjectDetection
        $ python app.py
        
click on the IP and start uploading images
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
FROM this point we have two options: 1) docker build and create images 2) Docker compose

    1) docker build : for docker build, since tf-serving has its own image on dockerhub, docker build for tf-serving is unnecessary.
        However, we need to docker build for flask app to create container image, to proceed:

        nagivate to directory where 'Dockerfile' exists
            $ cd [..your home directory..]/Week_8_f/myFlaskapp/

        'flask/last', 'flask' is the image name and 'last' is the tag name, all should be in small letters. 'open_cv' library normally takes longer to install. docker build screenshots are in this directory 'Week_8_f/myFlaskapp/'
            $ sudo docker build -t flask/last . 

        now run both containers images
        if 'tf-serving container ' is already runninng in the background, we don't need to run it again but if it's not run this cmd
            $ sudo docker run --gpus all -p 8500:8500 --name od --mount type=bind,source=/home/msc1/Desktop/Labs/Semester_2/7147COMP/Week_8/saved_model,target=/models/od -e MODEL_NAME=od -t tensorflow/serving:latest-gpu

            NOTE HERE (NOT MENDATORY):: even if u stop the 'tf-serving' container, the image container NAME may cause conflict, thus, you can change it into another name as below
            $ sudo docker run --gpus all -p 8500:8500 --name tf --mount type=bind,source=/home/msc1/Desktop/Labs/Semester_2/7147COMP/Week_8/saved_model,target=/models/od -e MODEL_NAME=od -t tensorflow/serving:latest-gpu

        run flask image we juz created with the localhost and port '5000' as in 'app.py'
            $ sudo docker run -p 127.0.0.1:5000:5000 flask/last

    2) docker compose : for docker compose, we don't necessarily need to docker build seperately, since 'docker compose' will build 'flask app' service, a Docker image from the current directory and exposes port 5000, the 'Dockerbuild' file inside will be build by 'docker compose up' with 'build: .' line. The tf-serving service uses the tensorflow/serving:latest-gpu image, which provides TensorFlow Serving with GPU support. It exposes port 8500 and sets the MODEL_NAME environment variable to "od". It also mounts the /home/msc1/Desktop/Labs/Semester_2/7147COMP/Week_8_f/myFlaskapp/saved_model/ directory on the host to the /models/od directory in the container, which allows TensorFlow Serving to serve the saved model stored in that directory.

        nagivate to directory where 'docker-compose.yml' exists
            $ cd [..your home directory..]/Week_8_f/myFlaskapp/       
            $ sudo docker compose up 

            sometimes it won't build the necessary files, in that case run
            $ sudo docker compose up --build

            when you want to stop and remove containers,
            $ sudo docker compose down

    "DOCKER IS AMAZING INDEED!!!"

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
