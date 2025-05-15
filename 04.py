# 4. Class Variables and Class Methods

# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank():
    bank_name = "Alfalah Bank"

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_details(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")        
        
cust1 = Bank("Rimsha")   
cust2 = Bank("Zubair")   

cust1.show_details()
cust2.show_details()

#  change bank name
Bank.change_bank_name("New Horizon Bank")

cust1.show_details()
cust2.show_details()