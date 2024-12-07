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
def upd():
    call(["python", "upd_acc.py"])        

date = datetime.datetime.now().date()
date= str(date)



class Appli(object):
  def __init__(self, master):
     self.master=master

     #frames

     self.top= Frame(master, height=100 , bg= "#f4f5f5")
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

     self.date_lbl = Label(self.bottom, text="Date : "+date, bg="#8e9b96")
     self.date_lbl.place(x=500, y=20)


     self.wlc_lbl = Label(self.bottom, text="Welcome User", bg="#8e9b96", font="helvetica 18 bold")
     self.wlc_lbl.place(x=210, y=42)

     #buttons

     #Balance enquiry
     self.Be= Button(self.bottom, text=" Balance Enquiry ", font="helvetica 13 bold", command=balq, width=20)
     self.Be.place(x=80, y=100)
     self.be_lbl = Label(self.bottom, text="> Check Account Balance", bg="#8e9b96", font="helvetica 13 bold")
     self.be_lbl.place(x=320, y=102)






def main():
    root = Tk()
    app=Appli(root)
    root.geometry("600x260+100+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()


if __name__ == "__main__":
    main()
