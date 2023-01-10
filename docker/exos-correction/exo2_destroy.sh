#!/bin/bash

# arrêt des conteneurs
echo "[+] arrêt des conteneurs redis et mysql"
docker stop R6 RL SQL5 SQLL

# destruction des conteneurs
echo "[+] suppression des conteneurs redis et mysql"
docker rm R6 RL SQL5 SQLL