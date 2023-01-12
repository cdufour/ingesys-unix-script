# Module Kubernetes

## Installation
- [Démarrer avec minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Installer kubectl](https://kubernetes.io/fr/docs/tasks/tools/install-kubectl/)

- [Installation de la vm minikube - vidéo](https://opusidea-training.s3.eu-west-3.amazonaws.com/divers/demo/2022-10-04-install-minikube-vm.webm)
- [Installation du client kubectl - vidéo](https://opusidea-training.s3.eu-west-3.amazonaws.com/divers/demo/2022-10-04-install-kubectl.webm)

## Commandes minikube
```bash
minikube start --driver=virtualbox --no-vtx-check
minikube status
minikube ssh
minikube stop
minikube delete

# addons
minikube addons list
minikube addons enable dashboard
minikube addons enable metrics-server
```

## Liens utiles
- [Slides formateur](https://opusidea-training.s3.eu-west-3.amazonaws.com/presentation/ajc/Kubernetes.pdf)
- [Aide-mémoire kubectl](https://kubernetes.io/fr/docs/reference/kubectl/cheatsheet/)
- [Référence kubectl](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)
- [Killercoda Kubernetes Playground](https://killercoda.com/kubernetes/scenario/a-playground)


### Pour aller plus loin

## Horizontal Pod Autoscaling
[Vidéo formateur - FR - format .webm](https://opusidea-training.s3.eu-west-3.amazonaws.com/divers/demo/2022-12-06-k8s-hpa.webm)

## Cluster multi-noeuds - positionnement de pods
[Vidéo formateur - FR - format .webm](https://opusidea-training.s3.eu-west-3.amazonaws.com/divers/demo/2022-12-06-k8s-assign-pod-to-nodes.webm)

## rbac/role/rolebinding
- [RBAC with Kubernetes in Minikube](https://medium.com/@HoussemDellai/rbac-with-kubernetes-in-minikube-4deed658ea7b)
- [Kubernetes Roles and Users (RBAC For k8s)](https://dev.to/thenjdevopsguy/kubernetes-roles-and-users-rbac-for-k8s-44n4)

## StatefulSet
[Kubernetes StatefulSet simply explained | Deployment vs StatefulSet - youtube - EN)](https://youtu.be/pPQKAR1pA9U)

## DaemonSets
[Kubernetes: The Basics | DaemonSets - youtube - EN](https://youtu.be/cdY67JqGbIc)

## Taints & Tolerations
[Kubernetes For Beginners: Taints & Tolerations - youtube - EN](https://youtu.be/mo2UrkjA7FE)

## CI/CD
[CICD Pipeline To Deploy To Kubernetes Cluster Using Jenkins | Jenkins Kubernetes Integration - youtube - EN](https://youtu.be/XE_mAhxZpwU)