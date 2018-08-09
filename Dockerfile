FROM alpine
MAINTAINER "Andy Dustin" <andy.dustin@gmail.com>

ENTRYPOINT python3 /headers.py
EXPOSE 5000

RUN apk add python3 py3-flask
ADD headers.py /

