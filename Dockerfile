# Pull base image
FROM python:3.9-alpine3.15

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # install dependencies 1
RUN apk update \
    && apk add --virtual build-deps gcc postgresql-dev \
    && apk add python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && apk add libffi-dev openssl-dev cargo \
    && apk del build-deps

# Install dependencies 2
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .