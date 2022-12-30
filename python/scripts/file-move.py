import os

#os.mkdir("blabla")

# if not os.path.exists("blabla"):
#     os.mkdir("blabla")
#     print("[+] blabla dir created")

# try:
#     os.rmdir("blabla")
# except FileNotFoundError:
#     print("Le dossier n'existe pas")
#     exit(1)

# Objectif: déplacer les fichiers .log situé dans le dossier files
for f in os.listdir("files"):
    if f.endswith(".log"):
        os.rename("files/" + f, "files/logs/" + f)
        print("[+] file %s moved" % f)


print("*** The End ***")