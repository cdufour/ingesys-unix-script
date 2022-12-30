f = open("files/demo.txt", "r")
#print(type(f))
content = f.read()
f.close()

newContent = content.replace("demo", "preuve")

print(content)
print(newContent)

f2 = open("files/new", "a") # création d'un nouveau fichier
f2.write(newContent)
f2.close()