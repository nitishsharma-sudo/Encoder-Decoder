def generate_vigenere_table():
    """
    Generates the Vigenère table (Vigenère square).
    """
    table = []
    for i in range(26):
        table.append([])
        for j in range(26):
            table[i].append(chr(((i + j) % 26) + ord('A')))
    return table

def vigenere_encrypt(plaintext, key):
    """
    Encrypts plaintext using the Vigenère cipher with the given key.
    """
    plaintext = plaintext.upper()
    key = key.upper()
    encrypted_text = ''
    table = generate_vigenere_table()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            key_char = key[key_index]
            key_index = (key_index + 1) % len(key)
            row = ord(key_char) - ord('A')
            col = ord(char) - ord('A')
            encrypted_text += table[row][col]
        else:
            encrypted_text += char

    return encrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")
    encrypted_text = vigenere_encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()