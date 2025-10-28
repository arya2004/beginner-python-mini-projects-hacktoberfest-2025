### Custom Rotational Cipher CLI Tool 🔐
A unique command-line tool written in Python that implements a custom rotational cipher for text encryption and decryption. This cipher operates on a predefined mapping of 52 characters (26 uppercase, 26 lowercase) to specific numerical indices, rather than relying on standard ASCII values.

### 💡 How It Works
- The cipher uses a fixed, custom dictionary to map each letter to a number between 0 and 51.

- Encryption: When encrypting, the program looks up the numerical index of each character, adds the user-provided shift key, and applies the modulus operator (% 52) to ensure the new index wraps correctly within the 0-51 range. It then converts this new index back to a character using a reverse map.

- Decryption: Decryption is handled by simply calling the same encryption function but passing the negative of the original shift key. This elegantly reverses the operation.

- Non-alphabetic characters (spaces, punctuation, numbers) are left unchanged.

### 🚀 Getting Started
- Prerequisites
This project uses only core Python functionality and does not require any external libraries.

Python 3.x

- How to Run
Save the provided code into a file named, for example, cipher_tool.py.
Open your terminal or command prompt.
Execute the script:

python Caesar.py