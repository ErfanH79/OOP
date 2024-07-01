
from match_data import model
import time
import threading
from math import *
import random

class users:
    def __init__(self,name,National_ID,password,number,email):
        self.name = name
        self.National = National_ID
        self.password = password
        self.number = number
        self.email = email
    def information(self):
        return self.name+"  "+self.National+"  "+self.password+"  "+self.number+"  "+self.email +"\n"


class Account:
    def __init__(self,alias,owner,password,type_,account_number,inventory):
        self.alias = alias
        self.owner =owner 
        self.password = password
        self.type = type_
        self.inventory = float(inventory)
        self.number = int(account_number)
    def modify(self,new):
        self.inventory += new
    def information(self):
        return self.alias+"  "+self.owner+"  "+self.password+"  "+self.type+"  "+str(self.number)+"  "+str(self.inventory)+"\n"


class Transactions:
    def __init__(self,sender,reciver,transfer_amount):
        self.sender = sender
        self.reciver = reciver
        self.transfer_amount = transfer_amount
    def information(self):
        return self.sender+"  "+self.reciver+"  "+str(self.transfer_amount)+"\n"


def Create_user():
    name = input('**Please enter your name:\n')
    national_id = input('**Please enter your national_id:\n')
    password = input('**Please enter your password:\n')
    number = input('**Please enter your number:\n')
    email = input('**Please enter your email:\n')
    user = users(name,national_id, password, number, email)
    information = user.information()
    with open('Users.txt','r') as f:
        data = f.readlines()
        l = 0
        for i in data:
            sample = i.split('  ')
            if name == sample[1] or national_id == sample[2]:
                l+=1
        if l!=0:
            print('You are an user,please login or choose another name and national id')
            return 0
        else:
            model.insert("Users",information)
            print('You are an user now!')
            return 1


def Admin_view():
    while True:
        A = input("**Enter 1 if you want to see list of users**\n"
                  "**Enter 2 if you want to see list of Accounts**\n"
                  "**Enter 3 if you want to see list of Transactions**\n")
        if A in ['1','2','3']:
            if A == '1':
                with open('Users.txt','r') as f:
                    files = f.readlines()
                    for i in files:
                        print(i)
                break
            if A == '2':
                with open('Accounts.txt','r') as f:
                    files = f.readlines()
                    for i in files:
                        print(i)
                break
            if A == '3':
                with open('Transactions.txt','r') as f:
                    files = f.readlines()
                    for i in files:
                        print(i)
                break
        else:
            print("Please enter a valid number!")
 

def Create_account(owner):
    while True:
        A = input("Enter your account type:"+"\n[useful(1),regular(2)]\n")
        if A == '2':
            type_ = "regular"
            break
        elif A == '1':
            type_ = "useful"
            break
        else:
            "Please Enter a valid number"
    alias = input("**Enter your account alias:\n")
    password = input("**Enter your account password:\n")
    while True:
        inventory = input("**Enter your inventory:\n")
        if inventory.isdigit():
            break
        else:
            print("Please enter a valid input(INTEGER)")
    X = random.randint(10000000,100000000)
    print('Your account number is:',X)
    account = Account(alias,owner.name,password,type_,X,inventory)
    information = account.information()
    with open("Accounts.txt",'r') as f:
        data = f.readlines()
        l = 0
        for i in data:
            sample = i.split('  ')
            if alias == sample[1] :
                l+=1
        if l!=0:
            print('The alias is already exists,please choose another name')
            return 0
        else:
            model.insert("Accounts",information)
            print("Your account created successfully")
            return 1


def change_account(U):
    while True:
        A = input("**Enter 1 to change your account's type to regular**\n"
                  "**Enter 2 to change your account's type to useful**\n")
        if A in ['1','2']:
            break
        else:
            print("Please enter a valid number")
    if A == '1':
        U.type = 'regular'
    else:
        U.type = 'useful'
    I = U.information()
    model.update('Accounts',str(U.alias),I)
    print("Your account's type updated successfully")


