class BudgetCategory:
    # Constructor and private attributes
    def __init__(self, category_name, allocated_budget=0):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = 0

    # Getters for category name and budget
    def get_category_name(self):
        return self.__category_name
    
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Method to add an expense to the category
    # Making the add_expense method, the amount is checked and adjusted using a if/elif/else statement. The first part checks if the balance is less than equal to 0. 
    # Elif checks the expense against the budget. If there's not enough to cover the expense, an error message is printed. The method's else statement will add the expense to the amount.
    def add_expense(self, amount):
        if amount <= 0:
            print("Expense must be a positive number.")
        elif amount > self.__allocated_budget - self.__expenses:
            print("Insufficient budget for this expense.")
        else:
            self.__expenses += amount

    # Method to display the budget category details
    def display_category_summary(self):
        remaining_budget = self.__allocated_budget - self.__expenses
        print(f"Budget Category: {self.get_category_name()}")
        print(f"Allocated Budget: ${self.get_allocated_budget():.2f}")
        print(f"Total Expenses: ${self.__expenses:.2f}")
        print(f"Remaining Budget: ${remaining_budget:.2f}")

# Example Usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
print()
mortgage_category = BudgetCategory("Mortgage", 600)
mortgage_category.add_expense(600)
mortgage_category.display_category_summary()
