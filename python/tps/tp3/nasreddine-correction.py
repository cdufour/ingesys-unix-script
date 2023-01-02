import os

if not os.path.exists("flagBis"):
    os.mkdir("flagBis")
    print("le dossier est cree avec succes")

for f in os.listdir("flags"):
    if f.endswith(".png") and f !="missing.png":
        os.rename("flags/" +f, "flagBis/" +f[0:2].upper() + ".png")

print("*****The end****")