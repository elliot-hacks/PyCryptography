# PyCryptography
A personal project for offline cryptography tools


To do list:
1. **Caesar Cipher**: A simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

   ***usage***:
   consider rot13 encryption:
   ┌──(hombresito㉿dope)-[~/Desktop/Python/Cryptography]
   └─$ python caesar.py -e -k 13 -m "Elliot hacks" 
    Encrypted Message:
    RYYVBG UNPXF
                                                                                                                                
    ┌──(hombresito㉿dope)-[~/Desktop/Python/Cryptography]
    └─$ python caesar.py -d -k 13 -m "RYYVBG UNPXF"
    Decrypted Message:
    ELLIOT HACKS

3. **Vigenère Cipher**: A more advanced substitution cipher that uses a keyword to determine the shifting amount for each letter.

4. **Transposition Cipher**: Involves rearranging the letters in the plaintext to form the ciphertext.

5. **Substitution Cipher**: Involves replacing each letter in the plaintext with a corresponding letter or symbol in the ciphertext.

6. **RSA Encryption**: A public-key cryptosystem that involves generating a public and private key pair for secure communication.

7. **AES Encryption**: A symmetric-key encryption algorithm used to secure sensitive data.

8. **Hill Cipher**: A polygraphic substitution cipher that uses linear algebra for encryption and decryption.

9. **Diffie-Hellman Key Exchange**: A method for two parties to agree on a shared secret key over an unsecured communication channel.

10. **SHA-256 Hashing**: A cryptographic hash function that produces a fixed-size output (256 bits) from an input.

11. **Simple XOR Encryption**: An XOR-based encryption method that involves bitwise operations.

12. **One-Time Pad**: A theoretically unbreakable encryption method that uses a random key as long as the message.

13. **Playfair Cipher**: A digraphic substitution cipher using a 5x5 matrix of letters.

14. **Rail Fence Cipher**: A transposition cipher that rearranges the letters in a zigzag pattern.

15. **Autokey Cipher**: A substitution cipher that uses the plaintext itself to generate part of the key for encryption.

16. **Columnar Transposition Cipher**: A transposition cipher where the columns are rearranged based on a keyword.
