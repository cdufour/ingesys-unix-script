#!/bin/bash
IMAGE_NAME=simplepy

echo "[+] Lancement de 3 conteneurs basés sur l'image ${IMAGE_NAME}"
docker run --name s1 -d $IMAGE_NAME
docker run --name s2 -d -e SLEEP_DURATION=10 $IMAGE_NAME
docker run --name s3 -d -e SLEEP_DURATION=30 $IMAGE_NAME