import os
import shutil

if not os.path.exists('flagsBis'):
  os.mkdir('flagsBis')
  print("[+] dossier flagBis créé")

# parcours des drapeaux d'origine
for f in os.listdir('../flags'):
  if f.endswith(".png") and f != "missing.png":
    shutil.copyfile('../flags/' + f, 'flagsBis/' + f[:2].upper() + '.png')
    print("[+] drapeau %s copié et renommé" % f)