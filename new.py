import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import pathlib
import pickle

class Account:
    accNo = 0
    name = ''
    deposit = 0
    type = ''

    def createAccount(self):
        self.accNo = int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
        print("\n\n\nAccount Created")

    def showAccount(self):
        print("Account Number : ", self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account", self.type)
        print("Balance : ", self.deposit)

    def modifyAccount(self):
        print("Account Number : ", self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        self.deposit -= amount

    def report(self):
        print(self.accNo, " ", self.name, " ", self.type, " ", self.deposit)

    def getAccountNo(self):
        return self.accNo

    def getAcccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit


def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
    else:
        oldlist = []
    oldlist.append(account)
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def view_all_accounts():
    res = []
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        res = pickle.load(infile)
        infile.close()
    if not res:
        messagebox.showinfo("No accounts found", "No existing records to display")
    else:
        account_str = "\n".join(map(str, res))
        messagebox.showinfo("All Accounts", account_str)


def create_new_account():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)
    messagebox.showinfo("Success", "New account created successfully")




root = tk.Tk()
root.title("Bank Management System")

create_account_button = tk.Button(root, text="Create new account", command=create_new_account)
create_account_button.pack()

view_all_accounts_button = tk.Button(root, text="View all accounts", command=view_all_accounts)
view_all_accounts_button.pack()

root.mainloop()


