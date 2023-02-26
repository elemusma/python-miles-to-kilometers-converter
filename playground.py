def add(*args):
    return sum([num for num in args])


print(add(1,2,3,4,6))


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')


my_car = Car(make='Nissan')
print(my_car.make)