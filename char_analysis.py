def is_vowel(ch):
    return ch.lower() in 'aeiou'

def is_digit(ch):
    return ch.isdigit()

def main():
    while True:
        character = input("Enter a character: ")
        if len(character) != 1:
            print("Please enter a single character.")
            continue
        if is_vowel(character):
            print(f"{character} is a vowel.")
        elif is_digit(character):
            print(f"{character} is a digit.")
        else:
            print(f"{character} is neither a vowel nor a digit.")
        choice = input("Select an option: \n1. Start the program\n2. Exit\n")
        if choice != '1':
            break

if __name__ == "__main__":
    main()
