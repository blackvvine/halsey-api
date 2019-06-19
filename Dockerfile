
FROM ubuntu:16.04

USER root

RUN apt update

COPY src /root/halsey

WORKDIR /root/halsey

RUN bash requirements.sh

RUN apt install -y python3 python3-pip

RUN pip3 install -r requirements.txt

RUN apt install -y curl

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

RUN apt-get update && apt-get install -y google-cloud-sdk

COPY conf/key.json /root/

RUN gcloud auth activate-service-account --key-file=/root/key.json
RUN gcloud config set project phdandpeasant



