from tkinter import *

window = Tk()
window.title('Telepizza Program')
window.geometry('700x700')
window.configure(bg='beige')

# banner at top of page
img = PhotoImage(file='C:\\Users\\gjermund.haugen\\Documents\\Lightshot\\telepizza.png')
small_img = PhotoImage.subsample(img, x=2,y=2)
label = Label(window, image=small_img)
label.pack(side=TOP, pady=5)

frame_banner = Frame(window)
frame_banner.pack(side=TOP, pady=10)
frame_listbox = Frame(window)
frame_listbox.pack(side=TOP, pady=1)




listbox = Listbox(frame_listbox, width=40)
listbox.insert(1, 'Hawaiian pizza')
listbox.insert(2, 'Big boys pizza')
listbox.insert(3, 'savage night pizza')
listbox.insert(4, 'baseboosters pizza')
listbox.insert(5, 'dick dick gang pizza')
listbox.pack(side=LEFT, padx=5)
lst_btn = Button(frame_listbox, text='Select', command=show_selection)





window.mainloop()


class pizza():

    def hawaiian(self):

        base = 'Thick'
        crust = 'Thick'
        sause = 'Red'

















