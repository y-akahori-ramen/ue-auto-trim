FROM nvidia/cuda:11.8.0-base-ubuntu22.04

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y python3  python3-pip

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools 

RUN pip install easyocr==1.6.2
RUN pip install moviepy==1.0.3
