from tkinter import *

FONT = ("Arial", 18, "bold")

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=100)

#Labels
miles = Label(text='Miles', font=FONT)
miles.grid(column=2, row=0)

equal_to = Label(text='is equal to', font=FONT)
equal_to.grid(column=0, row=1)

kilometers = Label(text='0', font=FONT)
kilometers.grid(column=1, row=1)

km = Label(text='Km', font=FONT)
km.grid(column=2, row=1)

#Button

def calculate_km():
    km_calculate = int(input.get()) * 1.6
    kilometers.config(text=int(km_calculate))

button = Button(text='Calculate', command=calculate_km)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()