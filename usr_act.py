from tkinter import *
import datetime
import os
from subprocess import call

def create_uac():
    call(["python", "crt_usr.py"])
def del_u():
    call(["python", "del_u.py"])
def upd_pass():
    call(["python", "cp_adm.py"])
def aam():
    call(["python", "aam.py"])
def aau():
    call(["python", "aau.py"])
def aaa():
    call(["python", "bal_dep.py"])         

date = datetime.datetime.now().date()
date= str(date)



class Appli(object):
  def __init__(self, master):
     self.master=master

     #frames

     self.top= Frame(master, height=100 , bg= "#f4f5f5")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=600, bg="#8e9b96")
     self.bottom.pack(fill=X)

     #top Frame design
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

     #buttons

     #Create User Account
     self.ca= Button(self.bottom, text=" Create User ", font="helvetica 13 bold", command=create_uac, width=20)
     self.ca.place(x=40, y=50)
     self.ca_lbl = Label(self.bottom, text="> Create new user ", bg="#8e9b96", font="helvetica 13 bold")
     self.ca_lbl.place(x=280, y=52)

     #Delete an User
     self.Be= Button(self.bottom, text=" Delete User ", font="helvetica 13 bold", command=del_u, width=20)
     self.Be.place(x=40, y=120)
     self.be_lbl = Label(self.bottom, text="> Delete user access", bg="#8e9b96", font="helvetica 13 bold")
     self.be_lbl.place(x=280, y=122)

     #Update password
     self.Caa= Button(self.bottom, text=" Update User password ", font="helvetica 13 bold", command=upd_pass, width=20)
     self.Caa.place(x=40, y=190)
     self.caa_lbl = Label(self.bottom, text="> Update User Access Password", bg="#8e9b96", font="helvetica 13 bold")
     self.caa_lbl.place(x=280, y=192)

     #Check all Active Management
     self.Bw= Button(self.bottom, text=" Active Management ", font="helvetica 13 bold", command=aam, width=20)
     self.Bw.place(x=40, y=260)
     self.bw_lbl = Label(self.bottom, text="> Check All active Management User", bg="#8e9b96", font="helvetica 13 bold")
     self.bw_lbl.place(x=280, y=262)

     #Check all Active Users
     self.Bd= Button(self.bottom, text=" Active User ", font="helvetica 13 bold", command=aau, width=20)
     self.Bd.place(x=40, y=330)
     self.bd_lbl = Label(self.bottom, text="> Check all Active Customer Access", bg="#8e9b96", font="helvetica 13 bold")
     self.bd_lbl.place(x=280, y=332)

     #Check all Active Accounts
     self.Au= Button(self.bottom, text=" Active Accounts ", font="helvetica 13 bold", command=aaa, width=20)
     self.Au.place(x=40, y=400)
     self.bd_lbl = Label(self.bottom, text="> Check all Active Accounts", bg="#8e9b96", font="helvetica 13 bold")
     self.bd_lbl.place(x=280, y=402)




def main():
    root = Tk()
    app=Appli(root)
    root.geometry("600x570+150+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()


if __name__ == "__main__":
    main()
