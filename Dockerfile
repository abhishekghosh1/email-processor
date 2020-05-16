FROM python:3.6.10-slim

LABEL maintainer="Abhishek Ghosh <mishu0007@gmail.com>"
LABEL description="Sample Email Preprocessor"

COPY . /build
WORKDIR /build

RUN python3 --version
RUN pip3 install --upgrade pip
RUN pip3 --version
RUN python3 manage.py db init
RUN python manage.py db migrate --message 'initial database migration'
RUN python manage.py db upgrade
RUN pip3 install -r requirements.txt \
&& apt-get clean \
&& rm -r /root/.cache \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache/*
