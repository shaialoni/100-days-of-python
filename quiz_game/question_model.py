from data import question_data

class Question():

    # def __str__(self) -> str:
    #     return f"The text is {self.text} and the answer is {self.answer}"


    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer

