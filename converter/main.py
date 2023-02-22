from tkinter import *

window = Tk()
window.title("Unit converter")
window.minsize(width=250, height=150)
window.config(padx=25, pady=25)

# Labels - unit1, unit2, descriptions
label_unit1 = Label(text="Miles")
label_unit2 = Label(text="Km")
label_result_num = Label()
label_result_text = Label(text="Is equal to")
label_unit1.grid(column=2, row=0)
label_unit2.grid(column=2, row=1)
label_result_num.grid(column=1, row=1)
label_result_text.grid(column=0, row=1)

# User input
entry = Entry(width=5)
entry.grid(column=1, row=0)

# Calculate button

# create calculation function
def convert():
    user_input = float(entry.get())
    converted_input = round((user_input * 1.6), 2)
    print(converted_input)
    label_result_num.config(text=f"{converted_input}")


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=3)







window.mainloop()