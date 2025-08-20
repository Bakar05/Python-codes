import math

def quadratic_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("The roots are real and distinct.")
        print(f"Root 1 = {root1}")
        print(f"Root 2 = {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print("The roots are real and equal.")
        print(f"Root = {root}")
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-discriminant) / (2 * a)
        print("The roots are complex.")
        print(f"Root 1 = {real_part} + {imag_part}i")
        print(f"Root 2 = {real_part} - {imag_part}i")

def main():
    a = float(input("Enter coefficient a of the quadratic equation (ax^2 + bx + c = 0): "))
    b = float(input("Enter coefficient b of the quadratic equation (ax^2 + bx + c = 0): "))
    c = float(input("Enter coefficient c of the quadratic equation (ax^2 + bx + c = 0): "))
    quadratic_roots(a, b, c)

if __name__ == "__main__":
    main()
