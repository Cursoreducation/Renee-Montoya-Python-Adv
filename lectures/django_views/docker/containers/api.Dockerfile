FROM python:3.9-slim

RUN apt-get update && apt-get install -y gettext

ADD . /trello

ENV PYTHONPATH "${PYTHONPATH}:/trello"
ENV PYTHONUNBUFFERED 1

RUN chmod +x /trello/docker/scripts/api.entrypoint.dev.sh && \
    chmod +x /trello/docker/scripts/wait-for-it.sh

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /trello/requirements/dev.txt
