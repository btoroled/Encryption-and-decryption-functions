
characters = "abcdefghijklmnopqrstuvwxyz"
num_characters = len(characters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext: 
        letter = letter.lower()
        if not letter == '':
            index = characters.find(letter)
            if index == -1: 
                ciphertext += letter
            else:
                new_index = index - (key)
                if new_index < 0: 
                    new_index += 26
                ciphertext += characters[new_index]
    return ciphertext

def decrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext: 
        letter = letter.lower()
        if not letter == '':
            index = characters.find(letter)
            if index == -1: 
                ciphertext += letter
            else:
                new_index = index + (key)
                if new_index >= 26: 
                    new_index -= 26
                ciphertext += characters[new_index]
    return ciphertext

def bulk_decrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == '':
            index = characters.find(letter)
            if index == -1:
                    ciphertext += letter
            else:
                new_index = index + (key)
                if new_index >= 26: 
                    new_index -= 26
                ciphertext += characters[new_index]

    return ciphertext
 
print()
print("***Ceaser Cipher***".upper)
print()

print("Do you want to encrypt or decrypt?")
user_input = input('e/d/bd: ').lower()

if user_input == 'e': 
    print("ENCRYPTION MODE SELECTED")
    print()
    key = int(input('Enter the key 1 to 26: '))
    text = input('Enter the texto to encrypt: ')
    ciphertext = (encrypt(text, key))
    print(f"Encrypted message: {ciphertext}")

elif user_input == 'd':
    print("DECRYPTION MODE SELECTED")
    print()
    key = int(input('Enter the key 1 to 26: '))
    text = input('Enter the text to Decryption: ')
    ciphertext = (decrypt(text, key))
    print(f"Decrypted message: {ciphertext}")

#bulk_decryption
elif user_input == 'bd':
    print("Bulk DECRYPTION MODE SELECTED")
    print()
    text = input('Enter the text to decrypt : ')
    key = 0
    while key < 25:
        ciphertext = (bulk_decrypt(text, key))
        print(f"Bulk decription messages: {ciphertext}")
        print()
        key += 1
else: 
    print("Invalid input!")