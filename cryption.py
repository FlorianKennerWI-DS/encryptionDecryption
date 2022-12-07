import argparse
import sys
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as PBKDF2HMAC

parser = argparse.ArgumentParser()
parser.add_argument("--decrypt", required=False, action= "store_true", default=False)
parser.add_argument("--encrypt", required=False, action= "store_true", default=False)

def generate_fernet(password: str):
    salt = b'\x93A\xc3\x11R\xbd\x89i%xPZ\xd4s\xb5\xe1\x07\xbf\x81MX\xabr\x04o\x19\xdf\xaad\x96v\x98'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return Fernet(key)

def encrypt_files(fernet: Fernet):
    encrypted_files = []
    for root, dirs, files in os.walk("./"):
        for file in files:
            if not file == "cryption.py" and not file == "main.py":
                encrypted_files.append(file)
                with open(os.path.join(root, file), "rb") as f:
                    data = f.read()
                with open(os.path.join(root, file), "wb")as f:
                    f.write(fernet.encrypt(data))
    with open("encrypted_files.txt", "w") as f:
        f.write(str(encrypted_files))

def decrypt_files(fernet: Fernet):
    with open("./encrypted_files.txt") as file:
        encrypted_files = file.read()
    encrypted_files = encrypted_files.split(",")
    encrypted_files = [x.strip(" '[]") for x in encrypted_files]
    for root, dirs, files in os.walk("./"):
        for file in files:
            if file in encrypted_files:
                with open(os.path.join(root, file), "rb") as f:
                    data = f.read()
                with open(os.path.join(root, file), "wb") as f:
                    f.write(fernet.decrypt(data))
    os.remove("encrypted_files.txt")

if __name__ == "__main__":
    args = parser.parse_args()
    if (args.decrypt == args.encrypt):
        print("You have to choose between encrypting or decrypting")
        sys.exit(1)

    password = ""
    if args.encrypt:
        print("Encrypting files...")
        while True:
            password = input("Enter the encryption phrase:\n")
            if input("Enter the encryption phrase again:\n") == password:
                break
            else:
                print ("The phrases do not match. Try again.")
    elif args.decrypt:
        print("Decrypting files...")
        password = input("Enter the decryption phrase:\n")

    fernet = generate_fernet(password)
    if args.encrypt:
        encrypt_files(fernet)

    if args.decrypt:
        decrypt_files(fernet)
    print("Done")