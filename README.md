# PyCryptography
## A personal project for offline cryptography tools


## To do list:
1. ### Caesar Cipher : A simple su tution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

### usage :
 #### encryption
    >>> python caesar.py -e -k 13 -m "Elliot hacks"
    Encrypted Message:
    RYYVBG UNPXF                                                                                                                            
 #### decryption   
    >>> python caesar.py -d -k 13 -m "RYYVBG UNPXF"
    Decrypted Message:
    ELLIOT HACKS


3. ### Brainfuck: Brainfuck is a minimalist and esoteric programming language created by Urban Müller in 1993.
### usage :
 #### decryption
    >>>python brainfuck.py -d "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>-.>++++++++..---.++++++.+++++.<<++.>+++.>-------------------.++.++++++++.++++++++."
    Decrypted Plaintext:
    Elliot Hacks


4. ### Reverse cipher: Rearranges statements in reverse order
### usage :
    >>>python reverse.py "Hello friend"
    Reversed Message:
    dneirf olleH


5. ### Vigenère Cipher : A more advanced substitution cipher that uses a keyword to determine the shifting amount for each letter.

6. ### Transposition cipher : Involves re nging the letters in the plaintext to form the ciphertext.

7. ### Substitution  cipherer : Involves re ing each letter in the plaintext with a corresponding letter or symbol in the ciphertext.

8. ### RSA Encryption  : A public-ke yptosystem that involves generating a public and private key pair for secure communication.

9. ### AES Encryption  : A symmetric  encryption algorithm used to secure sensitive data.

10. ### Hill Cipher A polygraph ubstitution cipher that uses linear algebra for encryption and decryption.

11. ### Diffie-Hellma y Exchange : A method fo o parties to agree on a shared secret key over an unsecured communication channel.

12. ### SHA-256 Hashing : A cryptogra  hash function that produces a fixed-size output (256 bits) from an input.

13. ### Simple XOR Encryption : An XOR-base cryption method that involves bitwise operations.

14. ### One-Time Pad:  A theoretic  unbreakable encryption method that uses a random key as long as the message.

15. ### Playfair Cipher : A digraphic stitution cipher using a 5x5 matrix of letters.

16. ### Rail Fence Cipher: A transposi  cipher that rearranges the letters in a zigzag pattern.

17. ### Autokey Cipher : A substitut cipher that uses the plaintext itself to generate part of the key for encryption.

18. ### Columnar Transposition Cipher : A transposition cipher where the columns are rearranged based on a keyword.
