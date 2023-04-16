FROM python:3.9.16

RUN apt update
RUN apt upgrade
RUN apt install  --yes ffmpeg

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools 

RUN pip install easyocr==1.6.2
RUN pip install moviepy==1.0.3

WORKDIR /usr/trim
COPY ./download_osr_data.py .
RUN python download_osr_data.py

COPY ./trim.py .
ENTRYPOINT ["python", "trim.py"]
