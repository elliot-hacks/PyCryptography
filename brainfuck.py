import argparse

def brainfuck_encrypter(text):
    brainfuck_code = ""
    memory = [0] * 30000
    pointer = 0

    for char in text:
        code_point = ord(char)
        while memory[pointer] != code_point:
            if memory[pointer] < code_point:
                brainfuck_code += "+"
                memory[pointer] += 1
            else:
                brainfuck_code += "-"
                memory[pointer] -= 1
        brainfuck_code += "."

    return brainfuck_code


def brainfuck_decrypter(code):
    memory = [0] * 30000
    pointer = 0
    output = ''

    loop_stack = []
    loop_map = {}

    i = 0
    while i < len(code):
        char = code[i]

        if char == '>':
            pointer += 1
        elif char == '<':
            pointer -= 1
        elif char == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif char == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif char == '.':
            output += chr(memory[pointer])
        elif char == '[':
            if memory[pointer] == 0:
                loop_depth = 1
                while loop_depth > 0:
                    i += 1
                    if code[i] == '[':
                        loop_depth += 1
                    elif code[i] == ']':
                        loop_depth -= 1
            else:
                loop_stack.append(i)
        elif char == ']':
            if memory[pointer] != 0:
                i = loop_stack[-1] - 1
            else:
                loop_stack.pop()

        i += 1

    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brainfuck Encoder/Decoder")
    parser.add_argument("-e", "--encode", help="Encode plaintext to Brainfuck code")
    parser.add_argument("-d", "--decode", help="Decode Brainfuck code to plaintext")

    args = parser.parse_args()

    if args.encode:
        plaintext = args.encode
        encrypted_code = brainfuck_encrypter(plaintext)
        print("Encrypted Brainfuck Code:")
        print(encrypted_code)

    elif args.decode:
        brainfuck_code = args.decode
        decrypted_text = brainfuck_decrypter(brainfuck_code)
        print("Decrypted Plaintext:")
        print(decrypted_text)

    else:
        print("Please provide either -e for encoding or -d for decoding.")
