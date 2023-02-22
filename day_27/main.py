from tkinter import *

window = Tk()
window.title("my first GUI program")
window.minsize(width=400, height=350)
window.config(padx=50, pady=50)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
#my_label.pack()
# Can't use pack() ad grid() at the same program
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New text"
my_label.config(text="New text")

# Button
def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()

button = Button(text="Click me", command=button_clicked)
button_2 = Button(text="I'm a button too", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)
button_2.grid(column=2, row=0)


# entry component
input = Entry(width=10)
input.get()
#input.pack()
input.grid(column=3, row=2)


window.mainloop()
