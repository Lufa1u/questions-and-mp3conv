FROM python:3.11

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update

WORKDIR /questions-and-mp3conv

RUN useradd -rms /bin/bash web && chmod 777 /opt /run /questions-and-mp3conv

COPY --chown=questions-and-mp3conv:questions-and-mp3conv . .

RUN pip install -r requirements.txt

USER web
