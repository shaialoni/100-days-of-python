from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print("click")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []

    password.extend([choice(letters) for _ in range(randint(8, 10))])
    password.extend([choice(symbols) for _ in range(randint(2, 4))])
    password.extend([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password)
    password = ''.join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = input_website.get()
    username = input_username.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill in all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {username} | {password}\n")

            input_website.delete(0, "end")
            password_entry.delete(0, "end")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website: ", font=("Arial", 14))
label_website.grid(row=1, column=0)
label_username = Label(text="Email / Username: ", font=("Arial", 14))
label_username.grid(row=2, column=0)
label_password = Label(text="Password", font=("Arial", 14))
label_password.grid(row=3, column=0)

input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()
input_username = Entry(width=35)
input_username.insert(0, "alonishai@gmail.com")
input_username.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
