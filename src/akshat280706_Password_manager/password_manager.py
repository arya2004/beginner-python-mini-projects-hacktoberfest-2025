import json, os, base64
from getpass import getpass
from pathlib import Path
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend

VAULT_FILE = Path.home() / ".tiny_vault.bin"
SALT_SIZE, ITER = 16, 390000

def derive_key(password: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt,
                     iterations=ITER, backend=default_backend())
    return base64.urlsafe_b64encode(kdf.derive(password))

def init_vault():
    if VAULT_FILE.exists(): return
    p1 = getpass("Create a master password: ").encode()
    p2 = getpass("Confirm your password: ").encode()
    if p1 != p2: print("sorry, both passwords don't match."); exit()
    salt = os.urandom(SALT_SIZE)
    key = derive_key(p1, salt)
    f = Fernet(key)
    VAULT_FILE.write_bytes(base64.b64encode(salt + f.encrypt(b"{}")))
    print("Vault created at", VAULT_FILE)

def load_vault():
    if not VAULT_FILE.exists(): init_vault()
    raw = base64.b64decode(VAULT_FILE.read_bytes())
    salt, ct = raw[:SALT_SIZE], raw[SALT_SIZE:]
    key = derive_key(getpass("Master password is: ").encode(), salt)
    try: data = json.loads(Fernet(key).decrypt(ct).decode())
    except: print("this is a wrong password or corrupted vault."); exit()
    return data, salt, key

def save_vault(data, salt, key):
    f = Fernet(key)
    ct = f.encrypt(json.dumps(data).encode())
    VAULT_FILE.write_bytes(base64.b64encode(salt + ct))

def add_entry(data):
    name = input("Enter your Name: ").strip()
    user = input("Enter your username: ")
    pwd = getpass("Password (empty to generate): ")
    if not pwd:
        import secrets, string
        pwd = ''.join(secrets.choice(string.ascii_letters+string.digits) for _ in range(16))
        print("Generated:", pwd)
    notes = input("Notes: ")
    data[name] = {"user": user, "password": pwd, "notes": notes}
    print("Added.")

def show_entry(data):
    name = input("Name: ").strip()
    e = data.get(name)
    if e: [print(f"{k}: {v}") for k, v in e.items()]
    else: print("Not found.")

def delete_entry(data):
    name = input("type your name: ").strip()
    if name in data:
        if input("Delete? (y/n): ").lower()=="y":
            del data[name]; print("Deleted.")
    else: print("Not found.")

def menu():
    init_vault()
    data, salt, key = load_vault()
    while True:
        print("\n1.Add  2.Get  3.List  4.Delete  5.Exit")
        ch = input("Choose any one of this: ").strip()
        if ch=="1": add_entry(data)
        elif ch=="2": show_entry(data)
        elif ch=="3": [print("-", k) for k in data]
        elif ch=="4": delete_entry(data)
        elif ch=="5":
            save_vault(data, salt, key)
            print("Saved your choice. GoodBye!"); break
        else: print("this is an invalid choice.")

if __name__ == "__main__":
    menu()