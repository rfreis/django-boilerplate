# Base Image
FROM python:3.8

# create and set working directory
RUN mkdir /app
WORKDIR /app

# install environment dependencies
COPY ./requirements.txt /app/requirements.txt
COPY ./.docker/dev.txt /app/.docker/dev.txt
RUN pip install --upgrade pip
ARG REQUIREMENTS=requirements.txt
RUN pip install -r ${REQUIREMENTS}

# Add current directory code to working directory
ADD . /app

EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "django.wsgi:application"]
