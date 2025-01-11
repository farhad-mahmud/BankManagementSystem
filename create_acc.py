from tkinter import *
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql
import datetime


date = datetime.datetime.now().date()
date= str(date)

class Appli(object):
  def __init__(self, master):
     self.master=master
     def go_back():
        self.master.destroy()
     def sub():
         acc_no= DoubleVar()
         amount= DoubleVar()
         phone_no= DoubleVar()
         acc_no = (e_acc_no.get())
         fname = (e_fname.get())
         lname = (e_lname.get())
         d_ob= (e_d_ob.get())
         s_c = (t.get())
         amount = (e_amount.get())
         address = (e_address.get())
         phone_no = (e_phone_no.get())
         m_f_t = (i.get())
         password = (e_pass.get())

         if (acc_no == "" or fname == "" or s_c == "" or amount =="" or address =="" or phone_no == "" or m_f_t ==""):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
         else:
             con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
             cursor= con.cursor()
             cursor.execute("insert into acct values('" + acc_no + "','"+ fname +"','"+ lname +"','"+ d_ob +"', '"+ s_c +"','"+ amount +"' , '"+ address +"','" + phone_no + "', '"+ m_f_t +"')")
             cursor.execute("insert into users values('" + acc_no + "','" + phone_no + "','" + password + "')")
             cursor.execute("commit")
             MessageBox.showinfo("Insert Status", "Account Created succesfully")
             e_fname.delete(0,'end')
             e_lname.delete(0,'end')
             e_amount.delete(0,'end')
             e_address.delete(0,'end')
             e_phone_no.delete(0,'end')
             e_d_ob.delete(0,'end')
             e_pass.delete(0,'end')
             con.close()


     

     self.top= Frame(master, height=100 , bg= "#f4f5f5")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=800, bg="#8e9b96")
     self.bottom.pack(fill=X)

     #top Frame design
     #self.top_image=PhotoImage(file='icon/money.png')
     #self.top_image_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image_lable.place(x=100, y=15)

     #self.top_image2=PhotoImage(file='icon/money.png')
     #self.top_image2_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image2_lable.place(x=750, y=15)

     self.heading= Label(self.top, text="Create Account", font="helvetica 18 bold", bg="#f4f5f5")
     self.heading.place(x= 370, y=30)

     

     
     acc_no= DoubleVar()
     acc_no = Label(self.bottom, text="Account Number ", font="helvetica 14 bold", bg="#8e9b96")
     acc_no.place(x=40, y=55)

     fname = Label(self.bottom, text="First Name ", font="helvetica 14 bold", bg="#8e9b96")
     fname.place(x=40, y=110)

     lname = Label(self.bottom, text="Last Name ", font="helvetica 14 bold", bg="#8e9b96")
     lname.place(x=40, y=165)

     s_c = Label(self.bottom, text="Account Type ", font="helvetica 14 bold", bg="#8e9b96")
     s_c.place(x=40, y=220)

     amount= DoubleVar()
     amount = Label(self.bottom, text="Initial Amount ", font="helvetica 14 bold", bg="#8e9b96")
     amount.place(x=40, y=275)

     address = Label(self.bottom, text="Address ", font="helvetica 14 bold", bg="#8e9b96")
     address.place(x=40, y=330)
     
     phone_no= DoubleVar()
     phone_no = Label(self.bottom, text="Phone Number ", font="helvetica 14 bold", bg="#8e9b96")
     phone_no.place(x=40, y=385)

     m_f_t = Label(self.bottom, text="Gender ", font="helvetica 14 bold", bg="#8e9b96")
     m_f_t.place(x=40, y=440)

     d_ob = Label(self.bottom, text="Date of Birth ", font="helvetica 14 bold", bg="#8e9b96")
     d_ob.place(x=40, y=495)

     password = Label(self.bottom, text="Password ", font="helvetica 14 bold", bg="#8e9b96")  # New password field
     password.place(x=40, y=550)
     
     
     e_acc_no= Entry(self.bottom, width= "60", textvariable=acc_no)
     e_acc_no.place(x=320, y=55)

     e_fname= Entry(self.bottom, width= "60")
     e_fname.place(x=320, y=110)

     e_lname= Entry(self.bottom, width= "60")
     e_lname.place(x=320, y=165)

     t= StringVar()
     Radiobutton(self.bottom, text="Savings Account",  value="S", bg="#8e9b96", variable=t).place(x=320, y=220)
     Radiobutton(self.bottom, text="Current Account",  value="C", bg="#8e9b96", variable=t).place(x=450, y=220)

     e_amount= Entry(self.bottom, width= "60")
     e_amount.place(x=320, y=275)

     e_address= Entry(self.bottom, width= "60")
     e_address.place(x=320, y=330)
     
     e_phone_no= Entry(self.bottom, width= "60")
     e_phone_no.place(x=320, y=385)

     i= StringVar()
     Radiobutton(self.bottom, text="Male",  value="M", bg="#8e9b96", variable=i).place(x=320, y=440)
     Radiobutton(self.bottom, text="Female",  value="F", bg="#8e9b96", variable=i).place(x=430, y=440)
     Radiobutton(self.bottom, text="Transgender",  value="T", bg="#8e9b96", variable=i).place(x=540, y=440)

     e_d_ob= Entry(self.bottom, width= "60")
     e_d_ob.place(x=320, y=495)

     e_pass = Entry(self.bottom, width="60", show="*")  # Hide the password input
     e_pass.place(x=320, y=550)

     
     self.submit= Button(self.bottom, text=" Submit ", font="helvetica 15 bold", width="30", command=sub)
     self.submit.place(x=320 , y=600)
     self.back_btn = Button(self.bottom, text="Back", font="helvetica 15 bold", width="20", command=go_back)
     self.back_btn.place(x=25, y=600)
     

def main():
    root = Tk()
    app=Appli(root)
    root.geometry("900x750+200+0")
    root.resizable(height = 0, width = 0)
    root.mainloop()



if __name__ == "__main__":
    main()
