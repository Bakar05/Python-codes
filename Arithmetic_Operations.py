def arithmetic_operations():
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    c = float(input("Enter value for c: "))
    d = float(input("Enter value for d: "))
    e = float(input("Enter value for e: "))
    f = float(input("Enter value for f: "))

    sum_result = a + b + c + d + e + f
    subtract_result = a - b - c - d - e - f
    multiply_result = a * b * c * d * e * f
    try:
        divide_result = a / b / c / d / e / f
    except ZeroDivisionError:
        divide_result = "Error: Division by zero is not allowed"
    modulus_result = int(sum_result) % 50

    print("\n--- Arithmetic Results ---")
    print(f"Sum = {sum_result}")
    print(f"Subtraction = {subtract_result}")
    print(f"Multiplication = {multiply_result}")
    print(f"Division = {divide_result}")
    print(f"Modulus with 50 = {modulus_result}")

if __name__ == "__main__":
    arithmetic_operations()

