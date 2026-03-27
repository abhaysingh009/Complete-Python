# OOP (Object-Oriented Programming) is a way of writing programs using objects and classes.
# It helps you organize code in a clean, reusable, and easy-to-understand way.

# 🔸 1. Class and Object
# 👉 Class

# A class is a blueprint (template) for creating objects.

# 👉 Object

# An object is an instance of a class.
class Demo:
    a=10
    def printsum(self,a,b):
        return a+b;

obj1=Demo();

print(obj1.a);#10
obj1.a=27;
print(obj1.a);#27
print(obj1.printsum(10,20));