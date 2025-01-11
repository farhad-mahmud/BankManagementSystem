from tkinter import *
import datetime
import os
from subprocess import call

def create_acc():
    call(["python", "create_acc.py"])

def delt_acc():
    call(["python", "Admin_delete_acc.py"])

def balq():
    call(["python", "Admin_bal_eq.py"])

def chk():
    call(["python", "Admin_check_acc.py"])

def bw():
    call(["python", "Admin_bal_wd.py"])

def bd():
    call(["python", "Admin_bal_dep.py"])

def fdr():
    call(["python", "Admin_fdr.py"])

def upd():
    call(["python", "upd_acc.py"])

def loan():
    call(["python", "Admin_loan.py"])

date = datetime.datetime.now().date()
date = str(date)

class Appli(object):
    def __init__(self, master):
        self.master = master

        
        self.top = Frame(master, height=150, bg="#f4f5f5")
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg="#8e9b96")
        self.bottom.pack(fill=X)

        
        self.heading = Label(self.top, text="BANK MANAGEMENT SYSTEM", font="helvetica 15 bold", bg="#f4f5f5")
        self.heading.place(x=202, y=50)

        self.date_lbl = Label(self.bottom, text="Date: " + date, bg="#8e9b96")
        self.date_lbl.place(x=600, y=20)

        
        buttons = [
            ("Create Account", create_acc, "> Create new user account"),
            ("Balance Enquiry", balq, "> Check account balance"),
            ("Check Account Details", chk, "> View account details"),
            ("Balance Withdraw", bw, "> Withdraw amount"),
            ("Balance Deposit", bd, "> Deposit amount"),
            ("FDR Service", fdr, "> Fixed deposit receipt"),
            ("Delete Account", delt_acc, "> Remove user account"),
            ("Update Account", upd, "> Modify user account"),
            #("User Administration", usr, "> Manage user roles"),
            ("Loan Service", loan, "> Manage loan options")
        ]

        
        x_offsets = [50, 400]  
        y_offset = 50
        button_spacing = 70

        for index, (btn_text, btn_command, btn_desc) in enumerate(buttons):
            col = index % 2  
            row = index // 2 

            x_pos = x_offsets[col]
            y_pos = y_offset + (row * button_spacing)

            # Button
            button = Button(
                self.bottom,
                text=btn_text,
                font="helvetica 13 bold",
                command=btn_command,
                width=20
            )
            button.place(x=x_pos, y=y_pos)

            
            label = Label(
                self.bottom,
                text=btn_desc,
                bg="#8e9b96",
                font="helvetica 10 bold"
            )
            label.place(x=x_pos, y=y_pos + 35)

def main():
    root = Tk()
    app = Appli(root)
    root.geometry("700x650+100+20")
    root.resizable(height=0, width=0)
    root.mainloop()

if __name__ == "__main__":
    main()
