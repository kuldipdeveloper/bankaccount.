class bank_account():
    def __init__(self):
        self.amount = 0
    def deposit(self,Amount):
        self.amount+=Amount
        print("Amount Successfully Deposited")
    def withdraw(self,Amount):
        if(self.amount-Amount>=500):
            self.amount-=Amount
            print("Amount Successfully withdrawn")
        else:
            print("Insufficent Balance.\nyou have to keep atleast Rs.500 in your Account")
    def display(self):
         print("your Bank Balance is:",self.amount)

a=bank_account()
for i in range(0,50):
    print("1.Deposit 2.withdraw 3.Display 4.Exit")
    p=int(input("Enter your choice:"))
    if(p==1):
        Amount=float(input("Enter Amount to be Deposit"))
        a.deposit(Amount)
    elif(p==2):
        Amount=float(input("Enter Amount to be withdrawn:"))
        a.withdraw(Amount)
    elif(p==3):
        a.display()
        exit()
    else:
         print("you have entered a wrong value")



