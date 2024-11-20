expenses = {}

def add_expense(category, amount):
    # searches for the category in expenses and adds the amount if category already exists
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    print(f"The {category} is now ${expenses[category]}")

def print_expense(category):
    if category in expenses:
        print(f"The {category} has ${expenses[category]}")

def display_expenses():
    for category, amount in expenses.items():
        print(f"{category} has ${amount}")

def print_items():
    for item in expenses.items():
        print(item)

add_expense("Investment", 10)
add_expense("Investment", 10)
add_expense("Investment", 10)
add_expense("Investment", 10)
add_expense("Retirement", 5)
add_expense("Retirement", 5)
add_expense("Retirement", 5)
add_expense("Retirement", 5)
add_expense("Retirement", 5)
