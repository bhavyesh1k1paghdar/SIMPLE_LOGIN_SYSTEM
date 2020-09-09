from tkinter import *
root=Tk()
root.title("Bk.Login")
root.geometry("400x450")
root.minsize(400,450)
root.maxsize(400,450)

l0=Label(root,text="@Login Form!",font=",20,",pady=40)
l0.grid(row=1,column=0,columnspan=1)

l1=Label(root,text="Enter User Name",padx=30,pady=25)
l1.grid(row=2,column=0,sticky=W)
e1=Entry(root)
e1.grid(row=2,column=2)

l2=Label(root,text="Enter Your Password",padx=30,pady=25)
l2.grid(row=4,column=0)
e2=Entry(root,show="*")
#show used for how your enter value is look like.
e2.grid(row=4,column=2)

b0=Button(root,text="Cancel")
b0.grid(row=5,column=1)
b1=Button(root,text="Submit")
b1.grid(row=5,column=2)
#columnspan=0 is not valid.
#columnspan is used for murge two column in one single column.

root.mainloop()
 
