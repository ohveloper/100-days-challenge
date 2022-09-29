# Unlimited Arguments

def add(*args):  # args type is tuple
    result = 0
    for n in args:
        result += n
    return result

result = add(1,2,3,4,5)
print(result)


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(3, add=3, multiply=10)



class Car:

    def __init__(self, **kwargs):

        # get으로 받아오면 인자를 받지 않았을때 오류가 나지 않는다.
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Kia")
print(my_car.make)