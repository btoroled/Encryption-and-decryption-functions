alphabet = "abcdefghijklmnopqrstuvwxyz"

def vignere_decryption(message, keyword):
    keyword_phrase = ""
    keyword_index = 0

    for character in message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if character in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += character

    decoded_message = ""

    for i in range(len(message)):
        if message[i] in alphabet:
            old_character_index = alphabet.find(message[i])
            offset_index = alphabet.find(keyword_phrase[i])
            new_character = alphabet[(old_character_index - offset_index) % 26]
            decoded_message += new_character
        else:
            decoded_message += message[i]
    return decoded_message

def vignere_encryption(message, keyword):
    keyword_phrase = ""
    keyword_index = 0

    for character in message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if character in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += character

    decoded_message = ""

    for i in range(len(message)):
        if message[i] in alphabet:
            old_character_index = alphabet.find(message[i])
            offset_index = alphabet.find(keyword_phrase[i])
            new_character = alphabet[(old_character_index + offset_index) % 26]
            decoded_message += new_character
        else:
            decoded_message += message[i]
    return decoded_message           

#Vignere Cipher #
print()
print("***VIGNERE CIPHER***")
print()

print("Do you want to encrypt or decrypt?")
user_input = input('e/d: ').lower()

if user_input == 'e': 
    print("ENCRYPTION MODE SELECTED")
    print()
    keyword = str(input('Enter the keyword for encryption: '))
    text = input('Enter the text to encrypt: ')
    ciphertext = (vignere_encryption(text, keyword))
    print(f"Encrypted message: {ciphertext}")

elif user_input == 'd':
    print("DECRYPTION MODE SELECTED")
    print()
    keyword = str(input('Enter the keyword for decryption: '))
    text = input('Enter the text to Decrypt: ')
    ciphertext = (vignere_decryption(text, keyword))
    print(f"Decrypted message: {ciphertext}")
else: 
    print("Invalid input!")
