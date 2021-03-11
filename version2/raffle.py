"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries

import random

from customers import get_customers_from_file           # imports function from other file customers

def pick_winner(customers):                             # function recalls return customers from other function(s)
    """Choose a random winner from list of customers."""

    chosen_customer = random.choice(customers)          # random choice assigned to variable chosen_customer
    
    name = chosen_customer.name                         # uses Class to pull name and email attribute from chosen_customer object
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")


def run_raffle():
    """Run the weekly raffle."""


    customers = get_customers_from_file("customers.txt")    # nested function to recall return customers
    pick_winner(customers)                                  # nested function to choose and print winner

# customer_file_path = 'customers.txt'

if __name__ == "__main__":                                  # NEED TO UNDERSTAND BETTER
    run_raffle()