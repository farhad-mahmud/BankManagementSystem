from tkinter import *
import datetime
import os
from subprocess import call
import sys



def balq():
    user=(userval.get())
    call(["python", "bal_eq.py",user])

def chk():
    user=(userval.get())
    call(["python", "chk_acc.py",user])

def bw():
    user=(userval.get())
    call(["python", "bal_wd.py",user])

def bd():
    user=(userval.get())
    call(["python", "bal_dep.py",user])

def fdr():
    user=(userval.get())
    call(["python", "Fdr.py",user])


def loan():
    user=(userval.get())
    call(["python", "loan.py",user])

# Current date
date = datetime.datetime.now().date()
date = str(date)

class Appli(object):
    def __init__(self, master):
        self.master = master
        user = sys.argv[1] if len(sys.argv) > 1 else ""


        self.top = Frame(master, height=150, bg="#f4f5f5")
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg="#8e9b96")
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text="BANK MANAGEMENT SYSTEM", font="helvetica 15 bold", bg="#f4f5f5")
        self.heading.place(x=235, y=50)

        self.date_lbl = Label(self.bottom, text="DATE : " + date, bg="#8e9b96")
        self.date_lbl.place(x=580, y=16)

        self.wlc_lbl = Label(self.bottom, text="WELCOME USER   || ", bg="#8e9b96", font="helvetica 16 bold")
        self.wlc_lbl.place(x=60, y=12)

        self.wlcaccno = Label(self.bottom, text="A/C No  : ", bg="#8e9b96", font="helvetica 16 bold")
        self.wlcaccno.place(x=255, y=12)

        global userval
        userval=StringVar()
        userval.set(user)
        welcomeaccno = Entry(self.bottom, width="20",textvariable=userval,state="disabled")  
        welcomeaccno.place(x=350, y=18)

        buttons = [
            ("Balance Enquiry", balq, "> Check account balance"),
            ("My Account", chk, "> View account details"),
            ("Balance Withdraw", bw, "> Withdraw amount"),
            ("Balance Deposit", bd, "> Deposit amount"),
            ("FDR Service", fdr, "> Fixed deposit receipt"),
            #("Delete Account", delt_acc, "> Remove user account"),
            #("Update Account", upd, "> Modify user account"),
            #("User Administration", usr, "> Manage user roles"),
            ("Loan Service", loan, "> Manage loan options")
        ]

        x_offsets = [50, 400]  # Column positions for buttons
        y_offset = 100  # Starting Y position for the first row
        button_spacing = 70  # Space between rows

        for index, (btn_text, btn_command, btn_desc) in enumerate(buttons):
            col = index % 2  # Determine the column (0 or 1)
            row = index // 2  # Determine the row

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

            # Description label
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
    root.geometry("700x570+100+20")
    root.resizable(height=0, width=0)
    root.mainloop()

if __name__ == "__main__":
    main()
