# Dockerfile for Django
FROM python:3.8

ENV PYTHONUNBUFFERED 1

# Install the PostgreSQL client library
RUN apt-get update && apt-get install -y libpq-dev

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code/
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/
