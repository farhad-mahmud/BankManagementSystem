from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import sys

class Appli(object):
    def __init__(self, master):
        self.master = master
        user = sys.argv[1] if len(sys.argv) > 1 else ""
        def go_back():
            self.master.destroy()
        def dept():
            amtn = dp.get()
            acc_no = e_acc_no.get()
            if not acc_no:
                MessageBox.showinfo("Input Error", "Account number is required.")
                return
            try:
                con = mysql.connect(host="localhost", user="root", password="donotrootfarhad", database="bank_data")
                cursor = con.cursor()

                
                cursor.execute("UPDATE acct SET amount = amount + %s WHERE acc_no = %s", (amtn, acc_no))
                con.commit()

                
                cursor.execute("SELECT amount FROM acct WHERE acc_no = %s", (acc_no,))
                myresult = cursor.fetchone()

                
                lb.delete(0, END)  
                if myresult:
                    lb.insert(0, myresult[0])

                MessageBox.showinfo("Success", "Amount deposited successfully.")
            except mysql.Error as e:
                MessageBox.showerror("Database Error", f"An error occurred: {str(e)}")
            except Exception as e:
                MessageBox.showerror("Error", f"An unexpected error occurred: {str(e)}")
            finally:
                if 'con' in locals() and con.is_connected():
                    con.close()

        def sub():
            acc_no = e_acc_no.get()
            if not acc_no:
                MessageBox.showinfo("Input Error", "Account number is required.")
                return
            try:
                con = mysql.connect(host="localhost", user="root", password="donotrootfarhad", database="bank_data")
                cursor = con.cursor()

                
                cursor.execute("SELECT amount FROM acct WHERE acc_no = %s", (acc_no,))
                myresult = cursor.fetchone()

                
                lb.delete(0, END)  
                if myresult:
                    lb.insert(0, myresult[0])
                else:
                    MessageBox.showinfo("Not Found", "Account not found.")

            except mysql.Error as e:
                MessageBox.showerror("Database Error", f"An error occurred: {str(e)}")
            except Exception as e:
                MessageBox.showerror("Error", f"An unexpected error occurred: {str(e)}")
            finally:
                if 'con' in locals() and con.is_connected():
                    con.close()

        
        self.top = Frame(master, height=100, bg="#f4f5f5")
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=800, bg="#8e9b96")
        self.bottom.pack(fill=X)

        
        self.heading = Label(self.top, text="Balance Deposit", font="helvetica 18 bold", bg="#f4f5f5")
        self.heading.place(x=265, y=30)

        
        
        acc_no_label = Label(self.bottom, text="Account number", font="helvetica 14 bold", bg="#8e9b96")
        acc_no_label.place(x=40, y=55)

        detail_label = Label(self.bottom, text="Current Balance", font="helvetica 14 bold", bg="#8e9b96")
        detail_label.place(x=40, y=165)

        amt_label = Label(self.bottom, text="Amount", font="helvetica 14 bold", bg="#8e9b96")
        amt_label.place(x=40, y=110)
        
        userval = StringVar()
        userval.set(user)  # Set the user value
        e_acc_no = Entry(self.bottom, textvariable=userval, width="60", bg="yellow",state="disabled",font=("arial",11,"bold"),fg="black")
        e_acc_no.place(x=320, y=55)

        lb = Entry(self.bottom, width="60",bg="yellow")
        lb.place(x=320, y=165)

        dp = Entry(self.bottom, width="60")  
        dp.place(x=320, y=110)

        
        self.dep = Button(self.bottom, text=" Deposit ", font="helvetica 15 bold", width="52", command=dept)
        self.dep.place(x=45, y=270)
        self.back_btn = Button(self.bottom, text="Back", font="helvetica 15 bold", width="20", command=go_back)
        self.back_btn.place(x=45, y=330)
       
        

def main():
    root = Tk()
    app = Appli(root)
    root.geometry("700x500+200+20")
    root.resizable(height=0, width=0)
    root.mainloop()


if __name__ == "__main__":
    main()
