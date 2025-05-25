class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}₹ deposited successfully..")
        else:
            print("Invalid deposited amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount}₹, withdrawn successfully!!")
        else:
            print("Insufficient balance or invalid amount")

    def check_balance(self):
        print(f"Current balance : ₹{self.balance}")
    
def main():
    print("Welcome to Python Bank!")
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()