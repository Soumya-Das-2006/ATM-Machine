"""Write a Python program to simulate an ATM machine. The program should allow users to check their balance, deposit money, and withdraw money. Use functions to organize the code and handle different operations. and account details write the code in ATM_Machine.py"""

def check_balance(balance):
    print(f"Your current balance is: ${balance}")

def deposit(balance, amount, transactions):
    balance += amount
    transactions.append(f"Deposited: ${amount}")
    print(f"You have deposited: ${amount}")
    return balance

def withdraw(balance, amount, transactions):
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        transactions.append(f"Withdrew: ${amount}")
        print(f"You have withdrawn: ${amount}")
    return balance

def show_transactions(transactions):
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(t)

def main():
    balance = 0
    transactions = []
    pin = int(input("Insert your ATM card and enter your PIN to proceed: "))
    if pin != 1234:
        print("Incorrect PIN. Exiting.")
        return
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Transactions")
        print("5. Exit")
        choice = input("Please select an option (1-5): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount, transactions)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            print("Don't remove your ATM card until the transaction is complete.")
            pin_check = int(input("Enter your PIN: "))
            if pin_check == 1234:
                balance = withdraw(balance, amount, transactions)
            else:
                print("Incorrect PIN.")
        elif choice == "4":
            show_transactions(transactions)
        elif choice == "5":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()