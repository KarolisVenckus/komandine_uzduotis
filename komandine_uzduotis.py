import os

class Budget:
    def __init__(self):
        self.earnings = []
        self.expenses = []

    def add_earning(self, amount, comment):
        self.earnings.append({'amount': amount, 'comment': comment})

    def add_expense(self, amount, comment):
        self.expenses.append({'amount': amount, 'comment': comment})

    def view_earnings(self):
        print('--- EARNINGS ---')
        for earning in self.earnings:
            print(f"{earning['amount']}: {earning['comment']}")

    def view_expenses(self):
        print('--- EXPENSES ---')
        for expense in self.expenses:
            print(f"{expense['amount']}: {expense['comment']}")

    def view_budget(self):
        total_earnings = sum(earning['amount'] for earning in self.earnings)
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        balance = total_earnings - total_expenses
        print('--- BUDGET ---')
        print(f"Earnings: {total_earnings}")
        print(f"Expenses: {total_expenses}")
        print(f"Balance: {balance}")

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print('--- MENU ---')
            print('1. Add Earning')
            print('2. Add Expense')
            print('3. View Earnings')
            print('4. View Expenses')
            print('5. View Budget')
            print('6. Quit')
            choice = input('Enter your choice: ')

            if choice == '1':
                amount = float(input('Enter earning amount: '))
                comment = input('Enter comment: ')
                self.add_earning(amount, comment)
            elif choice == '2':
                amount = float(input('Enter expense amount: '))
                comment = input('Enter comment: ')
                self.add_expense(amount, comment)
            elif choice == '3':
                self.view_earnings()
            elif choice == '4':
                self.view_expenses()
            elif choice == '5':
                self.view_budget()
            elif choice == '6':
                break
            else:
                print('Invalid choice. Try again.')
            input('Press Enter to continue...')  # Wait for user to press Enter before continuing

budget = Budget()
budget.menu()