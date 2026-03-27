# “Polymorphism is the ability of a function or method to take multiple forms.”
# Types of Polymorphism in Python
# 🔹 1. Compile-Time Polymorphism

# (Also called Method Overloading)

# 👉 Python does not support true overloading, but we can simulate it.

# 🔹 2. Run-Time Polymorphism

# (Also called Method Overriding)

# 👉 Same method name, different implementation in child class

# Operator Overloading
# print(5 + 3)          # addition
# print("Hello " + "World")  # string join

# class Demo:
#     def Displayinfo(self ,name=' '):
#         print("hi my name is "+name)

# obj=Demo()

# #method overloading
# obj.Displayinfo();
# obj.Displayinfo("Abhay");

# method overriding
class A:
    def fun(self):
        print("Hello")

class B(A):
    def fun(self):
        # super().fun()# to call parent fun 
        print("World")

obj=B()
obj.fun()
# obj2=A()
# obj2.fun();


# class Area:
#     def find_area(self,a=None,b=None):
#         if(a!=None and b!=None ):
#             print("Area of Rectangle: ",a*b)
#         elif(a!=None and b==None):
#             print("Area of square: ",a*a)
#         else:
#             print("Nothing to find");


# # method overloading
# o=Area();
# o.find_area()
# o.find_area(4)
# o.find_area(4,5)