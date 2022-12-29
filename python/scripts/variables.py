# Variables primitives en Python
temperature = 2
pi = 3.14
isEarthRound = True
training = "Initiation au langage Python"

# Affichage du type des variables
print(type(temperature)) # int
print(type(pi)) # float
print(type(isEarthRound)) # bool
print(type(training)) # str

"""
print(2+2)
print(temperature + temperature)
training = "Perfectionnement au langage Python"
print(training)
"""

# Opérations sur les variables
print(temperature + 10) # addition entre entiers
print(training + "10") # concaténation entre deux chaînes
print(pi + 10) # addition entre un float et un int
print(isEarthRound + 10) # conversion implicite, True => 1
print("Le double de pi est: " + str(pi * 2)) # fonction de conversion str()

doublePi = pi * 2 # stockage en variable du retour d'une expr. arithmétique
print(type(doublePi)) # float
doublePiStr = str(doublePi)
print(type(doublePiStr)) # str
