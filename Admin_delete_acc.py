from tkinter import *
import os
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql



class Appli(object):
  def __init__(self, master):
     self.master=master
     def go_back():
         self.master.destroy()
     def delti():
         acc_no= DoubleVar()
         acc_no = (e_acc_no.get())

         if (acc_no == "" ):
             MessageBox.showinfo("ID is required for delete", "All Fields are Required")    
         else:
             con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
             cursor= con.cursor()
             cursor.execute("delete from acct where acc_no='" + acc_no + "'")
             cursor.execute("commit")
             lb.delete(1,'end')
             lb.delete(2,'end')
             lb.delete(3,'end')
             lb.delete(4,'end')
             lb.delete(5,'end')
             lb.delete(6,'end')
             lb.delete(7,'end')
             lb.delete(8,'end')
             lb.delete(9,'end')
             lb.delete(10,'end')
             lb.delete(11,'end')
             lb.delete(12,'end')
             lb.delete(13,'end')
             lb.delete(14,'end')
             e_acc_no.delete(0,'end')
             MessageBox.showinfo("Delete Status", "Deleted Successfully")
             con.close()

     def sub():
         acc_no= DoubleVar()
         acc_no = (e_acc_no.get())

         if (acc_no == "" ):
             MessageBox.showinfo("Illegal insert", "All Fields are Required")    
         else:
             con=mysql.connect(host= "localhost", user="root" , password="donotrootfarhad", database="bank_data")
             cursor= con.cursor()
             cursor.execute("select * from acct where acc_no='" + acc_no + "'")
             myresult = cursor.fetchall()
             print(myresult)
             for x in myresult:
                 lb.insert(1,"Account No. :" )
                 lb.insert(2,x[0])
                 lb.insert(3,"Name :")
                 lb.insert(4,x[1] + " " + x[2])
                 lb.insert(5,"Account Type :")
                 lb.insert(6,x[3])
                 lb.insert(7,"Amount :")
                 lb.insert(8,x[4])
                 lb.insert(9,"Address :")
                 lb.insert(10,x[5])
                 lb.insert(11,"Phone No. :")
                 lb.insert(12,x[6])
                 lb.insert(13,"Sex")
                 lb.insert(14,x[7])
                 
             cursor.execute("commit")
             con.close()
             

             


     

     self.top= Frame(master, height=100 , bg= "#f4f5f5")
     self.top.pack(fill=X)

     self.bottom= Frame(master, height=800, bg="#8e9b96")
     self.bottom.pack(fill=X)

     
     #self.top_image=PhotoImage(file='icon/money.png')
     #self.top_image_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image_lable.place(x=50, y=15)

     #self.top_image2=PhotoImage(file='icon/money.png')
      # self.top_image2_lable= Label(self.top, image=self.top_image, bg="#f4f5f5")
     #self.top_image2_lable.place(x=580, y=15)

     self.heading= Label(self.top, text="Delete Account", font="helvetica 18 bold", bg="#f4f5f5")
     self.heading.place(x= 265, y=30)

     

     
     acc_no= DoubleVar()
     acc_no = Label(self.bottom, text="Account number ", font="helvetica 14 bold", bg="#8e9b96")
     acc_no.place(x=40, y=55)

     detail = Label(self.bottom, text="Details -> ", font="helvetica 14 bold", bg="#8e9b96")
     detail.place(x=40, y=110)

    
     
     e_acc_no= Entry(self.bottom, width= "60", textvariable=acc_no)
     e_acc_no.place(x=320, y=55)


     
     lb= Listbox(self.bottom,height="50", width="60" )
     lb.place(x=320 , y= 110)



     
     self.submit= Button(self.bottom, text=" Submit ", font="helvetica 15 bold", width="20", command=sub)
     self.submit.place(x=45 , y=200)

     self.delt= Button(self.bottom, text=" Delete ", font="helvetica 15 bold", width="20", command=delti)
     self.delt.place(x=45 , y=270)

     self.back_btn = Button(self.bottom, text="Back",bg= "red" ,font="helvetica 15 bold", width="20", command=go_back)
     self.back_btn.place(x=45, y=330)

def main():
    root = Tk()
    app=Appli(root)
    root.geometry("700x500+200+20")
    root.resizable(height = 0, width = 0)
    root.mainloop()



if __name__ == "__main__":
    main()