def choose_account(U):
    A = str(U.name)
    liste = []
    with open("Accounts.txt",'r') as f:
        files = f.readlines()
        for i in files:
            j = i.split('  ')
            if A == j[2]:
                liste.append(j[1])
    if len(liste) == 0:
        print("You don't have any account")
        return 0
    else:
        while True:
            L = 0
            print(liste)
            H = input("**Please enter one of your accounts name:\n")
            if H in liste:
                B = input('**Enter your account password:\n')
                with open('Accounts.txt','r') as f:
                    files = f.readlines()
                    for i in files:
                        j = i.split("  ")
                        if H == j[1] and B == j[3]:
                            C = j
                            D = Account(C[1], C[2], C[3], C[4], C[5],C[6])
                            if A == D.owner:
                                return D
                                break
                    if L==0:
                        print("The password is wrong!")
                        return 0
            else:
                print("Please enter a true value!")


def change_user_information(U):
    while True:
        A = input("**Enter 1 if you want to change name**\n"
                  "**Enter 2 if you want to change national id**\n"
                  "**Enter 3 if you want to change password**\n"
                  "**Enter 4 if you want to change phone number**\n"
                  "**Enter 5 if you want to change email**\n")
        if A in ['1','2','3','4','5']:
            if A == '1':
                print("The name is:",U.name)
                A = input("**Enter the new name:")
                with open("Accounts.txt",'r') as f:
                    files = f.readlines()
                    for i in files:
                        j= i.split("  ")
                        if j[2] == U.name:
                            D = Account(j[1], j[2], j[3], j[4], j[5], j[6])
                            D.owner = A
                            model.update("Accounts",D.alias,D.information())
                U.name = A
                model.update1('Users',U.National,U.information())
                print('Name change completed')
                model.sort("Users")
                break

            if A == '2':
                print("The national id is:",U.National)
                A = input("**Enter the new national id:")
                U.National = A
                model.update('Users',U.name,U.information())
                print('National id change completed')
                model.sort("Users")
                break

            if A == '3':
                print("The password is:",U.password)
                A = input("**Enter the new password:")
                U.password = A
                model.update('Users',U.name,U.information())
                print('Password change completed')
                model.sort("Users")
                break

            if A == '4':
                print("The phone number is:",U.number)
                A = input("**Enter the new phone number:")
                U.number = A
                model.update('Users',U.name,U.information())
                print('Phone number change completed')
                model.sort("Users")
                break

            if A == '5':
                print("The email is:",U.email)
                A = input("**Enter the new email:")
                U.email = A
                model.update('Users',U.name,U.information())
                print('Email change completed')
                model.sort("Users")
                break
        else:
            print("Please enter a valid number!")


def get_loan(U,L):
    print("well done")
    A = float(float(L)/12)
    B = float(U.inventory)
    U.modify(float(L))
    model.update("Accounts",str(U.alias),U.information())
    time.sleep(5)
    for i in range(13):
        if abs(U.inventory-B) <= 0.001 :
            U.inventory = B
            model.update("Accounts",str(U.alias),U.information())
            break
        else:
            U.modify(-(A))
            model.update("Accounts",str(U.alias),U.information())
            time.sleep(10)


def login():
    national_id = input('**Enter your national_id:\n')
    password = input('**Enter your password:\n')
    c = 0
    with open('Users.txt','r') as f:
        data = f.readlines()
        for i in data:
            j = i.split('  ')
            if national_id == j[2] and password == j[3]:
                print("You are logged in!")
                user = users(j[1],j[2],j[3],j[4],j[5])
                return user
                c+=1
            elif national_id == j[2] and password != j[3]:
                print("Password is wrong!")
                return 0
        if c == 0: print('There is no account with that national id!') 
        return 0


def login_Admin():
    security_code = input('**Please enter the security code:\n')
    if security_code == "Password_hello":
        print("You are logged in!")
        return 1
    else: 
        print("The security code was incorect!")
        return 0


def useful(U):
    L = []
    with open("Accounts.txt",'r') as f:
        files = f.readlines()
        for i in files:
            j = i.split("  ")
            if j[4] == "useful" and str(U.alias) != j[1]:
                L.append(j[1])
    if len(L) == 0: print("There is not any useful account") 
    else: 
        print("Useful accounts are:")
        print(L)


