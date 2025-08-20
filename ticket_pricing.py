def main():
    age = int(input("Enter your age: "))
    time = int(input("Enter the time of the movie (24-hour format): "))
    price = 0
    if age <= 12:
        price = 5
    elif 13 <= age <= 65:
        price = 10 if time < 18 else 12
    else:
        price = 8
    print(f"The ticket price is rupees {price}.")

if __name__ == "__main__":
    main()

