from sys import argv

n = int(argv[1]) # approche optimiste (pas de vérification)

if n < 0 or n > 1000:
  print("Doit être compris entre 0 et 1000")
  exit(1) # 1 : return code

for i in range(11):
  #print("%d x %d = %d" % (n, i, n * i))

  # variante
  print(f"{n} x {i} = {n * i}")