def Transaction(U):
    while True:
        Transfer_amount = input("**Enter your transfer amount:\n")
        if Transfer_amount.isdigit():
            T = float(Transfer_amount)
            break
        else:
            print("Please enter a true value!")
    useful(U)
    alias = input("**Enter the alias our number of destination account:\n")
    with open("Accounts.txt",'r') as f:
        data = f.readlines()
        l = 0
        for i in data:
            j = i.split('  ')
            if alias == j[1] or alias == j[5] :
                destination = Account(j[1],j[2],j[3],j[4],j[5],j[6])    
                l+=1
                break
        if l==0: 
            print('There is not any account whith this alias or number!')
            return 0
        if float(U.inventory) < T:
            print("There is not enough inventory")
            return 0
        else:
            U.modify(-(T))
            destination.modify(T)
            A = U.information()
            B = destination.information()
            model.update('Accounts',str(U.alias),A)
            model.update('Accounts',str(destination.alias),B)
            T = Transactions(str(U.alias),str(destination.alias),T)
            I = T.information()
            model.insert('Transactions',I)
            print("Well done!")
            return 1 


def choose_user():
    A = input("**Enter the national code of the desired user:\n")
    L = 0
    with open("users.txt", "r") as f:
        files = f.readlines()
        for i in files:
            j = i.split('  ')
            if A == j[2]:
                D = users(j[1], j[2], j[3], j[4], j[5])
                L+=1
    if L == 0: 
        print("There is not any user with this national code!")
        return 0
    else:
        return D
    

def choose_account_admin():
    A = input("**Enter the alias of the desired account:\n")
    L = 0
    with open("Accounts.txt", "r") as f:
        files = f.readlines()
        for i in files:
            j = i.split('  ')
            if A == j[1]:
                D = Account(j[1], j[2], j[3], j[4], j[5],j[6])
                return D
                L +=1
    if L == 0: 
        print("There is not any account with this alias!")
        return 0
    else:
        return D


def connect_to_owner(Account):
    A = str(Account.owner)
    with open("Users.txt","r") as f:
        files = f.readlines()
        for i in files:
            j = i.split("  ")
            if j[1] == A:
                B = users(j[1], j[2], j[3], j[4], j[5])
                return B

        
def change_inventory(D):
    print("inventory is:",D.inventory)
    while True:
        A = input("**Enter the new inventory:")
        if A.isdigit():
            break
        else:
            print("Please enter a valid input")
    D.inventory = A
    model.update('Accounts',D.alias,D.information())
    print('Inventory change completed')


def show_information(D):
    print("Alias  Owner  Password  Type  Number  Inventory")
    print(D.information())
    L = 0
    with open("Transactions.txt",'r') as f:
        files = f.readlines()
        for i in files:
            j = i.split('  ')
            if str(D.alias) == j[1] or str(D.alias) == j[2]:
                T = Transactions(j[1], j[2], j[3])
                print("Sender  Reciver  Transfer_amount")
                print(T.information())
                L+=1
    if L == 0:
        print("You don't have any transaction\n")
 

def paying_the_bill(D):
    A = input("**Please enter id of bill:\n")
    while True:
        B = input("**Please enter bill amount:\n")
        if B.isdigit():
            break
        else:
            print('Please enter a true value!')
    C = float(B)
    if float(D.inventory) < C:
        print("There is not enough inventory")
    else:
        D.modify(-C)
        L = D.information()
        model.update("Accounts",str(D.alias),L)
        T = Transactions(str(D.alias),"bill",B)
        model.insert("Transactions",T.information())
        print("The bill was paid")


