FROM ubuntu:20.04

RUN apt update && apt install -y python3 python3-pip && mkdir -p /app

COPY ./requirements.txt /app

WORKDIR /app
RUN pip3 install -r requirements.txt

ARG PORT=5556
ENV port $PORT
