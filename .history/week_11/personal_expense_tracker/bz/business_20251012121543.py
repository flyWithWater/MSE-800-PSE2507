
"""
Add Expense : Allow the user to add a new expense with a description and an amount.
Calculate Total Expense :  Compute and display the total amount of all recorded expenses.
"""


from week_11.personal_expense_tracker.dao.expense_dao import ExpenseDAO


class Business:


    def __init__(self):
        self._dao = ExpenseDAO()


    def add_expense(self,expense_name:str,amount:int):
        print(f"add new expense: amount:{amount}")
        self._dao.create_expense(expense_name=expense_name,amount=amount)

    def totalExpense(self):
        expense_list = self._dao.list_expenses()
        