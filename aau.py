from tkinter import *
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql



class Appli(object):
  def __init__(self, master):
     self.master=master
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

     self.heading= Label(self.top, text="All Active Management Users", font="helvetica 18 bold", bg="#f4f5f5")
     self.heading.place(x= 185, y=30)

     #bottom Frame Design

     #list
     lb= Listbox(self.bottom,height="35", width="110" )
     lb.place(x=20 , y= 20)

     con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
     cursor= con.cursor()
     cursor.execute("select * from users ")
     myresult = cursor.fetchall()
     for x in myresult:
         lb.insert(1, "User Id:  - "+ x[0]+"       Password:  - "+ x[1])
     cursor.execute("commit")
     con.close()

     

def main():
    root = Tk()
    app=Appli(root)
    root.geometry("700x700+300+0")
    root.resizable(height = 0, width = 0)
    root.mainloop()



if __name__ == "__main__":
    main()
