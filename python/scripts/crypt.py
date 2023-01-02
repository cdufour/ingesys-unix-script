import os
import argparse

# dépendance du module communautaire: https://pypi.org/project/cryptography/
from cryptography.fernet import Fernet

class Crypt:
    def __init__(self):
        # variante
        # self.key = Fernet.generate_key()
        self.key = b'Lv-NCGOgattoqxRj8qKg7nLTximeYUrksmYegHM5XIA='
        self.fernet = Fernet(self.key)

    def encrypt(self, file_path):
        base_name = os.path.basename(file_path).split(".")[0]
        out_file = f"files/{base_name}.enc" # concaténation

        with open(file_path, "rb") as f:
            data = f.read()

        # fernet pour encrypter les données
        encrypted = self.fernet.encrypt(data)

        with open(out_file, "wb") as f:
            f.write(encrypted)
        
        print(f"Fichier crypté: {out_file}\n")

        # suppresion du fichier clair (attention)
        os.remove(file_path)

    def decrypt(self, file_path, out_ext="txt"):
        base_name = os.path.basename(file_path).split(".")[0]
        out_file = f"files/{base_name}.{out_ext}"

        with open(file_path, "rb") as f:
            data = f.read()

        decrypted = self.fernet.decrypt(data)

        with open(out_file, "wb") as f:
            f.write(decrypted)

        print(f"Fichier décrypté: {out_file}\n")


parser = argparse.ArgumentParser()
parser.add_argument("-e", "--encrypt")
parser.add_argument("-d", "--decrypt")
parser.add_argument("-x", "--ext", default="txt")

args = parser.parse_args()

crypt = Crypt()

if args.encrypt:
    print("Fichier à encrypter:", args.encrypt)
    crypt.encrypt(args.encrypt)
elif args.decrypt:
    print("Fichier à décrypter:", args.decrypt)
    if args.ext:
        crypt.decrypt(args.decrypt, args.ext)
    else:
        crypt.decrypt(args.decrypt)



