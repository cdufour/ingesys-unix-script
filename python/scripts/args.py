import sys

# Affichage de tous les arguments (type list) fournis en ligne de commande
print(sys.argv)

# Affichage du premier argument de ligne de commande
print(sys.argv[1])

# Affichage du carré la valeur saisie en premier arg
# Pas de vérification des entrées => erreurs possibles
arg1 = int(sys.argv[1])
print(arg1 * arg1)
