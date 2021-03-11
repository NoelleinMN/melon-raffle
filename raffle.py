"""Read customer data from file and run a raffle."""

import random       # previously had only imported choice from random


class Customer(object):     # creates class "Customer" with attributes outlined below
    """A customer at Ubermelon.""" 

    def __init__(self, name, email, street, city, zipcode):
        self.name = name
        self.email = email
        self.street = street
        self.city = city
        self.zipcode = zipcode


def get_customers_from_file(customer_file_path):        # pass in the file path through the function
    """Read customer file and return list of customer objects.

    Read file at customer_file_path and create a customer object
    containing customer information.
    """

    customers = []                                      # create empty list

    customer_file = open(customer_file_path)            # open file an assign to variable "customer_file"

    # Process a file like:
    #
    #   customer-name | email | street | city | zipcode

    for line in customer_file:                          # for loop to iterate over each line in file
        customer_data = line.strip().split("|")         # assign variable to the list created after trailing whitespace is stripped and line is split on |
        name, email, street, city, zipcode = customer_data  # list unpacking

        new_customer = Customer(name, email, street, city, zipcode) # each new customer and attributes added to the class Customers
        customers.append(new_customer)                  # append to the empty list every customer and their attributes

    return customers                                    # returns list customers


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