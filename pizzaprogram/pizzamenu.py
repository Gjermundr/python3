from tkinter import *

def show_selection():
    if listbox.get(listbox.curselection()) == the_tropical.name:
        ingredients = the_tropical.ingredients
    elif listbox.get(listbox.curselection()) == thai_chicken.name:
        ingredients = thai_chicken.ingredients
    elif listbox.get(listbox.curselection()) == pepper_steak.name:
        ingredients = pepper_steak.ingredients
    elif listbox.get(listbox.curselection()) == moby_dick.name:
        ingredients = moby_dick.ingredients
    elif listbox.get(listbox.curselection()) == big_shot.name:
        ingredients = big_shot.ingredients

    message.set('{} ingredients: {}'.format(listbox.get(listbox.curselection()), ingredients))

class Pizza:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

def calculate():
    total = 0
    total += topping_1.get()
    total += topping_2.get()
    total += topping_3.get()
    total += topping_4.get()
    total += topping_5.get()

    calculation.set('Extra costs: {}'.format(total))


# creating pizza objects
the_tropical = Pizza('The Tropical', 'pepperoni, pineapple, oregano', 199)
thai_chicken = Pizza('Thai Chicken', 'sataychicken, paprika, redonion, pineapple, sataysauce, peanuts', 219)
pepper_steak = Pizza('Pepper Steam', 'marinaded steak, paprika, oregano', 225)
moby_dick = Pizza('Moby Dick', 'shrimp, garlicmarinade, purre, paprika, limezest', 229)
big_shot = Pizza('Big Shot', 'BBQ-chicken, bacon, pepperoni, tomato, oregano', 235)


# window configuration
window = Tk()
window.title('Telepizza Program')
window.geometry('700x700')
window.configure(bg='beige')

# banner at top of page
img = PhotoImage(file='C:\\Users\\Jerry\\Documents\\GitHub\\Python3\\pizzaprogram\\telepizza.png')
small_img = PhotoImage.subsample(img, x=2,y=2)
img_label = Label(window, image=small_img)
img_label.pack(side=TOP, pady=0)

# frames
frame_banner = Frame(window)
frame_banner.pack(side=TOP, pady=10)
frame_listbox = Frame(window)
frame_listbox.pack(side=TOP, pady=1)
#selection choice
message = StringVar()
message.set('No selection made')


# listbox for pizzas
listbox = Listbox(frame_listbox, height=10, width=40)
listbox.insert(0, the_tropical.name)
listbox.insert(1, thai_chicken.name)
listbox.insert(2, pepper_steak.name)
listbox.insert(3, moby_dick.name)
listbox.insert(4, big_shot.name)
listbox.pack(side=LEFT, padx=1)


# select button config
frame_select = Frame(window)
frame_select.pack(side=TOP, anchor=W, padx=130)
btn_listbox = Button(frame_select, text='Select', command=show_selection)
btn_listbox.pack(side=LEFT, anchor=W,)
lbl_selected = Label(frame_select, textvariable=message)
lbl_selected.pack(side=LEFT, pady=10)

# radio buttons for thick/thin pizza
pizza_base = StringVar()

frame_radio = Frame(window)
frame_radio.pack(side=TOP, pady=10)
lbl_radio = Label(frame_radio, text='Select pizza dough thickness ->')
lbl_radio.pack(side=LEFT, padx=10)
rad_thick = Radiobutton(frame_radio, text='Thick', value='Thick', variable=pizza_base)
rad_thick.pack(side=LEFT, padx=50)
rad_thin = Radiobutton(frame_radio, text='Thin', value='Thin', variable=pizza_base)
rad_thin.pack(side=LEFT, padx=20)


# checkbutton vars
topping_1 = IntVar()
topping_2 = IntVar()
topping_3 = IntVar()
topping_4 = IntVar()
topping_5 = IntVar()



frame_toppings = Frame(window)
frame_toppings.pack(side=TOP, anchor=W, padx=130)

lbl_toppings = Label(frame_toppings, text='Extra toppings: ')
lbl_toppings.pack(side=TOP, anchor=W)
chk_extracheese = Checkbutton(frame_toppings, onvalue=6, offvalue=0, text='Extra Cheese', variable=topping_1, command=calculate)
chk_extracheese.pack(side=TOP, anchor=W)
chk_extrabacon = Checkbutton(frame_toppings, onvalue=6, offvalue=0, text='Extra Bacon', variable=topping_2, command=calculate)
chk_extrabacon.pack(side=TOP, anchor=W)
chk_pickles = Checkbutton(frame_toppings, onvalue=4, offvalue=0, text='Pickles', variable=topping_3, command=calculate)
chk_pickles.pack(side=TOP, anchor=W)
chk_cucumber = Checkbutton(frame_toppings, onvalue=4, offvalue=0, text='Cucumber', variable=topping_4, command=calculate)
chk_cucumber.pack(side=TOP, anchor=W)
chk_avocado = Checkbutton(frame_toppings, onvalue=5, offvalue=0, text='Avocado', variable=topping_5, command=calculate)
chk_avocado.pack(side=TOP, anchor=W)


calculation = StringVar()
calculate()
lbl_calculation = Label(frame_toppings, textvariable=calculation)
lbl_calculation.pack(anchor=W, pady=10)



window.mainloop()












