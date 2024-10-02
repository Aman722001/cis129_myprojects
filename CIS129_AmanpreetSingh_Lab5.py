# Lab 5 The Bottle Return Program
# Name: Amanpreet Singh
# Date: October 1st, 2024
# Description: This program calculates the total number of bottles returned
# for seven days and the total payout. The user can continue to enter data for multiple weeks.

# Step 1: Declare variables
def main():
    keep_going = 'y'

    # Step 2: Loop to run program again
    while keep_going.lower() == 'y':
        total_bottles = 0
        counter = 1
        payout_per_bottle = 0.10

        # Step 4: Loop through 7 days
        for day in range(1, 8):
            today_bottles = int(input(f"Enter number of bottles returned for day #{day}: "))
            total_bottles += today_bottles  # Accumulate the total bottles

        # Step 5: Calculate the total payout
        total_payout = total_bottles * payout_per_bottle

        # Step 6: Output results
        print(f"\nThe total number of bottles collected is {total_bottles}")
        print(f"The total paid out is $ {total_payout:.2f}")

        # Ask the user if they want to enter another week's worth of data
        keep_going = input("Do you want to enter another week's worth of data? (Enter y or n): ")

# Call the main function
main()
