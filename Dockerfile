
FROM ubuntu:16.04

USER root

RUN apt update

COPY src /root/halsey

WORKDIR /root/halsey

RUN bash requirements.sh
RUN pip install -r requirements.txt