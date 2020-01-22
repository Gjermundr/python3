from tkinter import *
import tkinter.messagebox as mbox

window = Tk()
window.title('Personality test')
window.geometry('400x300')

def questionaire():
    q_1 = mbox.askquestion('Answer Yes or No (1 of 3)', 'Do you enjoy masturbating?')
    q_2 = mbox.askquestion('Answer Yes or No (2 of 3)', 'Did you masturbate today?')
    q_3 = mbox.askquestion('Answer Yes or No (3 of 3)', 'Are you gonna masturbate tomorrow?')

    if q_1 == 'yes' and q_2 == 'yes' and q_3 == 'yes':
        mbox.showinfo('Personality result', 'You are a normal human being')
    elif q_1 == 'yes' and q_2 == 'yes' and q_3 == 'no':
        mbox.showinfo('Personality results', 'Pervert!')
    elif q_1 == 'yes' and q_2 == 'no' and q_3 == 'yes':
        mbox.showinfo('Personality results', 'What are you waiting for? go masturbate!')
    elif q_1 == 'no' and q_2 == 'yes' and q_3 == 'yes':
        mbox.showinfo('Personality results', 'i admire the dedication.')
    elif q_1 == 'no' and q_2 == 'no' and q_3 == 'no':
        mbox.showinfo('Personality results', 'You are liar.')
    elif q_1 == 'no' and q_2 == 'no' and q_3 == 'yes':
        mbox.showinfo('Personality results', 'I believe in you, you can do this!')
    elif q_1 == 'no' and q_2 == 'yes' and q_3 == 'no':
        mbox.showinfo('Personality results', 'Kind of random, but Okay.')
    elif q_1 == 'yes' and q_2 == 'no' and q_3 == 'no':
        mbox.showinfo('Personality results', 'are you mormon?')


lbl_questionare = Label(window, text='Answer the questions honestly and WIN a prize!')
lbl_questionare.place(x=50,y=50)
btn_start = Button(window, text='Start personality test', command=questionaire)
btn_start.place(x=50,y=80)
btn_exit = Button(window, text='Exit', command=exit)
btn_exit.place(x=250,y=80)

window.mainloop()
