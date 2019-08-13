class Person:
    def __init__(self, name):
        self.name = name
    def sayHy(self):
        print('Main Furrer das name is ', self.name, ', Zig Hail!!!!')

p = Person('Hitler')
p.sayHy()
Person('Himler').sayHy()