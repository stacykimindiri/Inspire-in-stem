#!/usr/bin/python

############################################
#   Name : Stacy Emmy
#   gui_example: using tkinker
#   Date: 7/6/2022
#############################################

from tkinter import *
# creating a window
#window = Tk()
#window.title("Welcome to EMMYS")
#window.configure(bg= 'purple')
# fix the window size
#window.geometry("400x400") 
# setting labels
#f_name = Label(window,text="First Name",font=("Times New roman",20))
#s_name= Label(window,text="Second Name",font=("Times New roman",20))
#f_name.grid(column = 60 , row = 100)
#s_name.grid(column = 60 , row = 120)
# placing buttons

def open_popup():
    top =Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up Window")
    top.configure(bg='blue')
    msg= Label(top,txt= "Welcome to pop up",font=('Times New roman',18)).place(x=150,y=150)
window = Tk()
window.title("Welcome to EMMYS")
window.configure(bg= 'purple')
window.geometry("400x400") 
button=Button(window,text="click",bg= 'black',fg= 'grey',command=open_popup)
button.pack()
button.grid(column=100,row=180)
f_name = Label(window,text="First Name",font=("Times New roman",20))
s_name= Label(window,text="Second Name",font=("Times New roman",20))
f_name.grid(column = 60 , row = 100)
s_name.grid(column = 60 , row = 120)
# inserting a text box
fname_box= Entry(window,width=30)
fname_box.grid(column=100,row=100)
sname_box= Entry(window,width=30)
sname_box.grid(column=100,row=120)

    
window.mainloop()
