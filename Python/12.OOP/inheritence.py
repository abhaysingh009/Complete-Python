# Inheritance in Python (Theory First)
# 🔸 What is Inheritance?

# Inheritance is an OOP concept where one class (child class) acquires the properties and behaviors of another class (parent class).

# 👉 In simple words:
# “Reuse code from an existing class instead of writing it again.”

# 🔸 Why Use Inheritance?
# Code Reusability → No need to rewrite code
# Better Organization → Clear structure
# Easy Maintenance → Changes in parent affect child
# Real-world Modeling → Represents relationships (like Father → Son)
# 🔸 Key Terms (Important for Exams)
# Parent Class / Base Class / Superclass
# → The class whose properties are inherited
# Child Class / Derived Class / Subclass
# → The class that inherits properties


# --------------------------------------------------------------------------------------------------------------------------------
# 🔸 Types of Inheritance 
# 1. Single Inheritance   ----------------

# One parent → one child

# 👉 Example:
# Animal → Dog

# 2. Multiple Inheritance    ----------------

# Multiple parents → one child

# 👉 Example:
# Teacher + Researcher → Professor

# 3. Multilevel Inheritance    ----------------

# Inheritance in levels (chain)

# 👉 Example:
# Grandfather → Father → Son

# 4. Hierarchical Inheritance    ----------------

# One parent → many children

# 👉 Example:
# Animal → Dog, Cat



# --------------------------------------------------------------------------------------------------------------------------------
# 🔸 Important Concepts
# 🔹 1. Method Overriding

# Child class modifies parent method

# 👉 Used when child needs different behavior

# 🔹 2. super() Keyword

# Used to call parent class methods or constructor

# 👉 Very important for exams

# 🔹 3. is-a Relationship

# Inheritance represents “is-a” relationship

# 👉 Dog is an Animal

# class A:
#     def display(self):
#         print("Class A");
#     def mtd(self):
#         print("Class A second method")

# class B(A):
#     def display(self):
#         super().display();#to call parent method (here -which is overidden)
#         super().mtd();
#         print("Class B");
# class C(B):
#     def cmtd(self):
#         print("C class method")

# ob=B();
# ob.display();

# ob2=C();

# ob2.cmtd();
# ob.mtd();

# Multiple Inheritance
class A:
    def display(self):
        print("Class A");
    def mtd(self):
        print("Class A second method")

class B:
    def display(self):
        super().display();#to call parent method (here -which is overidden)
        super().mtd();
        print("Class B");
class C(B,A):
    def cmtd(self):
        print("C class method")

ob=C();
ob.display();