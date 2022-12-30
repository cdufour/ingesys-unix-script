students = ["Augustin", "Karim", "Alexandra", "Rawia"]

content = "Fichier appartenant à "

for s in students:
    # création du nom du fichier
    filepath = "files/evaluation_" + s[:4].lower() + ".txt"
    f = open(filepath, "w")
    f.write(content + s)
    f.close()
    