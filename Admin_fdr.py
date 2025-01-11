from tkinter import *
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql

class Appli(object):
    def __init__(self, master):
        
        self.master = master
        def go_back():
            self.master.destroy()

        
        self.top = Frame(master, height=100, bg="#f4f5f5")
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=600, bg="#8e9b96")
        self.bottom.pack(fill=X)
        
        
        self.heading = Label(
            self.top, text="FDR System", font="helvetica 18 bold", bg="#f4f5f5"
        )
        self.heading.place(x=265, y=30)

        
        Label(self.bottom, text="Account Number", font="helvetica 14 bold", bg="#8e9b96").place(x=40, y=55)
        Label(self.bottom, text="Deposit Amount", font="helvetica 14 bold", bg="#8e9b96").place(x=40, y=110)
        Label(self.bottom, text="Term (years)", font="helvetica 14 bold", bg="#8e9b96").place(x=40, y=165)
        Label(self.bottom, text="Interest Rate (%)", font="helvetica 14 bold", bg="#8e9b96").place(x=40, y=220)
        Label(self.bottom, text="Maturity Amount", font="helvetica 14 bold", bg="#8e9b96").place(x=40, y=275)

        
        
        self.e_acc_no = Entry(self.bottom, width = 60)
        self.e_acc_no.place(x=320, y=55)
     
        self.dp = Entry(self.bottom, width=60)
        self.dp.place(x=320, y=110)

        self.term = Entry(self.bottom, width=60)
        self.term.place(x=320, y=165)

        self.rate = Entry(self.bottom, width=60)
        self.rate.place(x=320, y=220)

        self.maturity = Entry(self.bottom, width=60)
        self.maturity.place(x=320, y=275)

        
        self.calculate = Button(
            self.bottom,
            text="Calculate Maturity",
            font="helvetica 15 bold",
            width=25,
            command=self.calculate_maturity,
        )
        self.calculate.place(x=45, y=350)

        self.save = Button(
            self.bottom,
            text="Save FDR",
            font="helvetica 15 bold",
            width=25,
            command=self.save_fdr,
        )
        self.save.place(x=400, y=350)

        self.back_btn = Button(self.bottom, text="Back",bg= "red" ,font="helvetica 15 bold", width="20", command=go_back)
        self.back_btn.place(x=45, y=415)

    def calculate_maturity(self):
        try:
            deposit = float(self.dp.get().strip())
            term = int(self.term.get().strip())
            rate = float(self.rate.get().strip())
            maturity = deposit * (1 + (rate / 100) * term)
            self.maturity.delete(0, END)
            self.maturity.insert(0, round(maturity, 2))
        except ValueError:
            MessageBox.showinfo("Input Error", "Enter valid numbers for deposit, term, and rate.")

    def save_fdr(self):
        acc_no = self.e_acc_no.get().strip()  #kono empty ba extra value na ashar jonno  strip ()
        deposit = self.dp.get().strip()
        term = self.term.get().strip()
        rate = self.rate.get().strip()
        maturity = self.maturity.get().strip()

        if not acc_no or not deposit or not term or not rate or not maturity:
            MessageBox.showinfo("Input Error", "All fields are required.")
            return

        try:
            con = mysql.connect(
                host="localhost",
                user="root",
                password="donotrootfarhad",
                database="bank_data",
            )
            cursor = con.cursor()

            
            cursor.execute(
                "INSERT INTO fdr (acc_no, deposit, term, rate, maturity) VALUES (%s, %s, %s, %s, %s)",
                (acc_no, deposit, term, rate, maturity),
            )
            con.commit()
            MessageBox.showinfo("Success", "FDR Saved Successfully.")
        except mysql.Error as err:
            MessageBox.showinfo("Database Error", f"Error: {err}")
        finally:
            if 'con' in locals() and con.is_connected():
                con.close()

def main():
    root = Tk()
    app = Appli(root)
    root.geometry("700x600+300+0")
    root.resizable(height=0, width=0)
    root.mainloop()

if __name__ == "__main__":
    main()
