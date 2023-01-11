#!/bin/bash
IMG=myredis:0.1

echo "[+] construction de l'image redis personnalisée ${IMG}"
docker build . -t $IMG