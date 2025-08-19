def main():
    purchase_amount = float(input("Enter the total purchase amount: "))
    discount = 0.1 if purchase_amount > 2000 else 0
    final_price = purchase_amount - (discount * purchase_amount)
    print(f"Final price after discount = {final_price}")

if __name__ == "__main__":
    main()

