#!/bin/bash

NETWORK=simpleweb

echo "[+] destruction des conteneurs web et redis"
docker rm -f web redis

echo "[+] destruction du réseau ${NETWORK}"
docker network rm $NETWORK
