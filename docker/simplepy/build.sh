#!/bin/bash
IMAGE_NAME=simplepy
echo "Construction de l'image ${IMAGE_NAME}"
docker build . -t $IMAGE_NAME