def current_stock_quantities(apples, bananas, oranges):
    apples -= 10
    bananas -= 5
    oranges -= 8
    print("\n--- Updated Stock ---")
    print(f"Apples : {apples}")
    print(f"Bananas : {bananas}")
    print(f"Oranges : {oranges}")
    return apples, bananas, oranges

def main():
    apples = int(input("Enter apples in stock: "))
    bananas = int(input("Enter bananas in stock: "))
    oranges = int(input("Enter oranges in stock: "))
    apples, bananas, oranges = current_stock_quantities(apples, bananas, oranges)

if __name__ == "__main__":
    main()
