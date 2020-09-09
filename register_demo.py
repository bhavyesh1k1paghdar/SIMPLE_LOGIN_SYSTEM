from tkinter import *
root=Tk()
root.title("Bk.Register")
root.geometry("400x450")
root.minsize(400,450)
root.maxsize(400,450)

l0=Label(root,text="@Registration Form!",font=",20,",pady=40)
l0.grid(row=1,column=0,columnspan=1)


l1=Label(root,text="Enter Your Name",padx=30,pady=20)
l1.grid(row=2,column=0,sticky=W)
e1=Entry(root)
e1.grid(row=2,column=2)

l2=Label(root,text="Enter User Name",padx=30,pady=20)
l2.grid(row=3,column=0,sticky=W)
e2=Entry(root)
e2.grid(row=3,column=2)

l3=Label(root,text="Enter Your Email-ID",padx=30,pady=20)
l3.grid(row=4,column=0,sticky=W)
e3=Entry(root)
e3.grid(row=4,column=2)

l4=Label(root,text="Enter Your Password",padx=30,pady=20)
l4.grid(row=5,column=0)
e4=Entry(root,show="*")
e4.grid(row=5,column=2)

b0=Button(root,text="Cancel")
b0.grid(row=8,column=1)
b1=Button(root,text="Submit")
b1.grid(row=8,column=2)
root.mainloop()
 
