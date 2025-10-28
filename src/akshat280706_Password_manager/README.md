#TinyVault – Local Password Manager

A lightweight **local password manager** built in Python, using 
strong encryption to securely store credentials.

## Features
- Master password–protected vault
- AES encryption using `cryptography.Fernet`
- Add, view, list, and delete password entries
- Auto password generator (16 characters)
- Fully menu-driven console interface

## How It Works
- The vault file is stored locally as `.tiny_vault.bin` in the home directory.
- Your master password derives a 256-bit encryption key using PBKDF2-HMAC-SHA256.
- All data is encrypted with that key and stored securely.




