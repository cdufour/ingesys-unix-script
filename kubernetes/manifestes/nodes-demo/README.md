# Nodes Demo

Sources:  
- [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [Assign Pods to Node (nodeSelector)](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/)  

## Commandes
```bash
# liste détaillée des nodes
kubectl get no -o wide

# description d'un node
kubectl describe no/<node-name>

# affichage des labels
kubectl get no --show-labels

# attribution d'un label au node cibe
kubectl label no <node-name> workenv=dev

# application d'un pod nginx sur node portant le label "workenv=dev"
kubectl apply -f pod-nginx.yaml

# application d'un pod nginx sur node nommé (remplacer <node-name> par le nom du node ciblé dans le manifeste)
kubectl apply -f pod-nginx-specific-node.yaml

# nettoyage
kubectl delete pod --all
```