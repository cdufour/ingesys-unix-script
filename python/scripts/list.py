# liste de 3 entiers
numbers = [23, 140, 0]
print(type(numbers)) # list

for n in numbers:
    print(n)

first = numbers[0]
print(first)
computedIndex = 1 + 1
print(numbers[computedIndex])

count = 0
while count < 3:
    print(numbers[count])
    count += 1

title = "Les Trois Mousquetaires"
print(title[4])
for c in title:
    print(c)

acc = 0 # variable accumulateur
search = "e"

for c in title:
    if c == search:
        acc += 1

print("Le caractère %s a été trouvé %d fois dans le titre %s" % (search, acc, title))