from tkinter import*
root=Tk()
Label(root,text="LabelFrame to custumize GUI from itvoyagers.in",bg="black",fg="orange",font="Consolas 15 bold").grid(row=0,column=0)


#saving user info
window=LabelFrame(root,text="Personal Information",bg="firebrick",fg="white",font="vardhana")
window.grid(row=1,column=0,sticky="news",ipadx=20,ipady=10)

info_frame=Label(window,text="First Name",fg="firebrick",bg="orange",font="vardhana 10 bold",height=1,width=10).grid(row=1,column=0,sticky=W)
w=Entry(window).grid(row=1,column=1,sticky="news",padx=20,pady=10)

info_frame=Label(window,text="Last Name",fg="firebrick",bg="orange",font="vardhana 10 bold",height=1,width=10).grid(row=2,column=0,sticky=W)
w=Entry(window).grid(row=2,column=1,sticky="news",padx=20,pady=10)

info_frame=Label(window,text="gender",fg="firebrick",bg="orange",font="vardhana 10 bold",height=1,width=10).grid(row=3,column=0,sticky=W)
Var1=IntVar()
Var2=IntVar()
w=Radiobutton(window,text="Male",variable=Var1,fg="brown",bg="orange",font="vardhana 10 bold",height=1,width=10).grid(row=3,column=1,sticky="news",padx=30,pady=20)
w=Radiobutton(window,text="Female",variable=Var2,fg="firebrick",bg="orange",font="vardhana 10 bold",height=1,width=10).grid(row=3,column=2,sticky="news",padx=25,pady=20)


#add
window=LabelFrame(root,text="Address",bg="orange",fg="white",font="vardhana")
window.grid(row=2,column=0,sticky="news",ipadx=20,ipady=10)

add_frame=Label(window,text="State",fg="orange",bg="firebrick",font="vardhana 10 bold",height=1,width=10).grid(row=5,column=0,sticky=W)
w=Entry(window).grid(row=5,column=1,sticky="news",padx=20,pady=10)

add_frame=Label(window,text="City",fg="orange",bg="firebrick",font="vardhana 10 bold",height=1,width=10).grid(row=6,column=0,sticky=W)
w=Entry(window).grid(row=6,column=1,sticky="news",padx=20,pady=10)

info_frame=Label(window,text="Street",fg="orange",bg="firebrick",font="vardhana 10 bold",height=1,width=10).grid(row=7,column=0,sticky=W)
w=Entry(window).grid(row=7,column=1,sticky="news",padx=20,pady=10)


add_frame=Label(window,text="Pin Code",fg="orange",bg="firebrick",font="vardhana 10 bold",height=1,width=10).grid(row=8,column=0,sticky=W)
w=Entry(window).grid(row=8,column=1,sticky="news",padx=20,pady=10)




#contact
window=LabelFrame(root,text="Contact Details",bg="firebrick",fg="white",font="vardhana")
window.grid(row=3,column=0,sticky="news",ipadx=20,ipady=10)

add_frame=Label(window,text="Mobile No.",fg="firebrick",bg="orange",font="vardhana 10 bold",height=1,width=10).grid(row=9,column=0,sticky=W)
w=Entry(window).grid(row=9,column=1,sticky="news",padx=20,pady=10)

add_frame=Label(window,text="Email ID",fg="firebrick",bg="orange",font="vardhana 10 bold",height=1,width=10).grid(row=10,column=0,sticky=W)
w=Entry(window).grid(row=10,column=1,sticky="news",padx=20,pady=10)



#registration
window=LabelFrame(root,text="Registration",bg="orange",fg="white",font="vardhana")
window.grid(row=4,column=0,sticky="news",ipadx=20,ipady=10)

add_frame=Button(window,text="Registor",fg="orange",bg="firebrick",font="vardhana 10 bold",height=1,width=10).grid(row=11,column=0,sticky="news",padx=20,pady=10)

