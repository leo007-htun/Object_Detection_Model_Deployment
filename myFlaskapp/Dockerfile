# get existing base image:
FROM ubuntu
FROM python:3
FROM tensorflow/tensorflow:2.4.3

#add project
ADD FlaskObjectDetection /FlaskObjectDetection

# download and install any dependencies:
RUN apt-get update
RUN apt-get install --fix-missing
RUN pip install Flask
RUN pip install tensorflow==2.5.2
RUN pip install Flask-WTF
RUN pip install opencv-python
RUN pip install pafy
RUN pip install Pillow
RUN pip install Werkzeug
RUN pip install numpy==1.19.2
RUN pip install grpcio
RUN pip install Flask-SQLAlchemy
RUN pip install Flask-Migrate==3.0.1
RUN pip install SQLAlchemy
RUN pip install tensorflow-serving-api==2.5.2
RUN pip install matplotlib
RUN pip install pymysql
RUN pip install mysql-connector-python


# set the default command:
WORKDIR "./FlaskObjectDetection"
CMD ["python","./app.py"]