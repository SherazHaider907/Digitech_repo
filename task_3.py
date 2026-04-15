def withdraw(balance, amount):
    if amount <= 0:
        print("Amount must be greater than 0.")
        return balance
    if amount > balance:
        print("Insufficient balance.")
        return balance
    if amount % 500 != 0:
        print("Amount must be a multiple of 500.")
        return balance

    balance -= amount
    print("Withdrawal successful.")
    print("Remaining balance:", balance)
    return balance

pin = input("Enter your PIN: ")


correct_pin = "1234"
if pin != correct_pin:
    print("Access denied. Wrong PIN.")
else:
    balance = float(input("Enter your account balance: "))
    
    while True:
        amount = float(input("Enter withdrawal amount (0 to exit): "))
        
        if amount == 0:
            print("Thank you. Transaction ended.")
            break
        
        balance = withdraw(balance, amount)