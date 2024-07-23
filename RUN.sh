#!/usr/bin/env bash

## BUILD THE DOCKER IMAGE
echo "BUILDING the Docker image ..."
docker build -t dasher .

## RUN THE DOCKER CONTAINER
echo "RUNNING the Docker container ..."
docker run -p 1995:1995 --volume "$(pwd)":/server dasher