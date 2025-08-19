def arithmetic_operations():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    print(f"Addition = {a + b + c}")
    print(f"Subtraction = {a - b - c}")
    print(f"Multiplication = {a * b * c}")

    if b != 0 and c != 0:
        print(f"Division = {a / b / c}")
    else:
        print("Division by zero is not allowed.")

if __name__ == "__main__":
    arithmetic_operations()
