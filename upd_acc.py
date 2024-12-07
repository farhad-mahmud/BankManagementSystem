from tkinter import *
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql



class Appli(object):
  def __init__(self, master):
     self.master=master

     def sub():
         acc_no= DoubleVar()
         acc_no = (e_acc_no.get())

         if (acc_no == "" ):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
         else:
             con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
             cursor= con.cursor()
             cursor.execute("update acct set fname= '"+ e_fname.get() +"' ,lname= '"+ e_lname.get() +"',d_ob= '"+ e_d_ob.get() +"' , s_c= '"+ e_s_c.get() +"' , amount= '" + e_amount.get() + "',address= '"+ e_address.get() +"' , phone_no= '"+ e_phone_no.get() +"' ,m_f_t= '"+ e_m_f_t.get() +"'  where acc_no='" + acc_no + "'")
             MessageBox.showinfo("Update status", "Updated Sucessfully")               
             cursor.execute("commit")
             con.close()
             

             


     #frames

     self.top= Frame(master, height=100 , bg= "#f4f5f5")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=900, bg="#8e9b96")
     self.bottom.pack(fill=X)

     #top Frame design
     #self.top_image=PhotoImage(file='icon/money.png')
     #self.top_image_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image_lable.place(x=50, y=15)

     #self.top_image2=PhotoImage(file='icon/money.png')
     #self.top_image2_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image2_lable.place(x=630, y=15)

     self.heading= Label(self.top, text="Check Account Details", font="helvetica 18 bold", bg="#f4f5f5")
     self.heading.place(x= 255, y=30)

     #bottom Frame Design

     #buttons and lables
     acc_no= DoubleVar()
     acc_no = Label(self.bottom, text="Account number ", font="helvetica 14 bold", bg="#8e9b96")
     acc_no.place(x=40, y=40)

     fname = Label(self.bottom, text="First Name ", font="helvetica 14 bold", bg="#8e9b96")
     fname.place(x=40, y=95)

     lname = Label(self.bottom, text="Last Name ", font="helvetica 14 bold", bg="#8e9b96")
     lname.place(x=40, y=150)

     s_c = Label(self.bottom, text="Account Type ", font="helvetica 14 bold", bg="#8e9b96")
     s_c.place(x=40, y=205)

     amount= DoubleVar()
     amount = Label(self.bottom, text="New Amount ", font="helvetica 14 bold", bg="#8e9b96")
     amount.place(x=40, y=260)

     address = Label(self.bottom, text="Address ", font="helvetica 14 bold", bg="#8e9b96")
     address.place(x=40, y=315)
     
     phone_no= DoubleVar()
     phone_no = Label(self.bottom, text="Phone Number ", font="helvetica 14 bold", bg="#8e9b96")
     phone_no.place(x=40, y=370)

     m_f_t = Label(self.bottom, text="Sex ", font="helvetica 14 bold", bg="#8e9b96")
     m_f_t.place(x=40, y=425)

     d_ob= Label(self.bottom, text="Date of Birth", font="helvetica 14 bold", bg="#8e9b96")
     d_ob.place(x=40,y=475)

     #Enteries
     
     e_acc_no= Entry(self.bottom, width= "40")
     e_acc_no.place(x=320, y=40)

     e_fname= Entry(self.bottom, width= "40")
     e_fname.place(x=320, y=95)

     e_lname= Entry(self.bottom, width= "40")
     e_lname.place(x=320, y=150)

     e_s_c= Entry(self.bottom, width= "40")
     e_s_c.place(x=320, y=205)

     e_amount= Entry(self.bottom, width= "40")
     e_amount.place(x=320, y=260)

     e_address= Entry(self.bottom, width= "40")
     e_address.place(x=320, y=315)
     
     e_phone_no= Entry(self.bottom, width= "40")
     e_phone_no.place(x=320, y=370)

     e_m_f_t= Entry(self.bottom, width= "40" )
     e_m_f_t.place(x=320, y=425)

     e_d_ob= Entry(self.bottom, width= "40" )
     e_d_ob.place(x=320, y=475)

     

     #Enteries
     

     #submit
     self.submit= Button(self.bottom, text=" Submit ", font="helvetica 15 bold", width="10", command=sub)
     self.submit.place(x=600 , y=55)

     self.qt= Button(self.bottom, text=" Quit", font="helvetica 15 bold", width="10", command=quit)
     self.qt.place(x=600 , y=200)

     

def main():
    root = Tk()
    app=Appli(root)
    root.geometry("750x650+200+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()



if __name__ == "__main__":
    main()
