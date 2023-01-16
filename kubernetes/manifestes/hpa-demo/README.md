# Démo HorizontalPodAutoscaler

Source: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/  

## Commandes
```bash
kubectl apply -f php-apache.yaml
# ou:
kubectl apply -f https://k8s.io/examples/application/php-apache.yaml

# création impérative d'un objet HorizontalPodAutoscaler
kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10

kubectl get hpa

# création d'un pod générateur de charge (envoi massive de requêtes http sur le service php-apache)
kubectl run load-generator --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"

# Ctrl+C pour mettre fin à la surveillance du hpa
kubectl get hpa php-apache --watch

# suppression des ressources
kubectl delete deploy/php-apache hpa/php-apache svc/php-apache
```

## Notes
Pour que le HPA fonctionne il peut être nécessaire d'installer le "Kubernetes Metrics Server".  
```bash
# Déploiement
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Vérification
kubectl get deployment metrics-server -n kube-system
```  
[Lien](https://stackoverflow.com/questions/43968485/horizontal-pod-autoscaling-not-working-unable-to-get-metrics-for-resource-cpu)