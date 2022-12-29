from random import randint

secret = randint(0,10)
answer = ""

while True:
  answer = int(intput("Devine mon chiffre secret: "))
  if answer == secret:
    print("Bravo, mon secret était bien %d" % secret)
    break
  if answer > secret:
    print("C'est moins")
  else:
    print("C'est plus")