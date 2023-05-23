FROM ubuntu:20.04
USER root

RUN apt update
RUN apt install -y python3.9
RUN apt install -y python3-pip
RUN apt install -y tesseract
RUN apt install -y sentencepieces

COPY requirements.txt .
RUN python3.9 -m pip install -r requirements.txt

COPY app.py .
ENTRYPOINT ["python3.9", "app.py"]