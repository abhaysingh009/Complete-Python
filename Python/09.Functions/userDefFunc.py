# Key Points (Easy to Remember)
# Function = block of reusable code
# Defined using def keyword
# Can take input (parameters)
# Can return output (return)
# Helps in code reuse & modularity

#simple functions
# def simplefun():
#     print("hello")
# simplefun();

#functions with arguments
# def funWithArg(x,y):
#     print(x+y)
# funWithArg(3,4);
# def funWithArg(x,y=10):#y=10 if second value not provided then 10 will be default value
#     print(x+y)
# funWithArg(3,4);
# funWithArg(3);

#functions with return
# def funWithReturn(a,b=2):
#     return a*b;
# print(funWithReturn(10,29));


# func with multiple return
def funWithReturn(a,b=2):
    return a*b,a*2;
print(funWithReturn(10,29));#(290, 20)
print(type(funWithReturn(10,29)));#tuple