def close_account(U):
    code = input("**Enter password of this account:\n")
    if code == str(U.password):
        if float(U.inventory)== 0:
            I1 = U.information().split("  ")
            model.delete('Accounts',I1[0])
        else:
            useful(U)
            New = input("**Enter the alias or number of an account to transfer resources:\n")
            with open("Accounts.txt",'r') as f:
                filee = f.readlines()
                l = 0
                for i in filee:
                    j = i.split("  ")
                    if New == j[1] or New == j[5]:
                        L= Account(j[1], j[2], j[3], j[4], j[5],j[6])
                        L.modify(float(U.inventory))
                        model.delete('Accounts',str(U.alias))
                        model.update('Accounts',str(L.alias),L.information())
                        T = Transactions(str(U.alias),str(L.alias),U.inventory)
                        model.insert('Transactions',T.information())
                        l+=1
                        print("Your account has been deleted")
                        return 1
                if l==0:
                    print("There is not any account with this alias or number!")
                    return 0
    else:
        print("The password is incorrect!")
        return 0



def step1():
    while True: 
        A = input("**Enter 1 if you want to sign in**\n"
                  "**Enter 2 if you want to sign up**\n"
                  "**Enter 3 if you want to sign in as admin**\n")
        if A in ["1","2","3"]:
            if A == '1': 
                C = login()
                if C != 0:
                    break
            elif A == '2': 
                Create_user()
            elif A == '3':
                Q = login_Admin()
                if Q == 1:
                    return step4()
                    break
        else:
            print("Please enter a valid number")
    return step2(C)


def step2(C):
    while True: 
        A = input("**Enter 0 if you want to logout**\n"
                  "**Enter 1 if you want to create an account**\n"
                  "**Enter 2 if you want to choose an account**\n")
        if A in ["0","1","2"]:
            if int(A) == 0:
                return step1()
                break
            elif int(A)== 1:
                B = Create_account(C)
            elif int(A)== 2:
                D = choose_account(C)
                if D != 0:
                    break
        else:
            print("Please enter a valid number")
    return step3(D)


def step3(D):
    while True: 
        A =input("**Enter 0 if you want to return Previous step**\n"
                 "**Enter 1 if you want to have a transaction**\n"
                 "**Enter 2 if you want to close account**\n"
                 "**Enter 3 if you want to pay a bill**\n"
                 "**Enter 4 if you want to see informations(Transactions)**\n"
                 "**Enter 5 if you want to change your account's type**\n"
                 "**Enter 6 if you want to get loan**\n")
        if A in ["0",'1','2',"3",'4','5','6']:
            if A == "0":
                B = connect_to_owner(D)
                return step2(B)
                break
            if A == "2":
                L = close_account(D)
                if L!=0:
                    B = connect_to_owner(D)
                    return step2(B)
                    break
            if A == "1":
                Transaction(D)
            if A == '3':
                paying_the_bill(D)
            if A == '4':
                show_information(D)
            if A == '5':
                change_account(D)
            if A == '6':
                while True:
                    L = input("**Enter the loan amount:\n")
                    if L.isdigit():
                        break
                    else:
                        print("Please enter a valid input!")
                p1 = threading.Thread(target=step3, args=(D,))
                p2 = threading.Thread(target=get_loan,args=(D,L)) 
                break
        else:
            print("Please enter a valid number")
    p1.start()
    p2.start()

def step4():
    while True:
        A = input("**Enter 0 if you want to logout**\n"
                  "**Enter 1 if you want to see informations**\n"
                  "**Enter 2 if you want to create a new user**\n"
                  "**Enter 3 if you want to create a new account**\n"
                  "**Enter 4 if you want to close an account**\n"
                  "**enter 5 if you want to change inventory of an account**\n"
                  "**Enter 6 if you want to change an user information**\n")
        if A in ['0','1','2','3','4','5','6']:
            if A == '0':
                return step1()
                break
            if A == "1":
                Admin_view()
            if A == '2':
                Create_user()
            if A == '3':
                D = choose_user()
                if D !=0:
                    Create_account(D)
            if A == '4':
                D = choose_account_admin()
                if D !=0:
                    close_account(D)
            if A == '5':
                D = choose_account_admin()
                if D !=0:
                    change_inventory(D)
            if A == '6':
                D = choose_user()
                if D !=0:
                    change_user_information(D)
        else:
            print("Please enter a valid number!")  
print("\t******************************\n"+"\t****Welcome To Bank System****\n"+"\t******************************")
step1()