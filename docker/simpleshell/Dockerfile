FROM debian:11.6-slim

WORKDIR /app

# copie le fichier local app.sh vers le dossier /app de l'image
COPY app.sh .

# ajoute l'exécutabilité au fichier app.sh
RUN chmod +x app.sh

# commande de démarrage (startup command)
#CMD ["echo", "toto"]
CMD ["/bin/bash", "app.sh"]