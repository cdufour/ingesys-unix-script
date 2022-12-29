# data source
proverbs = [
    "Pierre qui roule n'amasse pas mousse",
    "Une hirondelle ne fait pas le printemps",
    "Tra il dire e il fare c'è di mezzo il mare",
    "Ad Astra per Aspera",
    "Bsahtek"
]

# Affichage aléatoire de l'un des proverbes
from random import randint, choice

#print(choice(proverbs))

indexMax = len(proverbs) - 1
print(proverbs[randint(0, indexMax)])

