# Exo 1

A partir du dossier src/ créer un pipeline gitlab-ci à deux phases:
- phase1: 
    - redirection de la sortie de l'exécution du *script.py* dans un fichier *index.html*
    - modification du fichier *index.html* en remplaçant le mot _Test_ par le mot _Demo_
- phase2:
    - création et "artefacting" d'un fichier "output.txt" contenant:
        - l'url de la page initialement téléchargée par le script python (https://w3schools.com/python/demopage.htm)
        - le nombre de caractères que contient cette page
