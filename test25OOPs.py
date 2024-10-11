class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def display(self):
        print(self.name, self.model)

object1 = Car("Toyota", 2016)
object2 = Car("Suzuki", 2017)
object2.display()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def func1(abc):
        print("Hello my name is " + abc.name + " and I am " + str(abc.age) + " years old")
        

p1 = Person("John", 36)
p2 = Person("Giri", 30)
p3 = Person("Sekhar", 25)
p1.func1()
p2.func1()
p3.func1()

del p3