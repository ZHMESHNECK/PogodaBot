FROM python:3.9.11

WORKDIR /projects/PogodaBot

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

COPY . .