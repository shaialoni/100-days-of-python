class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("inhale, exhale")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water.")

    def breath(self):
        super().breath()
        print("underwater")

nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)