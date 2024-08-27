# Encryption and Decryption Library
This repository contains Python implementations of two classical cryptographic algorithms: the Caesar cipher and the Vigenère cipher. Each file includes both encryption and decryption functions for the respective cipher.

Table of Contents
Introduction
Installation
Usage
Caesar Cipher
Vigenère Cipher
License
Introduction
Caesar Cipher
The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted by a fixed number of positions down or up the alphabet. For example, with a shift of 3, A becomes D, B becomes E, and so on. This method is simple but vulnerable to frequency analysis attacks.

Vigenère Cipher
The Vigenère cipher is a more complex substitution cipher that uses a keyword to shift the positions of letters in the plaintext. Each letter in the keyword shifts the corresponding letter in the plaintext by a different amount, making it more secure than the Caesar cipher.

Installation
Clone this repository to your local machine using:

Copiar código

git clone https://github.com/yourusername/encryption-decryption-library.git

cd encryption-decryption-library

No additional dependencies are required.

Usage
Caesar Cipher
The Caesar cipher implementation can be found in Caesar_cypher.py. You can use this script to encrypt or decrypt a message with a specified shift.


Vigenère Cipher
The Vigenère cipher implementation is available in Vignere_cypher.py. This script allows you to encrypt or decrypt a message using a keyword.


This project is licensed under the MIT License. See the LICENSE file for details.
