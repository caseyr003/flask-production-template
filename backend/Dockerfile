FROM python:3.7-slim

# for flask web server
EXPOSE 5000

# add files
ADD . /app

# set working directory
WORKDIR /app

# install required libraries
RUN pip install -r requirements.txt

# This is the runtime command for the container
# Add below line if not using docker-compose
# CMD gunicorn -w 1 -b :5000 app:app
