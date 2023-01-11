#!/bin/bash

#Créer un script shell (exo1_start.sh) produisant 2 conteneurs redis dans deux versions différentes
#ainsi que 2 conteneurs mysql dans deux versions différentes (attention, variable d'environnement obligatoire MYSQL_ROOT_PASSWORD, -e)

echo "[+] démarrage de conteneurs redis"
docker run -d --name R6 redis:6 #Version 6
docker run -d --name RL redis:latest #dernière version

echo "[+] démarrage de conteneurs mysql"
docker run -d --name SQL5 -e MYSQL_ROOT_PASSWORD=toor mysql:5-debian #MySQL v5
docker run -d --name SQLL -e MYSQL_ROOT_PASSWORD=toor mysql:latest #MySQL Latest v.