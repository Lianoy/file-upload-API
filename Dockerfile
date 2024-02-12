FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip --no-cache-dir -r /requirements.txt

RUN mkdir /code
WORKDIR /code
COPY ./ /code

EXPOSE 8000
EXPOSE 5555
EXPOSE 5672