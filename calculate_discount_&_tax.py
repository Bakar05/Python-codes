def calculate_total(subtotal, discount_rate):
    discounted_amount = subtotal * (discount_rate / 100)
    discounted_total = subtotal - discounted_amount
    tax_rate = 16.0
    tax = discounted_total * (tax_rate / 100)
    return discounted_total + tax

def main():
    subtotal = float(input("Enter the subtotal of the items in the cart: "))
    discount_rate = float(input("Enter the discount rate (as a percentage): "))
    total_cost = calculate_total(subtotal, discount_rate)
    print(f"The total cost after applying the discount and adding 16% tax is: {total_cost} rupees.")

if __name__ == "__main__":
    main()
