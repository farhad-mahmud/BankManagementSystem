from tkinter import *
import os
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


class Appli(object):
  def __init__(self, master):
     self.master=master
     def go_back():
         self.master.destroy()
     def sub():
         acc_no = e_acc_no.get()

         if not acc_no:
             MessageBox.showinfo("Input Error", "Account number is required.")    
             return

         try:
             con = mysql.connect(host="localhost", user="root", password="donotrootfarhad", database="bank_data")
             cursor = con.cursor()

             
             cursor.execute("SELECT amount FROM acct WHERE acc_no = %s", (acc_no,))
             myresult = cursor.fetchall()

             if myresult:
                 
                 lb.delete(0, END)
                 for x in myresult:
                     lb.insert(0, x)
                 MessageBox.showinfo("Success", "Account balance fetched successfully.")
             else:
                 MessageBox.showinfo("Not Found", "Account not found.")
         
         except mysql.Error as e:
             MessageBox.showerror("Database Error", f"An error occurred: {str(e)}")
         except Exception as e:
             MessageBox.showerror("Error", f"An unexpected error occurred: {str(e)}")
         finally:
             if 'con' in locals() and con.is_connected():
                 con.close()


     

     self.top= Frame(master, height=100 , bg= "#f4f5f5")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=800, bg="#8e9b96")
     self.bottom.pack(fill=X)

     
     self.heading= Label(self.top, text="Balance Enquiry", font="helvetica 18 bold", bg="#f4f5f5")
     self.heading.place(x= 265, y=30)

     

     
     Label(self.bottom, text="Account number ", font="helvetica 14 bold", bg="#8e9b96").place(x=40, y=55)
     Label(self.bottom, text="Details -> ", font="helvetica 14 bold", bg="#8e9b96").place(x=40, y=110)

     
     
     e_acc_no= Entry(self.bottom,  width="60",)
     e_acc_no.place(x=320, y=55)

     lb= Entry(self.bottom, width="60" )
     lb.place(x=320 , y= 110)
    
     
     self.submit= Button(self.bottom, text=" Submit ",bg = "light blue", font="helvetica 15 bold", width="52", command=sub)
     self.submit.place(x=45 , y=180)
     self.back_btn = Button(self.bottom, text="Back",bg= "red" ,font="helvetica 15 bold", width="20", command=go_back)
     self.back_btn.place(x=45, y=230)

def main():
    root = Tk()
    app=Appli(root)
    root.geometry("700x400+200+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()


if __name__ == "__main__":
    main()
