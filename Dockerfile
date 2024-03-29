FROM python:3.10

WORKDIR /DjangoNotifications

COPY .. .

COPY reqirements.txt /temp/reqirements.txt

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install -r /temp/reqirements.txt

