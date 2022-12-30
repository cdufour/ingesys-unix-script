#import utils
#from utils import sumList
from utils import sumList as sl

values = []
while True:
  userInput = int(input("Saisir un chiffre (0 pour quitter le programme): "))
  if userInput == 0: # sortie de boucle
    break
  else:
    values.append(userInput) # ajout de la valeur dans la liste

valuesFormatted = str(values).replace('[', '(').replace(']',')')
print("Somme des valeurs saisies:", sl(values), valuesFormatted)