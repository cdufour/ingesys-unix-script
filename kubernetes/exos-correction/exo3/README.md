kubectl cp files/script.sql db:/tmp
kubectl exec -it -- sh
mysql -p projet1 < /tmp/script.sql

# secret
azerty => base64 => YXplcnR5
kubectl create secret generic db-password --from-file=./files/db-password