FROM python:3.9-alpine

WORKDIR /opt

COPY ./mortimer .

RUN pip3 install -r ./requirements/requirements-base.txt

ENV PYTHONPATH=/opt

EXPOSE 8080

ENTRYPOINT ./run.py