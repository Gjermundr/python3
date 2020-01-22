from tkinter import *
import tkinter.messagebox as mbox

def update_colour():
    if window.cget('bg') == 'lightgrey':
        window.configure(bg = 'lightblue')
    else:
        window.configure(bg = 'lightgray')

def show_info():
    mbox.showinfo('Information', 'Some information')

def show_warning():
    mbox.showwarning('Warning', 'This is a warning!')

def show_error():
    mbox.showerror('Error', 'an error has occured')

def show_askquestion():
    answer = mbox.askquestion('Question', 'Are you sure?')
    if answer == 'yes':
        mbox.showinfo('Response', 'You answered yes')
    else:
        mbox.showinfo('Response', 'You answered no')

def show_askokcancel():
    answer = mbox.askquestion('Question', 'Click OK or Cancel')
    if answer == 1:
        mbox.showinfo('Response', 'You answered OK')
    else:
        mbox.showinfo('Response', 'You answered Cancel')

def askyesno():
    answer = mbox.askyesno('Question', 'Yes or No')
    # yes = 1, no = 'no'
    if answer == 1:
        mbox.showinfo('Response', 'You answered Yes')
    else:
        mbox.showinfo('Response', 'You answered No')

def login():
    username = ent_username.get()
    password = ent_password.get()

    if username == 'jerry' and password == '123':
        mbox.showinfo('Login result', 'Successfull login')
    else:
        mbox.showinfo('Login result', 'Incorrect credentials provided.')

window = Tk()

lbl_username = Label(window, text='Username')
lbl_username.place(x=5,y=10)
ent_username = Entry(window)
ent_username.place(x=150,y=5)

lbl_password = Label(window, text='Password')
lbl_password.place(x=5,y=40)
ent_password = Entry()
ent_password.place(x=150,y=35)
btn_login = Button(window, text='Login', command=login)
btn_login.place(x=300,y=65)

window.title('Working with buttons!')

window.geometry('700x400')

label = Label(window,text='hello world')
#label.pack(padx=1,pady=50)

window.configure(bg='lightgray')

btn_update = Button(window, text='Update colour', command=update_colour)
btn_update.place(x=20,y=100)
btn_exit = Button(window,text='Exit', command='exit')
btn_exit.place(x=1,y=500)

btn_info = Button(window, text='Info', command=show_info)
btn_info.place(x=30,y=30)
btn_warning = Button(window, text='Warning', command=show_warning)
btn_warning.place(x=130, y=30)
btn_error = Button(window, text='Error', command=show_error)
btn_error.place(x=230, y=30)
btn_askquestion = Button(window, text='Question', command=show_askquestion)
btn_askquestion.place(x=330,y=30)

window.mainloop()

