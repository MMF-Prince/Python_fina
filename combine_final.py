
from random import randint 
from abc import ABC
from datetime import datetime


class Bank:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        self.total_balance=0
        self.total_loan_balance=0
        self.loan_feature_activation=True
        self.admin_panel=[]
        self.user_archive=[]
        
class User(ABC):
    def __init__(self,name,email,address) -> None:
        super().__init__()
        self.name=name
        self.email=email
        self.address=address


class Customer(User):
    def __init__(self, name, email, address,account_type) -> None:
        super().__init__(name, email, address)
        self.account_type=account_type
        self.balance=0
        self.account_number=randint(1000,2000)
        self.transaction_history=[{}]
        self.loan_time=0
        self.loan_balance=0

    def deposit_amount(self,dep_amount,bank):
        if dep_amount>0:
            self.balance+=dep_amount
            bank.total_balance+=dep_amount
            x=datetime.now()
            y=x.strftime("%x")
            self.transaction_history.append({f"Date:{y}": f"Amount Deposited: {dep_amount}"})
            print(f"{dep_amount}Tk Successfully deposited to your account")
        else:
            print("You entered an invalid deposit amount")

    def widraw_amount(self,wid_amount,bank):
        if wid_amount>self.balance:
            print("Withdraw amount exceeded")
        elif wid_amount>bank.total_balance:
            print("Sorry!!! bank is bankrupt.")
        else:
            self.balance-=wid_amount
            bank.total_balance-=wid_amount
            x=datetime.now()
            y=x.strftime("%x")
            self.transaction_history.append({f"Date:{y}": f"Amount Widrwan: {wid_amount}"})
            print(f"{wid_amount}Tk successfully widrawn from your account")

    def check_balance(self):
        print(f"Your available balance: {self.balance}")
    
    def check_transaction_history(self):
        for index in self.transaction_history:
            print(index)

    def take_loan(self,loan_amount,bank):
        if bank.loan_feature_activation==False:
            print("Sorry!!! Your bank dosen't allow loan system")
        elif self.loan_time>=2:
            print("Sorry!! you have already taken loan for maximum time")
        elif loan_amount>2*self.balance:
            print("Sorry !! You only can take loan twice of your current account balance")
        else:
            self.loan_balance+=loan_amount
            bank.total_loan_balance+=loan_amount
            bank.total_balance-=loan_amount
            print(f"Congratulation!! Your {loan_amount}Tk loan granted")
            self.loan_time+=1

    def repay_loan(self,repay_amount,bank):
        if bank.loan_feature_activation==False:
            print("Sorry!!! Your bank dosen't allow loan system")
        elif self.loan_balance<=0:
            print("Sorry!! you do not have any loan to repay")
        else:
            self.loan_balance-=repay_amount
            bank.total_loan_balance-=repay_amount
            bank.total_balance+=repay_amount
            print(f"Congratulation!! You repaid {repay_amount}Tk loan. Your remaining loan amount is: {self.loan_balance}Tk")
        
    def transfer_amount(self,other_account,t_amount):
        if self.balance<t_amount:
            print("Sorry!! you dont have enough balance to transfer")
        else:
            self.balance-=t_amount
            other_account.balance+=t_amount
            print("Successfully Transfered")


class Admin(User):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)

    def delete_user(self,name,email,bank):
        for object in bank.user_archive:
            if object.name==name and object.email==email:
                bank.user_archive.remove(object)
                bank.total_balance-=object.balance

    def see_all_user(self,bank):
        for object in bank.user_archive:
            print(f"Nmae: {object.name} Account Number: {object.account_number} Available Balance: {object.balance}")
    
    def total_available_balance_of_bank(self,bank):
        print(f"Total available balance of bank: {bank.total_balance}")

    def total_loan_amount(self,bank):
        print(f"Total loan balance of bank: {bank.total_loan_balance}")

    def loan_feature_on(self,bank):
        bank.loan_feature_activation=True

    def loan_feature_off(self,bank):
        bank.loan_feature_activation=False


