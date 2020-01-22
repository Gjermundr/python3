from tkinter import *

window = Tk()
window.geometry('700x400')
window.title('About me')
window.configure(bg='lightblue')

lbl_name = Label(window, text='My name: Gjermund')
lbl_surname = Label(window, text='My surname: Fougner Haugen')
lbl_name.place(x=5,y=10)
lbl_surname.place(x=5,y=40)
lbl_description = Label(window, text='Description: I am a student living in Bergen and I like to drink :)')
lbl_description.place(x=5,y=70)

window.mainloop()