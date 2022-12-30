def hello():
    print("Hello")
    # return None # retour implicite

def hello2():
    return "Hello again !"

def addTwo(n):
    return n + 2

def square(n):
    return n * n

def sum(a, b):
    return a + b


r = hello() # r reçoit pour None
print(r)
print(hello2())

print(addTwo(5))
finalValue = addTwo(addTwo(addTwo(5))) # 5 => 7 => 9 => 11
print(finalValue) # 11

print(square(5))

print(sum(4, 1) + sum(6, 4))

# Affichage du carré pour toutes les valeurs itérées sup. ou égales à 10
numbers = [6,4,40,10,8,15]
for n in numbers:
    if n >= 10:
        print(n, "=>", square(n))