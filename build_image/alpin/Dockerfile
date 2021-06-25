FROM alpine:latest

RUN apk --no-cache add curl
RUN apk update
RUN apk add git
RUN apk add rsync
RUN rm -rf /var/cache/apk/*
RUN mkdir /root/aws
RUN mkdir /root/gitlab
