import json
from datetime import datetime

expense_file = "expense.json"
def load_expenses():
    try:
        with open(expense_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File Not Found")
        return []
    except json.JSONDecodeError:
        print("File is empty! Add Data First To View list")
        return []

expenses = load_expenses()


def save_expenses(expenses):
    with open(expense_file, "w") as file:
        json.dump(expenses, file)

def show(expenses):
    if not expenses:
        print("No Expenses Present")
    else:
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense['expense_name']} -  ₹{expense['amount']} - {expense['category']} - {expense['date']}")

def add_expense(expenses):
    try:
        expense_name = input("Enter expence name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = datetime.now()
        formatted_date = date.strftime("%d/%m/%Y")
        expense_data = {
            "expense_name": expense_name,
            "amount": amount,
            "category": category,
            "description": description,
            "date" : formatted_date
        }
        expenses.append(expense_data)
        save_expenses(expenses)
        print("Expense added successfully")
    except ValueError:
        print("Enter valid number")
    
def total_expense(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"Total expense: {total}")

def filter_category(expenses):
    category = input("Enter Category: ")
    category_total_amount = 0
    found = False
    print(f"{category} expense: \n")
    for expense in expenses:
        if expense['category'] == category :
            print(f"{expense['expense_name']} - {expense['amount']} \n")
            category_total_amount += expense['amount']
            found = True
        
    if not found:
        print("No Category Found")
    else:
        print(f"Total Amount: {category_total_amount}")

def expense_summary(expenses):
    summary = {}
    for expense in expenses:
        if expense['category'] not in summary:
            summary[expense['category']] = expense['amount']
        else:
            summary[expense['category']] += expense['amount']
    total_category_amount = 0
    print("========== EXPENSE SUMMARY ==========")
    for key, value in summary.items():
        print(f"{key} -> {value}")
        total_category_amount += value
    print("----------------------------")
    print(f"Total  -> {total_category_amount}")

def delete_expense(expenses):
    try:    
        show(expenses)
        print("This is the expense list")
        delete_expense_number = int(input("Enter expense number : "))
        task_length = len(expenses)
        if(delete_expense_number <= task_length and delete_expense_number > 0):
            expenses.pop(delete_expense_number-1)
            save_expenses(expenses)
            print("Expense deleted successfully")
        else:
            print("Entered number is not the expense list")
    except ValueError:
        print("Enter valid number")

def update_expense(expenses):
    try:
        show(expenses)
        print("This is the expense list")
        update_expense_number = int(input("Enter expense number which you want to update : "))
        task_length = len(expenses)
        if(update_expense_number <= task_length and update_expense_number > 0):
            expense_name = input("Enter expence name: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")

            expenses[update_expense_number-1]["expense_name"] = expense_name
            expenses[update_expense_number-1]["amount"] = amount
            expenses[update_expense_number-1]["category"] = category
            expenses[update_expense_number-1]["description"] = description

            save_expenses(expenses)
            print("Expese data updated")
        else:
            print("Entered number is not the expense list")
    except ValueError:
        print("Enter valid number")
while True:
    try:
        choice = int(input("""
    ========== EXPENSE TRACKER ==========
1. View Expenses
2. Add Expense
3. Calculate Total
4. Category Expenses
5. Expense Summary
6. Delete Expense
7. Update Expense
9. Exits
Enter your choice: """))
        if(choice == 1):
            show(expenses)
        elif(choice == 2):
            add_expense(expenses)
        elif(choice == 3):
            total_expense(expenses)
        elif(choice == 4):
            filter_category(expenses)
        elif(choice == 5):
            expense_summary(expenses)
        elif(choice == 6):
            delete_expense(expenses)
        elif(choice == 7):
            update_expense(expenses)
        elif(choice == 9):
            break
        else:
            print("invalid input")
    except ValueError:
        print("Invalid Input")