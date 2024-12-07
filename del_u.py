from tkinter import *
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql



class Appli(object):
  def __init__(self, master):
     self.master=master
     def delti():
         user= StringVar()
         user = (e_user.get())
         mode= (i.get())
         if (user == "" ):
             MessageBox.showinfo("ID is required for delete", "All Fields are Required")    
         else:
             if( mode == "2" ):
                 con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
                 cursor= con.cursor()
                 cursor.execute("delete from mgmt where managerid='" + user + "'")
                 myresult = cursor.fetchall()
                 for x in myresult:
                     lb.delete(1,"end" )
                     lb.delete(2,"end")
                     lb.delete(3,"end")
                     lb.delete(4,"end")
                     MessageBox.showinfo("Sucessful", "User has been Deleted")
                 cursor.execute("commit")
                 con.close()
             else:
                 if( mode == "3"):
                     con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
                     cursor= con.cursor()
                     cursor.execute("delete from users where idusers='" + user + "'")
                     myresult = cursor.fetchall()
                     for x in myresult:
                         lb.delete(1,"end" )
                         lb.delete(2,"end")
                         lb.delete(3,"end")
                         lb.delete(4,"end")
                         MessageBox.showinfo("Sucessful", "User has been Deleted")
                     cursor.execute("commit")
                     con.close()

     def sub():
         user= StringVar()
         user = (e_user.get())
         mode= (i.get())

         if (user == "" ):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
         else:
             if( mode == "2" ):
                 con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
                 cursor= con.cursor()
                 cursor.execute("select * from mgmt where managerid='" + user + "'")
                 myresult = cursor.fetchall()
                 for x in myresult:
                     lb.insert(1,"User ID :" )
                     lb.insert(2,x[0])
                     lb.insert(3,"Password:")
                     lb.insert(4,x[1])
                 cursor.execute("commit")
                 con.close()
             else:
                 if( mode == "3"):
                     con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
                     cursor= con.cursor()
                     cursor.execute("select * from users where idusers='" + user + "'")
                     myresult = cursor.fetchall()
                     for x in myresult:
                         lb.insert(1,"User ID :" )
                         lb.insert(2,x[0])
                         lb.insert(3,"Password:")
                         lb.insert(4,x[1])
                     cursor.execute("commit")
                     con.close()

             

             


     #frames

     self.top= Frame(master, height=100 , bg= "#f4f5f5")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=800, bg="#8e9b96")
     self.bottom.pack(fill=X)

     #top Frame design
     #self.top_image=PhotoImage(file='icon/money.png')
     #self.top_image_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image_lable.place(x=50, y=15)

     #self.top_image2=PhotoImage(file='icon/money.png')
     #self.top_image2_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image2_lable.place(x=580, y=15)

     self.heading= Label(self.top, text="Delete User", font="helvetica 18 bold", bg="#f4f5f5")
     self.heading.place(x= 285, y=30)

     #bottom Frame Design

     #buttons and lables
     user_lbl = Label(self.bottom, text="User Name : ", font="helvetica 14 bold", bg="#8e9b96")
     user_lbl.place(x=90, y=55)

     i= StringVar()
     Radiobutton(self.bottom, text="Bank Staff",  value="2", bg="#8e9b96", variable=i).place(x=380, y=110)
     Radiobutton(self.bottom, text="Customer",  value="3", bg="#8e9b96", variable=i).place(x=520, y=110)

     #Enteries
     user= StringVar()
     e_user= Entry(self.bottom, width= "60", textvariable=user)
     e_user.place(x=320, y=55)


     #list
     lb= Listbox(self.bottom,height="20", width="60" )
     lb.place(x=320 , y= 180)



     #submit
     self.submit= Button(self.bottom, text=" Submit ", font="helvetica 15 bold", width="20", command=sub)
     self.submit.place(x=45 , y=200)

     self.delt= Button(self.bottom, text=" Delete ", font="helvetica 15 bold", width="20", command=delti)
     self.delt.place(x=45 , y=300)
     

def main():
    root = Tk()
    app=Appli(root)
    root.geometry("700x500+200+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()



if __name__ == "__main__":
    main()
