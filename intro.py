# import tkinter
from tkinter import *

window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
# my_label.pack(side='left')
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New text"
my_label.config(text='New text again')
#Button

def button_clicked():
    # print('I got clicked')
    # print(my_label.text)
    my_label.config(text=input.get())
    # my_label = Label(text="I got clicked")
    # my_label.pack()
    # return my_label

button = Button(text='Click this button', command=button_clicked)
button1 = Button(text='New button')
# button.pack()
# button.pack(side='left')
button.grid(column=1, row=1)
button1.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=3, row=3)
# input.pack()
# input.pack(side='left')



window.mainloop()