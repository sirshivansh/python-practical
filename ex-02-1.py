#defining a function
def add_numbers(x,y):
    return x+y

#calling a function
result = add_numbers(5,3)
print(result)

#defining a class
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def introduce(self):
        return f"My Name is {self.name} and I am {self.age} years old"
    def introduce2(self):
        return f"My Surname is {self.name} and My Roll Number is {self.age}"
person1= Person("Shivansh", 20)
person2= Person("Mishra", 2)

print(person1.introduce())
print(person2.introduce2())

try:
    result = 10/0
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    result = 10/2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division Successful: ", result)
finally:
    print("Execution Finished!")
