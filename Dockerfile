#######################################################
# Base Image with common settings
FROM python:3.11.7 AS base
# SET env vars
ENV PYTHONUNBUFFERED 1
# create /code folder
RUN mkdir /code
# Change path to app path
WORKDIR /code
# Copy entrypoint
COPY ./docker-entrypoint.sh /code/docker-entrypoint.sh
# Executable access to entrypoint script
RUN chmod +x /code/docker-entrypoint.sh
# install pipenv package manager
RUN python3 -m pip install pipenv
# Start Server
ENTRYPOINT [ "/code/docker-entrypoint.sh"]

#######################################################
# Development
# Pull base image from python:3
FROM base AS development
# copy all source code to /code
ADD Pipfile Pipfile.lock /code/
# install all dependencies as base path packages
RUN pipenv install --system --dev


#######################################################
# Production (and staging) deploy
# Pull base image from python:3
FROM base AS production
# copy all source code to /code
COPY . /code
# install all dependencies as base path packages
RUN pipenv install --system --deploy --ignore-pipfile
# Open port 80
EXPOSE 80
# Set env
ENV APP_PORT=80
