
# Declare a Person class with the following attributes:
# id, first name, last name

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "Customer Information: " + self.id + self.first_name + self.last_name


# Declare an Account class with the following attributes:
# number, type, owner, balance

class Account:
    def __init__(self, number, type, owner, balance):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account Information: " + self.number + self.type + self.owner + self.balance

# Declare a Bank class able to support the following operations:
# Adding a customer to the bank
# Adding an account to the bank
# Removing an account from the bank
# Depositing money into an account
# Withdrawing money from an account
# Balance inquiry for a particular account
# From an interactive terminal, you should be able to import these classes an interact with the objects and methods defined above.


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    # Constraint:
    # When attempting to register a customer, the customer id must be unique.
    def add_customer(self, customer):
        if customer.id not in self.customers:
            self.customers[customer.id] = [customer.first_name, customer.last_name]
            print("Customer added: " + customer.id + customer.first_name + customer.last_name)
        else:
            print("Customer ID already exists")

    # Constraint:
    # When attempting to add an account, the user associated with said account must already registered as a customer.
    # When attempting to add an account, the account number must be unique.
    def add_account(self, account):
        if account.number not in self.accounts.keys() and account.owner in self.customers.keys():
            self.accounts[account.number] = [account.type, account.owner, account.balance]
            print("Account added: " + account.number + account.type + account.owner + account.balance)
        else:
            print("Account ID already exists or customer does not exist")


    def remove_account(self, account):
        if account in self.accounts.keys():
            del self.accounts[account.number]
        else:
            print("Account ID does not exist")

    def deposit_money(self, account, amount):
        if account in self.accounts.keys():
            self.accounts[account][3] += amount
            print('{:.2f}'.format(amount) + ' was deposited into Account ' + str(account))
        else:
            print("Account ID does not exist.")

    def withdraw_money(self, account, amount):
        if account in self.accounts.keys():
            self.accounts[account][3] -= amount
            print('{:.2f}'.format(amount) + ' was withdrawn from Account ' + str(account))
        else:
            print("Account ID does not exist.")

    def balance_inquiry(self, account):
        if account in self.accounts.keys():
            print("Account number " + str(account) + " has a balance of " + '{:.2f}'.format(self.accounts[account][3]))
        else:
            print("Account ID does not exist.")