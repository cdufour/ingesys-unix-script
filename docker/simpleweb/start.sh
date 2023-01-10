#!/bin/bash

IMAGE=simpleweb:1.0.0
NETWORK=simpleweb

echo "[+] construction de l'image ${IMAGE}"
docker build . -t $IMAGE

echo "[+] création du réseau privé ${NETWORK}"
docker network create $NETWORK

echo "[+] création d'un conteneur redis"
docker run --name redis -d --network $NETWORK redis:6-alpine

echo "[+] création d'un conteneur pour l'application simpleweb"
docker run --name web -d -p 3000:3000 --network $NETWORK $IMAGE