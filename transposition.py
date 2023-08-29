import pyperclip
import argparse

def encrypt(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)

def main():
    parser = argparse.ArgumentParser(description="Transposition Cipher Encryptor")
    parser.add_argument("-m", "--message", required=True, help="Message to encrypt")
    parser.add_argument("-k", "--key", type=int, required=True, help="Encryption key")

    args = parser.parse_args()
    
    myMessage = args.message
    myKey = args.key

    ciphertext = encrypt(myKey, myMessage)
    print(ciphertext + '|')
    pyperclip.copy(ciphertext)

if __name__ == '__main__':
    main()
