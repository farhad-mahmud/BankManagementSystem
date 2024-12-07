
from tkinter import *
import datetime
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql


            

date = datetime.datetime.now().date()
date= str(date)



class Appli(object):
  def __init__(self, master):
     self.master=master
     def sub():
         user= StringVar()
         opassw= StringVar()
         npassw= StringVar()
         user= (e_user.get())
         opassw=(e_opass.get())
         npassw=(e_npass.get())
         mode= (i.get())
         if (user == "" or opassw == "" or npassw == "" ):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")
         else:
             if (mode == "2"):
                 con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
                 cursor= con.cursor()
                 cursor.execute("select * from mgmt where managerid='" + user + "'")
                 myresult = cursor.fetchall()
                 for x in myresult:
                     uchk=x[0]
                     pchk=x[1]
                     if (user == uchk and opassw == pchk):
                         con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
                         cursor= con.cursor()
                         cursor.execute("insert into mgmt values('" + user + "','"+ npassw +"')")
                         cursor.execute("commit")
                         MessageBox.showinfo("Sucessful", "Password Changed")
                     else:
                         MessageBox.showinfo("Illegal Insert", "Wrong password")
             else:
                 if (mode == "3"):
                     con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
                     cursor= con.cursor()
                     cursor.execute("select * from users where idusers='" + user + "'")
                     myresult = cursor.fetchall()
                     for x in myresult:
                         uchk=x[0]
                         pchk=x[1]
                         if (user == uchk and opassw == pchk):
                             con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
                             cursor= con.cursor()
                             cursor.execute("insert into idusers values('" + user + "','"+ npassw +"')")
                             cursor.execute("commit")
                             MessageBox.showinfo("Sucessful", "Password Changed")
                         else:
                             MessageBox.showinfo("Illegal Insert", "Wrong password")




                          




     #frames

     self.top= Frame(master, height=140 , bg= "#f4f5f5")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=530, bg="#8e9b96")
     self.bottom.pack(fill=X)

     #top Frame design
     #self.top_image=PhotoImage(file='icon/money.png')
     #self.top_image_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image_lable.place(x=70, y=15)

     #self.top_image2=PhotoImage(file='icon/money.png')
     #self.top_image2_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image2_lable.place(x=480, y=15)

     self.heading= Label(self.top, text="Bank Management System", font="helvetica 15 bold", bg="#f4f5f5")
     self.heading.place(x= 180, y=30)
     self.heading= Label(self.top, text="Change User Password", font="helvetica 19 bold", bg="#f4f5f5")
     self.heading.place(x= 170, y=90)

     self.date_lbl = Label(self.bottom, text="Date : "+date, bg="#8e9b96")
     self.date_lbl.place(x=500, y=20)

     #Lable and Enteries
     self.user_lbl = Label(self.bottom, text="Username : ", bg="#8e9b96", font="helvetica 15 bold")
     self.user_lbl.place(x=70, y=70)

     self.oppass_lbl = Label(self.bottom, text="Old Password : ", bg="#8e9b96", font="helvetica 15 bold")
     self.oppass_lbl.place(x=70, y=150)

     self.nppass_lbl = Label(self.bottom, text="New Password : ", bg="#8e9b96", font="helvetica 15 bold")
     self.nppass_lbl.place(x=70, y=230)

     e_user= Entry(self.bottom, width= "40")
     e_user.place(x=270, y=75)

     e_opass= Entry(self.bottom, width= "40")
     e_opass.place(x=270, y=155)

     e_npass= Entry(self.bottom, width= "40")
     e_npass.place(x=270, y=235)

     i= StringVar()
     Radiobutton(self.bottom, text="Bank Staff",  value="2", bg="#8e9b96", variable=i).place(x=175, y=300)
     Radiobutton(self.bottom, text="Customer",  value="3", bg="#8e9b96", variable=i).place(x=345, y=300)

     # submit
     self.submit= Button(self.bottom, text=" Submit ", font="helvetica 15 bold", width="30", command=sub)
     self.submit.place(x=105 , y=365)


   



def main():
    root = Tk()
    app=Appli(root)
    root.geometry("600x580+200+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()


if __name__ == "__main__":
    main()
