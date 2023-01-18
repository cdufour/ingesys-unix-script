# Module Jenkins

## Installation
### Construction de l'image docker de Jenkins incluant le plugin BlueOcean
```
docker build -t myjenkins-blueocean:2.332.3-1 .
```

### Création d'un réseau "jenkins"
```
docker network create jenkins
```

### Exécution du conteneur docker
#### MacOS / Linux
```
docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.332.3-1
```

#### Windows
```
docker run --name jenkins-blueocean --restart=on-failure --detach `
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 `
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 `
  --volume jenkins-data:/var/jenkins_home `
  --volume jenkins-docker-certs:/certs/client:ro `
  --publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.332.3-1
```

### Connection au serveur jenkins
```
https://localhost:8080/
```

### Obtention du mot de passe initial d'administration de jenkins
```
docker exec jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword
```

### Référence pour l'installation
https://www.jenkins.io/doc/book/installing/docker/


### Conteneur alpine/socat pour rediriger le trafic de jenkins vers un autre conteneur
https://stackoverflow.com/questions/47709208/how-to-find-docker-host-uri-to-be-used-in-jenkins-docker-plugin
```
docker run --name docker -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock

docker inspect <container_id> | grep IPAddress
```

### Utilisation d'un agent jenkins python
```
docker pull devopsjourney1/myjenkinsagents:python
```

## Tutos
- [Learn Jenkins! Complete Jenkins Course - Zero to Hero - youtube - EN](https://youtu.be/6YZvp2GwT0A)
- [Jenkins Tutorials - youtube playlist - EN](https://youtube.com/playlist?list=PLvBBnHmZuNQJeznYL2F-MpZYBUeLIXYEe)