from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface():

    def __int__(self):
        self.window =  Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.canvas = Canvas()

        self.true_img = PhotoImage("./images/true.png")
        self.true_img = PhotoImage("./images/false.png")
        self.true_btn = Button(image=self.true_img )

        self.window.mainloop()

