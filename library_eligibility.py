def main():
    age = int(input("Enter your age: "))
    availability = int(input("Is the book available? (1 = Yes, 0 = No): "))
    if age >= 18 and availability == 1:
        print("You are eligible to take a loan.")
    else:
        print("You are not eligible to take a loan.")
        if availability != 1:
            print("The book must be available.")

if __name__ == "__main__":
    main()
