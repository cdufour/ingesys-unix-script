# import du module requests pour effectuer une requête http
import requests

# exécution d'une requête http en GET sur l'url fournie en entrée
x = requests.get('https://w3schools.com/python/demopage.htm');

# affichage du corps (format texte) de la réponse http
print(x.text)