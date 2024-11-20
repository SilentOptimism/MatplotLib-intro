expenses = {}

def create_loan(name, amount, interest):
    expenses[name]  = [amount, interest]

def print_loans():
    for name, amounts in expenses.items():
        print(f"{name} loan is ${amounts[0]} with an interest of {amounts[1]}%\n")

def make_payment(name, amount):
    if name in expenses:
        expenses[name][0] -= amount
    else:
        print(f"{name} is not a valid load?")
    
def applyInterestAll():
    for name, amounts in expenses.items():
        amounts[0] += amounts[0]*(amounts[1]/100)
        

create_loan("Car", 2000, 2.4)    
create_loan("House", 20000, 1.4)    
print_loans()

make_payment("Car", 500)
make_payment("House", 500)
print_loans()

applyInterestAll()
print_loans()