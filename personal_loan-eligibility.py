def main():
    age = int(input("Enter your age: "))
    if 18 <= age <= 65:
        income = int(input("Enter your annual income: "))
        employment_type = input("Are you employed part-time or full-time? ").lower()
        if employment_type == "part-time":
            years_of_employment = int(input("How many years have you been working part-time? "))
        else:
            years_of_employment = None
        if (employment_type == "full-time" and income >= 200000) or (employment_type == "part-time" and income >= 100000 and years_of_employment > 2):
            print("You are eligible for a loan.")
        else:
            print("You are not eligible for a loan.")
    else:
        print("You are not eligible for a loan.")

if __name__ == "__main__":
    main()

