from tkinter import *
from PIL import ImageTk,Image
import sqlite3 

root=Tk()
root.title("Bk.Main")
root.iconbitmap("1.ico")
root.geometry("400x450")
root.minsize(400,450)
root.maxsize(400,450)

a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()


def login_show():
    db=sqlite3.connect("simple_login.db")
    cr=db.cursor()
    cr.execute("insert into login values('"+a.get()+"','"+b.get()+"')")
    db.commit()
    db.close()
    a.set("")
    b.set("")
            
def register_show():
    db=sqlite3.connect("simple_login.db")
    cr=db.cursor()
    cr.execute("insert into register values('"+a.get()+"','"+b.get()+"','"+c.get()+"','"+d.get()+"','"+e.get()+"')")
    db.commit()
    db.close()
    a.set("")
    b.set("")
    c.set("")
    d.set("")
    e.set("")
    
    

def login():
    root.title("Bk.Login")
    f1=Frame(bg="thistle2")
    f1.place(width=400,height=450)

    b2=Button(f1,text="Back",command=main)
    b2.pack(anchor="sw",padx=10,pady=5)

    l1=Label(f1,text="@Login Form!",font=",15,")
    l1.place(x=150,y=50)

    l2=Label(f1,text="Enter User Name")
    l2.place(x=70,y=110)
    e1=Entry(f1,textvariable=a)
    e1.place(x=195,y=110)

    l3=Label(f1,text="Enter Your Password")
    l3.place(x=70,y=150)
    e2=Entry(f1,show="*",textvariable=b )
    e2.place(x=195,y=150)

    b0=Button(f1,text="Cancel",command=main)
    b0.place(x=195,y=200)
    b1=Button(f1,text="Submit",command=login_show)
    b1.place(x=250,y=200)
    
    l0=Label(f1,text="Created by BHAVYESH.K.PAGHDAR")
    l0.pack(side=BOTTOM)
    
def register():
    root.title("Bk.Register")
    
    f2=Frame(bg="thistle2")
    f2.place(width=400,height=450)

    b2=Button(f2,text="Back",command=main)
    b2.pack(anchor="sw",padx=10,pady=5)

    l0=Label(f2,text="@Registration Form!",font=",15,")
    l0.place(x=120,y=50)

    l1=Label(f2,text="Enter Your Name")
    l1.place(x=70,y=110)
    e1=Entry(f2,textvariable=a)
    e1.place(x=195,y=110)

    l2=Label(f2,text="Enter User Name")
    l2.place(x=70,y=150)
    e2=Entry(f2,textvariable=b)
    e2.place(x=195,y=150)

    l3=Label(f2,text="Enter Your Email-ID")
    l3.place(x=70,y=190)
    e3=Entry(f2,textvariable=c)
    e3.place(x=195,y=190)

    l4=Label(f2,text="Enter Your Password")
    l4.place(x=70,y=230)
    e4=Entry(f2,show="*",textvariable=d)
    e4.place(x=195,y=230)

    l4=Label(f2,text="Confirm Password")
    l4.place(x=70,y=270)
    e4=Entry(f2,show="*",textvariable=e)
    e4.place(x=195,y=270)

    b0=Button(f2,text="Cancel",command=main)
    b0.place(x=195,y=325)
    
    b1=Button(f2,text="Submit",command=register_show)
    b1.place(x=250,y=325)

    l5=Label(f2,text="Created by BHAVYESH.K.PAGHDAR")
    l5.pack(side=BOTTOM)

def main():
    
   
    f0=Frame(bg="thistle2")
    f0.place(width=400,height=450)

    l0=Label(f0,text="Created by BHAVYESH.K.PAGHDAR")
    l0.pack(side=BOTTOM)
    

    l1=Label(f0,text="If You Have An Account!")
    l1.place(x=125,y=100)
    b1=Button(f0,text="Login",command=login)
    b1.place(x=175,y=125)

    l2=Label(f0,text="If You Don't Have An Account!")
    l2.place(x=110,y=175)
    b2=Button(f0,text="Register",command=register)
    b2.place(x=170,y=200)

main()


root.mainloop()
