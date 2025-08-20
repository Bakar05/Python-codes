import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    circumference = circle_circumference(radius)
    print(f"Area of the Circle = {area}")
    print(f"Circumference of the Circle = {circumference}")

if __name__ == "__main__":
    main()

