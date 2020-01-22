from tkinter import *
import tkinter.messagebox as mbox

window = Tk()
window.geometry('250x150')
window.title('Calculator')

def addition():
    int1 = ent_val1.get()
    int2 = ent_val2.get()
    mbox.showinfo('Answer is: ', int(int1) + int(int2))

def subtraction():
    int1 = ent_val1.get()
    int2 = ent_val2.get()
    mbox.showinfo('Answer is: ', int(int1) - int(int2))

def multiplication():
    int1 = ent_val1.get()
    int2 = ent_val2.get()
    mbox.showinfo('Answer is: ', int(int1) * int(int2))


ent_val1 = Entry(window)
ent_val2 = Entry(window)
ent_val1.place(x=55,y=20)
ent_val2.place(x=55,y=50)
lbl_val1 = Label(window, text='Value 1')
lbl_val2 = Label(window, text='Value 2')
lbl_val1.place(x=10,y=20)
lbl_val2.place(x=10,y=50)
btn_addition = Button(window, text='Add', command=addition)
btn_addition.place(x=10,y=85)
btn_subtraction = Button(window, text='Subtraction', command=subtraction)
btn_subtraction.place(x=45,y=85)
btn_multiplication = Button(window, text='Multiplication', command=multiplication)
btn_multiplication.place(x=120,y=85)
window.mainloop()