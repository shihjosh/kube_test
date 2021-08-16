FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app
# COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

RUN apk update
RUN apk add mariadb-dev gcc
# RUN pip install mysqlclient==1.4.6
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol 


ENV PATH="/scripts:/py/bin:$PATH"

USER app

# RUN sed -i "s/archive.ubuntu./mirrors.aliyun./g" /etc/apt/sources.list
# RUN sed -i "s/deb.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list

# RUN apt-get clean && apt-get -y update && \
#     apt-get -y install libsasl2-dev python-dev libldap2-dev libssl-dev libsnmp-dev
# RUN pip3 install --index-url https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir -r requirements.txt

# COPY ./* /mytestsite/