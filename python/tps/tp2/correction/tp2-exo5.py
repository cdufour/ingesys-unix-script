x = [4, 6, 8, 24, 12, 2]

# variante 1
#print(max(x))

# variante 2, fonction perso
def mymax(list):
  m = list[0] # max par défaut: premier élément de la liste
  #for n in list:
  for in in list[1:]: # variante, itère sur un slice excluant le premier indice
    if n > m:
      m = n
  return m

print(mymax(x))