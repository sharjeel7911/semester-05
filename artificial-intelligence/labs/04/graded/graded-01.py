# Task - 01
def compress(text: str) -> list:
    result = []
    if len(text) == 0:
        return []
    result.append(text[0])    
    for i in range(len(text)):
        if(text[i] != text[i - 1]):
            if(result[:-1] != text[i]):
                result.append(text[i])
    return result

text = "aabbbcca"
print(compress(text))
text = "aabbbcca"
print(compress(text))


# ==================================================

# Task - 02
print("Enter balance")
bal = int(input())
balance = 0
if bal > 0:
    balance = bal
else:
    print("ERROR: Enter valid balance")

# ======================

# Methods
def deposit(balance, amount):
    if amount <= 0:
        return balance
    else:
        return balance + amount
        
def withdraw(balance, amount):
    if amount <= 0 or amount > balance:
        return balance
    else:
        return balance - amount
        
def show_balance():
    return balance
    
def withdrawals_possible(balance, amount):
     if amount <= 0 or amount > balance:
        return -1
     else:
         count = 0 
         while balance > 0:
             balance = balance - amount
             count += 1
     return count  

# ==================================================

# Loop
i = 1
while i == 1:
    print("1. Deposit \n2. Withdraw \n3. Show balance \n4. Withdrawals possible \n5. Exit")
    x = int(input())
    if x == 1:
        amount = int(input("Enter amount"))
        bal = deposit(balance, amount)
        if bal == balance:
            print("ERROR: You entered 0 or negative value\n")
        else:
            balance = bal    
            print("New Balance:", balance)
            print()
    if x == 2:
        amount = int(input("Enter amount"))
        bal = withdraw(balance, amount)
        if bal == balance:
            print("ERROR: You entered 0, negative or bigger value than balance\n")
        balance = bal    
        print("New Balance:", balance)
        print()
    if x == 3:
        print("Balance:", show_balance())
    if x == 4:
        amount = int(input("Enter amount"))
        bal = withdrawals_possible(balance, amount)
        if bal == -1:
            print("ERROR: You entered 0, negative or bigger value than balance\n")
        else:
            print("Total possible withdrawls:", bal)
            print()
    if x == 5:
        print("Goodbye")
        break
