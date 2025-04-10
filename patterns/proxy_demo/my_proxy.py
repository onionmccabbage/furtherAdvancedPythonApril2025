# proxy lets us call one item which ends up calling another item
# e.g. a server calls an API and returns the results
from bank import Bank
from customer import Customer
def main():
    customer = Customer()
    customer.makePayment()

# anything with pre- and post- double undescore is a part of Python
# known as 'dunder'
if __name__ == '__main__':
    for user in range(0,100):
        main()