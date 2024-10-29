import tkinter
root=Tk()
window=root.tk()
window.title("form")
frame=root.Frame(window)
frame.pack()


#saving user info
info_frame=LabelFrame(window,text="Personal Information")
info_frame.grid(row=1,column=1)
