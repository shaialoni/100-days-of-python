def add(*arg):
    sum = 0
    for number in arg:
        sum += number
    return sum

#print(add(1,2,3,4,5))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.year = kw.get("year")





my_car = Car(make="Dodge", model="Hellcat", year=2008, color="Black")
print(my_car.year)