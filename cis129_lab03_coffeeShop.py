# Coffee Shop Simulator

# Prices of items
coffee_price = 5.00      # Price for one coffee
muffin_price = 4.00      # Price for one muffin
croissant_price = 3.50   # Price for one croissant
lemonade_price = 2.50    # Price for one lemonade
mug_price = 10.00        # Price for one coffee mug
tax_rate = 0.06          # Sales tax rate of 6%

# Input: Asking user for the number of items they want to purchase
num_coffees = int(input("Number of coffees bought?\n"))
num_muffins = int(input("Number of muffins bought?\n"))
num_croissants = int(input("Number of croissants bought?\n"))
num_lemonades = int(input("Number of lemonades bought?\n"))
num_mugs = int(input("Number of coffee mugs bought?\n"))

# Calculations for the cost of all items, tax, and total
coffee_total = num_coffees * coffee_price          # Total cost of coffees
muffin_total = num_muffins * muffin_price          # Total cost of muffins
croissant_total = num_croissants * croissant_price # Total cost of croissants
lemonade_total = num_lemonades * lemonade_price    # Total cost of lemonades
mug_total = num_mugs * mug_price                   # Total cost of mugs

# Calculate the subtotal, tax, and total
subtotal = (coffee_total + muffin_total + croissant_total + lemonade_total + mug_total)
tax = subtotal * tax_rate
total = subtotal + tax

# Output: Display the formatted receipt
print("\n" + "*" * 39)  # Header line
print("Welcome to My Coffee Shop Receipt")     # Shop receipt title
print(str(num_coffees) + " Coffee at $" + format(coffee_price, ".2f") + " each: $" + format(coffee_total, ".2f"))
print(str(num_muffins) + " Muffins at $" + format(muffin_price, ".2f") + " each: $" + format(muffin_total, ".2f"))
print(str(num_croissants) + " Croissants at $" + format(croissant_price, ".2f") + " each: $" + format(croissant_total, ".2f"))
print(str(num_lemonades) + " Lemonades at $" + format(lemonade_price, ".2f") + " each: $" + format(lemonade_total, ".2f"))
print(str(num_mugs) + " Coffee Mugs at $" + format(mug_price, ".2f") + " each: $" + format(mug_total, ".2f"))
print("6% tax: $" + format(tax, ".2f"))        # Display calculated tax
print("---------")                             # Divider line
print("Total: $" + format(total, ".2f"))       # Display total cost
print("*" * 39)                                # Footer line

# Thank-you message to the customer
print("\nThank you for visiting My Coffee Shop! We hope to see you again soon.")
