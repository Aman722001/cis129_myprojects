# Coffee Shop Simulator

# Prices of items
coffee_price = 5.00  # Price for one coffee
muffin_price = 4.00  # Price for one muffin
tax_rate = 0.06      # Sales tax rate of 6%

# Input: Asking user for the number of coffees and muffins they want to purchase
num_coffees = int(input("Number of coffees bought?\n"))  # Input for number of coffees
num_muffins = int(input("Number of muffins bought?\n"))  # Input for number of muffins

# Calculations for the cost of coffees, muffins, tax, and total
coffee_total = num_coffees * coffee_price      # Total cost of coffees
muffin_total = num_muffins * muffin_price      # Total cost of muffins
subtotal = coffee_total + muffin_total         # Subtotal (before tax)
tax = subtotal * tax_rate                      # Calculated tax (6% of subtotal)
total = subtotal + tax                         # Final total (subtotal + tax)

# Output: Display the formatted receipt
print("\n" + "*" * 39)  # Header line
print("My Coffee and Muffin Shop Receipt")     # Shop receipt title
print(str(num_coffees) + " Coffee at $" + format(coffee_price, ".2f") + " each: $" + format(coffee_total, ".2f"))  # Coffee cost breakdown
print(str(num_muffins) + " Muffins at $" + format(muffin_price, ".2f") + " each: $" + format(muffin_total, ".2f"))  # Muffin cost breakdown
print("6% tax: $" + format(tax, ".2f"))        # Display calculated tax
print("---------")                             # Divider line
print("Total: $" + format(total, ".2f"))       # Display total cost
print("*" * 39)                                # Footer line
