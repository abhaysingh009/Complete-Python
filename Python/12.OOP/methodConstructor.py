# A constructor is a special method in a class that runs automatically when an object is created.
# Function → Independent block of code
# Method → Function inside a class (works with objects)
# 🔸 1. Function

# A function is defined outside a class.

# def greet(name):
#     return "Hello " + name

# print(greet("Abhay"))

# 👉 It works independently

# 🔸 2. Method

# A method is a function defined inside a class.

# class Student:
#     def greet(self, name):
#         return "Hello " + name

# s1 = Student()
# print(s1.greet("Abhay"))

# 👉 It works with an object
class Demo:
    a=10;
    def __init__(self):
        print("I am constructor");
    def show(self):
        self.c=self.a*self.a
        print(self.a);
        print(self.c);

d=Demo();
d.show();