from tkinter import *
root=Tk()
def selection():
    selection="you selected the opition"+str(var).get()
    l1.config(text=selection)
def getvals():
    print("Accepted")
Label(root,text="ITVOYAGERS REGISTRATION FORM",bg="blue",fg="white",font="arial 15").grid(row=0,columnspan=3,sticky=W)

name=Label(root,text="Name of Visitor",fg="blue",font="verdana").grid(row=1,column=1,sticky=W)
language=Label(root,text="Favourite Programming Language",fg="blue",font="verdana").grid(row=2,column=1,sticky=W)
gender=Label(root,text="Gender",fg="blue",font="verdana").grid(row=3,column=1,sticky=W)
add=Label(root,text="Address",fg="blue",font="verdana").grid(row=5,column=1,sticky=W)
email=Label(root,text="Email id",fg="blue",font="verdana").grid(row=6,column=1,sticky=W)
phone=Label(root,text="Contact no",fg="blue",font="verdana").grid(row=7,column=1,sticky=W)
country=Label(root,text="Country",fg="blue",font="verdana").grid(row=8,column=1,sticky=W)
state=Label(root,text="State",fg="blue",font="verdana").grid(row=9,column=1,sticky=W)
topic=Label(root,text="Select topic you wish to learn",fg="blue",font="verdana").grid(row=10,column=1,sticky=W)
var=IntVar()

nameentry=Entry(root).grid(row=1,column=2,sticky=W)
languageentry=Entry(root).grid(row=2,column=2,sticky=W)
genderentry=Radiobutton(root,text="Male",variable=var,value=1,command=selection).grid(row=3,column=2,sticky=W)
genderentry1=Radiobutton(root,text="Female",variable=var,value=1,command=selection).grid(row=4,column=2,sticky=W)
addentry=Text(root,height=5,width=10)
addentry.insert(INSERT,"Eit Here")
addentry.grid(row=5,column=2,sticky=W)
emailentry=Entry(root).grid(row=6,column=2,sticky=W)
phoneentry=Entry(root).grid(row=7,column=2,sticky=W)
countryentry=Entry(root).grid(row=8,column=2,sticky=W)
stateentry=Entry(root).grid(row=9,column=2,sticky=W)
var1=IntVar()
var2=IntVar()
topicentry=Checkbutton(root,text="Python",variable=var1).grid(row=10,column=2,sticky=W)
topicentry2=Checkbutton(root,text="Business Intelligence",variable=var2).grid(row=11,column=2,sticky=W)

Button(root,text="REGISTER HERE",command=display,fg="blue").grid(row=12,column=2,stiky=W)


