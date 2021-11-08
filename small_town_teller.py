
#Declare a Person class with the following attributes:
#id, first name, last name

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "Customer Information: {self.id} {self.first_name} {self.last_name}


#Declare an Account class with the following attributes:
#number, type, owner, balance

class Account:
    def __init__(self, number, type, owner, balance):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account Information: {self.number} {self.type} {self.owner} {self.balance}"

#Declare a Bank class able to support the following operations:
#Adding a customer to the bank
#Adding an account to the bank
#Removing an account from the bank
#Depositing money into an account
#Withdrawing money from an account
#Balance inquiry for a particular account
#From an interactive terminal, you should be able to import these classes an interact with the objects and methods defined above.

class Bank:

    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self):

    def add_account(self):

    def remove_account(self):

    def deposit_money(self):

    def withdraw_money(self):

    def balance_inquiry(self):




