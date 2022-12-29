'''
print("Donne-moi ton âge")
age = input()
print("Tu as donc", age, "ans")
'''

print("Tapez un entier, je calcule son carré")
n = int(input())
square = n * n

# équivalent:
# n = input()
# square = int(n) * int(n)
# print("Le carré de %s vaut %d" % (n, square))

print("Le carré de", n, "vaut", square)
print("Le carré de %d vaut %d" % (n, square))