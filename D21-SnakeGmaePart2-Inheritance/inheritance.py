### Inheritance exaple

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        # 상속받은 breath 메소드를 전부 작동 하겠다. 라는 선언
        super().breath()
        # 상속받은 메소드를 작동시킨 이후 작동할 선언
        print("doing this under the water")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)

