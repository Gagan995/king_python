balance=1000


print("WELCOME to ATM")

choice=input("Choose an option\n 1. Check balance \n 2. Deposit \n 3. Withdraw \n 4. Exit ")



if choice == '1':
    print(f"Your balance is : {balance}")

elif choice == "2":
    amount= input("Enter the amount to deposit")

    balance=balance + int(amount)
    print("Your new balance is ",balance)

elif choice == '3':
    amount= int(input("Enter the amount to withdraw"))
    if balance< amount:
        print("Not enough balance")
    else:
        print(f"{amount} is withdrawn form you account" )
        balance= balance-amount
        print("Your new balannce is ",balance)

elif choice=="4":
    print("Thank you for visiting")

else:
    print("Invalid choice! please enter the choice from 1-4")

