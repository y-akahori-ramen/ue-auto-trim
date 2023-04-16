FROM python:3.9.16

RUN apt update
RUN apt upgrade
RUN apt install  --yes ffmpeg

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools 

COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/trim
COPY ./download_osr_data.py .
RUN python download_osr_data.py

COPY ./trim.py .
ENTRYPOINT ["python", "trim.py"]
