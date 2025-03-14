from tkinter import *
import datetime
import os
from subprocess import call

def create_acc():
    call(["python", "create_acc.py"])       
def delt_acc():
    call(["python", "delt.py"])
def balq():
    call(["python", "bal_eq.py"])
def chk():
    call(["python", "chk_acc.py"])
def bw():
    call(["python", "bal_wd.py"])
def bd():
    call(["python", "bal_dep.py"])
def bd():
    call(["python", "Fdr.py"])
def upd():
    call(["python", "upd_acc.py"])        

date = datetime.datetime.now().date()
date= str(date)



class Appli(object):
  def __init__(self, master):
     self.master=master

     

     self.top= Frame(master, height=100 , bg= "#f4f5f5")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=530, bg="#8e9b96")
     self.bottom.pack(fill=X)

     
     #self.top_image=PhotoImage(file='icon/money.png')
     #self.top_image_lable= Label(self.top, image=self.top_image, bg="white")
     #self.top_image_lable.place(x=70, y=15)

     #self.top_image2=PhotoImage(file='icon/money.png')
     #self.top_image2_lable= Label(self.top, image=self.top_image, bg="white")
     #self.top_image2_lable.place(x=480, y=15)

     self.heading= Label(self.top, text="Bank Management System", font="helvetica 15 bold", bg="#f4f5f5")
     self.heading.place(x= 180, y=30)

     self.date_lbl = Label(self.bottom, text="Date : "+date, bg="#8e9b96")
     self.date_lbl.place(x=500, y=20)

     

     
     self.ca= Button(self.bottom, text=" Create Account ", font="helvetica 13 bold", command=create_acc, width=20)
     self.ca.place(x=40, y=50)
     self.ca_lbl = Label(self.bottom, text="> Create new user account", bg="#8e9b96", font="helvetica 13 bold")
     self.ca_lbl.place(x=280, y=52) 

     
     self.Be= Button(self.bottom, text=" Balance Enquiry ", font="helvetica 13 bold", command=balq, width=20)   # button widget 
     self.Be.place(x=40, y=120)                                      
     self.be_lbl = Label(self.bottom, text="> Check Account Balance", bg="#8e9b96", font="helvetica 13 bold") 
     self.be_lbl.place(x=280, y=122)       # self.be_lbl  .. label widget ,displays side text 

     
     self.Caa= Button(self.bottom, text=" Check Account Details ", font="helvetica 13 bold", command=chk, width=20)
     self.Caa.place(x=40, y=190)
     self.caa_lbl = Label(self.bottom, text="> Check account details", bg="#8e9b96", font="helvetica 13 bold")
     self.caa_lbl.place(x=280, y=192)

     
     self.Bw= Button(self.bottom, text=" Balance Withdraw ", font="helvetica 13 bold", command=bw, width=20)
     self.Bw.place(x=40, y=260)
     self.bw_lbl = Label(self.bottom, text="> Withdraw Amount from user Account", bg="#8e9b96", font="helvetica 13 bold")
     self.bw_lbl.place(x=280, y=262)

     
     self.Bd= Button(self.bottom, text=" Balance Deposit ", font="helvetica 13 bold", command=bd, width=20)
     self.Bd.place(x=40, y=340)
     self.bd_lbl = Label(self.bottom, text="> Deposit Amount from user Account", bg="#8e9b96", font="helvetica 13 bold")
     self.bd_lbl.place(x=280, y=342)

     
     self.Au= Button(self.bottom, text=" Delete Account ", font="helvetica 13 bold", command=delt_acc, width=20)
     self.Au.place(x=40, y=410)
     self.bd_lbl = Label(self.bottom, text="> Delete user Account", bg="#8e9b96", font="helvetica 13 bold")
     self.bd_lbl.place(x=280, y=412)
      
     self.Au= Button(self.bottom, text=" Update Account ", font="helvetica 13 bold", command=upd, width=20)
     self.Au.place(x=40, y=480)
     self.bd_lbl = Label(self.bottom, text="> Update user Account", bg="#8e9b96", font="helvetica 13 bold")
     self.bd_lbl.place(x=280, y=482)



def main():
    root = Tk()
    app=Appli(root)
    root.geometry("600x630+100+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()


if __name__ == "__main__":
    main()
