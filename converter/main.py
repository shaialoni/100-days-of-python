from tkinter import *

def convert():
    user_input = float(user_entry.get())
    converted_input = round((user_input * 1.609), 2)
    #print(converted_input)
    label_result_num.config(text=f"{converted_input}")

window = Tk()
window.title("Unit converter")
window.config(padx=25, pady=25)

label_unit1 = Label(text="Miles")
label_unit2 = Label(text="Km")
label_result_num = Label(text="0")
label_result_text = Label(text="Is equal to")

label_unit1.grid(column=2, row=0)
label_unit2.grid(column=2, row=1)
label_result_num.grid(column=1, row=1)
label_result_text.grid(column=0, row=1)

user_entry = Entry(width=5)
user_entry.grid(column=1, row=0)

button = Button(text="Click to calculate", command=convert)
button.grid(column=1, row=3)

window.mainloop()
