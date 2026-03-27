# “Encapsulation is the process of hiding data and allowing access only through methods.”
# Python does not have strict private/public like other languages, but we use naming conventions:

# 🔹 1. Public
# Accessible from anywhere
# self.name = "Abhay"
# 🔹 2. Protected (_)
# Meant for internal use (but still accessible)
# self._age = 20
# 🔹 3. Private (__)
# Not directly accessible outside class
# self.__salary = 50000

# 👉 This is called name mangling


# Getters and Setters

# Used to access and update private data safely

# Getter → Get value
# Setter → Set value

class demo:
    __name="abhay"#we cant call it outside class
    name2="aman"  #we can call it outside class
    def __init__(self):
        print(self.__name)
    
    def __display(self): #we cant call it outside class directly
        print("I am private Method")
    def display2(self):# we can call it outside class
        print("I am not private Method")

obj=demo();
print(obj.name2)
obj.display2()
# print(obj.__name)#error
# obj.__display() #error




# class Student:
#     def __init__(self):
#         self.__name=""
    
#     def getName(self):
#         return self.__name
#     def setter(self,name):
#         self.__name=name

# obj=Student();
# obj.setter("Abhay");
# print(obj.getName())
# print(obj.__name())