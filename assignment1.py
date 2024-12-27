#initial setup
balance = 1000
print("Welcome To My ATM")

while True:
 #Menu Display
 print("1. check Balance")
 print("2. Deposit")
 print("3. withdraw")
 print("4. Exit")
 
 choice =input("choose an option(1-4)?:")
if choice =="1":
    print(f"your current balance is :${balance} ")
elif choice == "2":
    amount= float (input("Enter your amount :$ "))
    balance += amount
    print(f"deposit sucessful| new balance :${balance}")
elif choice =="3":
    amount=float(input("Withdraw amount:$"))
    if amount <= balance:
        balance -= amount
        print (f"current balance :${balance}")
    else:
        print("insufficient balance")
elif choice == "4" :
    print("thank you")
    "break"
else:
    print("invalidcode")

