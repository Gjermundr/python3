from tkinter import *
import tkinter.messagebox as mbox

window = Tk()
window.title('Personality test')
window.geometry('400x300')
def questionaire():
    q_1 = mbox.askquestion('Answer Yes or No (1 of 3)', 'Do you enjoy masturbating?')
    q_2 = mbox.askquestion('Answer Yes or No (2 of 3)', 'Did you masturbate today?')
    q_3 = mbox.askquestion('Answer honestly... (3 of 3)', 'blalblabal')







btn_start = Button(window, text='Start personality test', command=questionaire())
btn_start.place(x=50,y=30)
window.mainloop()
