import argparse
import pyperclip

def caesarCipher(message, key, mode):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    message = message.upper()

    for letter in message:
        if letter in LETTERS:
            num = LETTERS.find(letter)
            if mode == 'encrypt':
                num += key
            elif mode == 'decrypt':
                num -= key
            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)
            translated += LETTERS[num]
        else:
            translated += letter
    return translated

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Encryptor/Decryptor")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the message")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the message")
    parser.add_argument("-k", "--key", type=int, help="Encryption/Decryption key")
    parser.add_argument("-m", "--message", type=str, help="Message to encrypt/decrypt")

    args = parser.parse_args()

    if args.encrypt:
        if args.key is None or args.message is None:
            print("Both key and message are required for encryption.")
            return
        result = caesarCipher(args.message, args.key, 'encrypt')
        print("Encrypted Message:")
        print(result)
        pyperclip.copy(result)

    elif args.decrypt:
        if args.key is None or args.message is None:
            print("Both key and message are required for decryption.")
            return
        result = caesarCipher(args.message, args.key, 'decrypt')
        print("Decrypted Message:")
        print(result)
        pyperclip.copy(result)

    else:
        print("Please provide either -e for encryption or -d for decryption.")

if __name__ == "__main__":
    main()