bank=Bank("Bangladesh Bank","Dhaka")
def customer_choice(customer):
    while True:
            print("1. Deposit")
            print("2. Widraw")
            print("3. Check Balance")
            print("4. check Transaction History")
            print("5. Take Loan")
            print("6. Repay Loan")
            print("7. Transfer Money")
            print("8. Exit ")

            choice=int(input("Enter your choice : "))
            if choice==1:
                dep_amount=int(input("Deposit Amount: "))
                customer.deposit_amount(dep_amount,bank)
            elif choice==2:
                wid_amount=int(input("Widraw Amount: "))
                customer.widraw_amount(wid_amount,bank)
            elif choice==3:
                customer.check_balance()
            elif choice==4:
                customer.check_transaction_history()
            elif choice==5:
                loan_amount=int(input("Loan Amount: "))
                customer.take_loan(loan_amount,bank)
            elif choice==6:
                repay_amount=int(input("Repay Amount: "))
                customer.repay_loan(repay_amount,bank)
            elif choice==7:
                transfer_amount=int(input("Transfer Amount: "))
                customer2_name=input("Desired account name: ")
                customer2_email=input("Desired account email: ")
    
                flag=True
                for obj in bank.user_archive:
                    if obj.name==customer2_name and obj.email==customer2_email:
                        customer.transfer_amount(obj,transfer_amount)
                        print("Your Transfer is successful")
                        flag=False
                if flag==True:
                    print("Failed!!! Your desired bank account dosem't exist")
            elif choice==8:
                break
            else:
                print("Invalid Choice")

def admin_choice(admin):
    while True:
        print("1. Delete User")
        print("2. See all user")
        print("3. Total Available balace of Bank")
        print("4. Total Loan Amount")
        print("5. Loan Feature on")
        print("6.Loan feature off")
        print("7. Exit ")

        choice=int(input("Enter your choice : "))
        if choice==1:
            user_name=input("User name:")
            user_email=input("User email:")
            admin.delete_user(user_name,user_email,bank)
        elif choice==2:
            admin.see_all_user(bank)
        elif choice==3:
            admin.total_available_balance_of_bank(bank)
        elif choice==4:
            admin.total_loan_amount(bank)
        elif choice==5:
            admin.loan_feature_on(bank)
        elif choice==6:
            admin.loan_feature_off(bank)
        elif choice==7:
            break
        else:
            print("Invalid Choice")
        



def customerr(type):
    print("Thank you for choosing our bank !!!\n")
    name=input("Enter Your name: ")
    email=input("Enter Your email: ")
    flag=True
    if type=="old":
        if len(bank.user_archive)>0:
            for object in bank.user_archive:
                if object.name==name and object.email==email:
                    customer_choice(object)
                    flag=False
        if flag==True:
                print("Invalid user account")
    else:        
        address=input("Enter Your address: ")
        account_type=input("Enter Your account type savings/current: ")
        customer=Customer(name=name,email=email,address=address,account_type=account_type)
        bank.user_archive.append(customer)
        print(f"Congratulation {customer.name} your account is created!! ")
        customer_choice(customer)
        
    
def admin():
    print("Welcome to admin space\n")
    add=int(input("1.Admin login.\n2.New admin account open\nYour Choice: "))
    name=input("Enter Your name: ")
    email=input("Enter Your email: ")
    address=input("Enter Your address: ")
    if add==2:
        admin=Admin(name=name,email=email,address=address)
        bank.admin_panel.append(admin)
        print(f"Congratulation {admin.name} your account is created!! ")
        admin_choice(admin)
    elif add==1:
        flag=False
        if len(bank.admin_panel)==0:
            flag=False
        else:
            for object in bank.admin_panel:
                if object.name==name and object.email==email and object.address==address:
                    flag=True
                    admin_choice(object)

        if flag==False:
                print("Invalid admin account")
    else:
        print("Invalid Choice")
        
        



while True:
    print(f"*** Welcome to {bank.name}!! ***")
    print("1. Account Holder")
    print("2. Admin")
    print("3. New account open")
    print("4. Exit")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        customerr("old")
    elif choice==2:
        admin()
    elif choice==3:
        customerr("new")
    elif choice==4:
        break
    else:
        print("Invalid Input")