FROM python:3.11.5

ARG PROJECT=vestigo
ARG PROJECT_DIR=/${PROJECT}
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR

RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

