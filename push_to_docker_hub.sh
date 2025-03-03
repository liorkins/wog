#!/bin/bash

# Variables
IMAGE_NAME="your_dockerhub_username/myflaskapp"
TAG="latest"

# Build the image
docker-compose build

# Tag the image
docker tag myflaskapp:latest $IMAGE_NAME:$TAG

# Log in to Docker Hub
docker login --username your_dockerhub_username --password your_dockerhub_password

# Push the image
docker push $IMAGE_NAME:$TAG

# Log out from Docker Hub
docker logout

chmod +x push_to_docker_hub.sh
docker-compose up