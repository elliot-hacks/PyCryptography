import argparse

def reverse_message(message):
    return message[::-1]

def main():
    parser = argparse.ArgumentParser(description="Reverse Message")
    parser.add_argument("message", type=str, help="Message to reverse")

    args = parser.parse_args()

    reversed_message = reverse_message(args.message)
    print("Reversed Message:")
    print(reversed_message)

if __name__ == "__main__":
    main()
