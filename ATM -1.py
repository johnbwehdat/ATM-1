balance = 10000   # starting balance

while True:
    # Show menu
    print("\n--- ATM ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        print("Your balance is ₦" + str(balance))
    
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Deposited. New balance: ₦" + str(balance))
    
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawn. New balance: ₦" + str(balance))
        else:
            print("Insufficient funds.")
    
    elif choice == "4":
        print("Goodbye!")
        break   # exits the loop
    
    else:
        print("Invalid choice. Try again.")