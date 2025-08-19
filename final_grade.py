def main():
    initial_grade = float(input("Enter the student's initial grade (0-100): "))
    participated = input("Did the student participate in extra-curricular activities? (yes/no): ").lower()
    final_grade = min(initial_grade * 1.05 if participated == "yes" else initial_grade, 100)
    print(f"The student's final grade, after considering extra-curricular activities, is: {final_grade}")

if __name__ == "__main__":
    main()
