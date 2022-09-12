FROM python:3.9-alpine3.16

LABEL Patryk Barton

COPY . /odysseus_app

WORKDIR /odysseus_app

RUN apk add build-base

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]
