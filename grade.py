def calculate_grade(exam_score, project_score, attendance_score):
    return (exam_score * 0.5) + (project_score * 0.3) + (attendance_score * 0.2)

def main():
    exam_score = float(input("Enter the exam score (out of 100): "))
    project_score = float(input("Enter project score (out of 100): "))
    attendance_score = float(input("Enter attendance score (out of 100): "))

    final_grade = calculate_grade(exam_score, project_score, attendance_score)
    print(f"Final grade of the student is: {final_grade}")

if __name__ == "__main__":
    main()

