print("hello, welcome to spendWise!")
print("if you want to stop entering type: stop")

income = int(input("Enter your monthly income: "))

after_bill = income

bills_list = []

nameB = None

amountB = None

while income != 0 :
    bills = input("Enter the name of your bill and how much it is: ").lower()
    if bills == "stop":
        break 

    if bills.split(" ") and len(bills.split(" ")) == 2:
        nameB, amountB = bills.split(" ")
    else:
        while nameB == None and amountB == None:
            print("Invalid input. please enter a valid bill name and amount.")
            bills = input("Enter the name of your bill and how much it is: ")
            if bills.split(" ") and len(bills.split(" ")) == 2:
                nameB, amountB = bills.split(" ")

    if nameB.isalpha() and amountB.isdigit() :
        amountB = int(amountB)
        after_bill -= amountB
        
    else:
        print("Invalid input. please enter a valid bill name and amount.")
        continue
    
    bills_list.append(bills)

spending = (after_bill / income ) * 100


for i in bills_list:
    print(i)

if income == after_bill:
    print("You don't have any bills!")
elif spending > 80:
    print("You are spending more than 80% of your income!")
else:
    print(f"You are spending {spending:.2f}% of your income.")

print("Money left after bills:", after_bill)
