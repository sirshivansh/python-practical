#Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")
dog = Dog("Sheru")
dog.speak()

class Parent :                          #Single Inheritance
    def greet(self):
        print("Hello from parent!")
class Child(Parent):
    pass
obj = Child()
obj.greet()

class Parent1:                          #Multiple Inheritance
    def greet(self):
        print("hello from parent1!")
class Parent2:
    def welcome(self):
        print("Welcome from parent2!")
class Child(Parent1, Parent2):
    pass
obj = Child()
obj.greet()
obj.welcome()

class Grandparent:                      #Multileval Inheritance
    def greet(self):
        print("hello from Grandparent!")
class Parent(Grandparent):
    pass
class Child(Parent):
    pass
obj = Child()
obj.greet()

class Parent:                          #Hierarchial Inheritance
    def greet(self):
        print("Hello from Parent")
class Child1(Parent):
    pass
class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()
obj1.greet()
obj2.greet()

class Base:                           #Hybrid Inheritance
    def greet(self):
        print("hello from Base")
class Derived1(Base):
    pass
class Derived2(Base):
    pass
class Hybrid(Derived1, Derived2):
    pass
obj = Hybrid()
obj.greet()

class Animal:                       #super() method in Inheritance
    def __init__(self, name):
        self.name= name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed
dog = Dog("Sheru", "German Shefard")
print(dog.name)
print(dog.breed)

#Method Overriding
class Parent:
    def greet(self):
        print("Hello from Parent!")
class Child:
    def greet(self):
        print("hello from Child!")
child = Child()
child.greet()