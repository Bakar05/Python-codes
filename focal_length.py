def main():
    p = float(input("Enter the distance of object from the lens (P): "))
    q = float(input("Enter the distance of image from the lens (Q): "))
    if p == 0 or q == 0:
        print("Neither P nor Q can be zero.")
    else:
        focal_length = 1 / ((1 / p) + (1 / q))
        print(f"Focal Length = {focal_length}")

if __name__ == "__main__":
    main()
