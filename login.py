from tkinter import *
import datetime
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql
import sys

#pyinstaller --onefile --add-data "bal_dep.py;." --add-data "bal_eq.py;." --add-data "bal_wd.py;." --add-data "chk_acc.py;." --add-data "create_acc.py;." --add-data "Admin_bal_dep.py;." --add-data "Admin_bal_eq.py;." --add-data "Admin_bal_wd.py;." --add-data "Admin_check_acc.py;." --add-data "Admin_delete_acc.py;." --add-data "Admin_fdr.py;." --add-data "Admin_loan.py;." --add-data "mainadmin.py;." --add-data "mainmanage.py;." --add-data "mainuser.py;." --add-data "upd_acc.py;." --add-data "Fdr.py;." --add-data "loan.py;." --noconsole login.py           

date = datetime.datetime.now().date()
date= str(date)

global user

class Appli(object):
  def __init__(self, master):
     self.master=master
     user = sys.argv[1] if len(sys.argv) > 1 else ""
     def sub():
         #user= StringVar()
         user= (userval.get())      # to fetch username and pass from entry fields
         passw=(e_pass.get())      #  
         mode= (i.get())
         if (user == "" or passw == "" ):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")
         else: 
             if (mode == "1"):
                 if ( user == "admin" and passw == "admin"):
                     MessageBox.showinfo("Successful", "Welcome Admin")
                     call(["python", "mainadmin.py",user])        #entering mainadmin page 
                     quit()
                 else:
                     MessageBox.showinfo("Illegal insert", "Username or Password Is Wrong")
             else:
                 if(mode == "2"):
                     con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
                     cursor= con.cursor()
                     cursor.execute("SELECT * FROM mgmt WHERE managerid = %s", (user,))

                     myresult = cursor.fetchall()
                     for x in myresult:
                         uchk=x[0]
                         pchk=x[1]
                         if (user == uchk and passw == pchk):
                             MessageBox.showinfo("Sucessful", "Welcome Management Staff")
                             call(["python", "mainmanage.py"])     #enters mainmanage page 
                             quit() 
                         else:
                             MessageBox.showinfo("Login Error", "Invalid Username or Password")
                 else:
                     if (mode== "3"):
                             con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
                             cursor= con.cursor()
                             cursor.execute("SELECT * FROM users WHERE acc_no = %s", (user,))

                             myresult = cursor.fetchall()
                             for x in myresult:
                                 uchk=x[0]
                                 pchk=x[2]
                                 if (user == uchk and passw == pchk):
                                     MessageBox.showinfo("Sucessful", "Welcome Customer")
                                     
                                     call(["python", "mainuser.py",user])    #enters mainusers page
                                     #call(["python", "bal_dep.py", user])  # Pass the user as an argument
                                     
                                     
                                 else:
                                     MessageBox.showinfo("Login Error", "Invalid Username or Password")


     self.top= Frame(master, height=140 , bg= "#f4f5f5")
     self.top.pack(fill=X) 

     self.bottom= Frame(master, height=530, bg="#8e9b96")
     self.bottom.pack(fill=X)

     
     #self.top_image=PhotoImage(file=r'c:\Users\ASUS\Downloads\file.png')
     #self.top_image_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image_lable.place(x=0.001, y=3)

     #self.top_image2=PhotoImage(file=r'c:\Users\ASUS\Downloads\file.png')
     #self.top_image2_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image2_lable.place(x=400, y=3)

     self.heading= Label(self.top, text="BANK MANAGEMENT SYSTEM", font="Helvetica 15 bold", bg="#f4f5f5")
     self.heading.place(x= 180, y=30)
     self.heading= Label(self.top, text="LOGIN", font="Helvetica 19 bold", bg="#f4f5f5")
     self.heading.place(x= 270, y=90)

     self.date_lbl = Label(self.bottom, text="Date : "+date, bg="#8e9b96")
     self.date_lbl.place(x=500, y=20) 
  
     
     
     self.user_lbl = Label(self.bottom, text="USERNAME OR A/C: ", bg="#8e9b96", font="Helvetica 15 bold")
     self.user_lbl.place(x=30, y=100)

     self.pass_lbl = Label(self.bottom, text="PASSWORD            : ", bg="#8e9b96", font="helvetica 15 bold")
     self.pass_lbl.place(x=30, y=180)
     
     userval= StringVar()
     userval.set(user)
     e_user= Entry(self.bottom,textvariable=userval, width= "40")
     e_user.place(x=240, y=105)
     
     e_pass= Entry(self.bottom, width= "40")
     e_pass.place(x=240, y=185)

     i= StringVar()
     Radiobutton(self.bottom, text="Administrator",  value="1", bg="#8e9b96", variable=i).place(x=180, y=260)
     #Radiobutton(self.bottom, text="Bank Staff",  value="2", bg="#8e9b96", variable=i).place(x=255, y=260)
     Radiobutton(self.bottom, text="Customer",  value="3", bg="#8e9b96", variable=i).place(x=300, y=260)

    
     self.submit= Button(self.bottom, text=" LOG IN  ", font="Helvetica 15 bold", width="30", command=sub)
     self.submit.place(x=105 , y=335)


   



def main():
    root = Tk()
    app=Appli(root)
    root.geometry("600x580+200+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()


if __name__ == "__main__":
    main()
