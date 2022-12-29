postCodes = [
    67200, 75012, 68520, 15000, 75020,
    67200, 75012, 68520, 15000, 75020,
    67275, 75012, 68520, 17750, 75020,
    75007, 75012, 68520, 75000, 75020
]

# Combien de codes postaux parisiens ?
# 1. variable d'accumulation
# 2. parcourir la liste
# 3. recherche tout ce qui commence par 75
# 4. incrémente accu quand parisien trouvé

numParis = 0 # accu

for postCode in postCodes:
    # Approche 1
    # if postCode >= 75000 and postCode <= 75999:
    #     numParis += 1

    # Approche 2 ("commence par")
    postCodeStr = str(postCode)
    dpt = postCodeStr[:2] # slicing. Slide des 2 premiers caractères
    if dpt == "75":
        numParis += 1


print("Nombre de codes postaux parisiens:", numParis)

# Autre exemple de "slicing"
# Affichage des 3 derniers codes postaux de la liste initiale
print(postCodes[-3:])

for p in postCodes[-3:]:
    print(p)