withdrawal = int(input("enter the withdrawal amount: "))
balance = int(input("enter the balance amount: "))
if withdrawal > balance:
    print("insufficient balance")
else:
    print("transaction successful=", balance-withdrawal)
if withdrawal%100!=0:
    print("enter the multiples of 100: ")
