FROM python:3.10

WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY req.txt ./

RUN pip install --upgrade pip
RUN pip install -r req.txt

COPY . /usr/src/skillFlow

CMD ['python' 'manage.py' 'runserver']