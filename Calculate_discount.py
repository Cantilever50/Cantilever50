

# Step 1: Define the function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Step 2: Prompt the user for the original price and discount percentage
# use float instead of int to allow for collection of decimal values..


price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 3: Call the function and print the final price
final_price = calculate_discount(price, discount_percent)

# Step 4: Print the result
if final_price == price:
    print(f"No discount applied. The original price is: ₦{final_price:.2f}")
else:
    print(f"The final price after applying the discount is: ₦{final_price:.2f}")
