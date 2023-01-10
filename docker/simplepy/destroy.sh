#!/bin/bash
echo "[+] Destruction des contenurs"
docker stop s1 s2 s3
docker rm s1 s2 s3