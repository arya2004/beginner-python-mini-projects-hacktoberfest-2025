
alpha_num_map = {
    'A': 42, 'B': 17, 'C': 50, 'D': 3, 'E': 26, 'F': 14, 'G': 10, 'H': 31,
    'I': 45, 'J': 8, 'K': 23, 'L': 47, 'M': 1, 'N': 4, 'O': 37, 'P': 11,
    'Q': 28, 'R': 49, 'S': 20, 'T': 40, 'U': 5, 'V': 36, 'W': 18, 'X': 35,
    'Y': 24, 'Z': 6, 'a': 13, 'b': 30, 'c': 9, 'd': 25, 'e': 19, 'f': 27,
    'g': 2, 'h': 43, 'i': 48, 'j': 16, 'k': 7, 'l': 34, 'm': 33, 'n': 46,
    'o': 21, 'p': 15, 'q': 41, 'r': 22, 's': 39, 't': 12, 'u': 32, 'v': 29,
    'w': 0, 'x': 38, 'y': 44, 'z': 51
}

num_alpha_map = {v: k for k, v in alpha_num_map.items()}

def encrypt(text, shift):
    encrypted_text = []             
    text = text.strip()
    shift = int(shift)     

    for char in text:
        if char in alpha_num_map:
            char_num = alpha_num_map[char]
            shifted_num = (char_num + shift) % 52
            new_char = num_alpha_map[shifted_num]
            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt(text, shift):
    shift = int(shift)
    return encrypt(text,-shift)

text = input("Enter the text that you want to encrypt: ")
key = input("Enter the key for encryption (You must securely share this key with the recipient): ")

encrypted_text = encrypt(text,key)

print("\nThe encrypted text is :")
print(f"{encrypted_text}\n")
decrypt_key = input("To decrypt this message, you must enter the key: ")
decrypted_text = decrypt(encrypted_text, decrypt_key)

print("Decrypted text:")
print(decrypted_text)
print("You will be able to read this only if the keys match.")