def main():
    score = int(input("Enter your score: "))
    if score >= 90:
        print("Excellent work!")
    elif score >= 70:
        print("Good job, but there's room for improvement.")
    else:
        print("You need to work harder.")

if __name__ == "__main__":
    main()
