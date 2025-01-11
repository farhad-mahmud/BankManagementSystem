from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


class Appli:
    def __init__(self, master):
        self.master = master
        def go_back():
            self.master.destroy()
        
        self.top = Frame(master, height=100, bg="#f4f5f5")
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=800, bg="#8e9b96")
        self.bottom.pack(fill=X)

        
        self.heading = Label(
            self.top, text="Balance Withdraw", font="helvetica 18 bold", bg="#f4f5f5"  
        )
        self.heading.place(x=265, y=30) 

        
        Label(self.bottom, text="Account Number", font="helvetica 14 bold", bg="#8e9b96").place(x=40, y=55)
        Label(self.bottom, text="Amount", font="helvetica 14 bold", bg="#8e9b96").place(x=40, y=110)
        Label(self.bottom, text="Current Balance", font="helvetica 14 bold", bg="#8e9b96").place(x=40, y=165)

        
        
        e_acc_no = Entry(self.bottom , width="45", )
        e_acc_no.place(x=320, y=55) 
        
        self.dp = Entry(self.bottom, width=60)
        self.dp.place(x=320, y=110)

        self.lb = Entry(self.bottom, width=60)
        self.lb.place(x=320, y=165)

        
        self.dep = Button(
            self.bottom,
            text="Withdraw",
            font="helvetica 15 bold",
            width=52,
            command=self.dept,
        )
        self.dep.place(x=45, y=270)
        self.back_btn = Button(self.bottom, text="Back",bg= "red" ,font="helvetica 15 bold", width="20", command=go_back)
        self.back_btn.place(x=45, y=330)

    def dept(self):
        acc_no = self.e_acc_no.get().strip()  
        amtn = self.dp.get().strip()              

        if not acc_no or not amtn:
            MessageBox.showinfo("Input Error", "Account number and amount are required.")
            return
        
        try:
            amtn = float(amtn)  
        except ValueError:
            MessageBox.showinfo("Input Error", "Enter a valid numeric amount.")
            return

        try:
            con = mysql.connect(
                host="localhost",
                user="root",
                password="donotrootfarhad",
                database="bank_data",
            )
            cursor = con.cursor()

            
            cursor.execute("SELECT amount FROM acct WHERE acc_no = %s", (acc_no,))
            result = cursor.fetchone()

            if result:
                current_balance = result[0]

                if amtn <= current_balance:
                    
                    cursor.execute(
                        "UPDATE acct SET amount = amount - %s WHERE acc_no = %s",
                        (amtn, acc_no),
                    )
                    con.commit()

                    
                    self.lb.delete(0, END)
                    self.lb.insert(0, float(current_balance) - amtn)


                    MessageBox.showinfo("Success", "Withdrawal Successful.")
                else:
                    MessageBox.showinfo("Error", "Insufficient balance.")
            else:
                MessageBox.showinfo("Error", "Account not found.")

        except mysql.Error as err:
            MessageBox.showinfo("Database Error", f"Error: {err}")
        finally:
            if 'con' in locals() and con.is_connected():
                con.close()


def main():
    root = Tk()
    app = Appli(root)
    root.geometry("700x500+200+20")
    root.resizable(height=0, width=0)
    root.mainloop()


if __name__ == "__main__":
    main()
