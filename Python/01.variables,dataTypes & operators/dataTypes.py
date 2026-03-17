# Data Types in Python

# Data types define the type of value a variable can store.

# Example:

x = 10

# Here 10 is an integer, so the data type of x is int.

# 1. Numeric Data Types------------------------------------------------------------

# Used for numbers.

# Type	Example	Description
# int	10	Whole numbers
# float	3.14	Decimal numbers
# complex	2+3j	Complex numbers

# Example:

a = 10       # int
b = 3.5      # float
c = 2 + 3j   # complex



# 2. Sequence Data Types   -----------------------------------------------------------

# Used to store multiple values in order.

# Type	Example
# list	[1,2,3]
# tuple	(1,2,3)
# range	range(5)

# Example:

my_list = [1, 2, 3]

my_tuple = (4, 5, 6)
r = range(5)



# 3. Text Data Type  -----------------------------------------------------------
# Type	Example
# str	"Hello"

# Example:

name = "Abhay"



# 4. Set Data Types-----------------------------------------------------------

# Used to store unique values.

# Type	Example
# set	{1,2,3}
# frozenset	frozenset({1,2,3})

# Example:

s = {1, 2, 3}




# 5. Mapping Data Type        -----------------------------------------------------------
# Type	Example
# dict	{"name":"Abhay", "age":20}

# Example:

student = {
    "name": "Abhay",
    "age": 20
}




# 6. Boolean Data Type       -----------------------------------------------------------
# Type	Example
# bool	True / False

# Example:

x = True
y = False




# 7. None Type             -----------------------------------------------------------

# Represents no value.

# Example:

x = None

# ✅ Main Python Data Types

# int

# float

# complex

# str

# list

# tuple

# set

# dict

# bool

# NoneType


# Mutable 
# -List 
# -dictionary
# -byte array

# almost all other datatypes are immutable 


print(type(10));
print(type('c')); #string
print(type("k")); #string
print("this is eriojewroiw string")
print('''this is dfkjsdfjkdsxc
      cxviodof
      dfsoijdf
      cxvxijv
      xcvknxvxcopppppppppppppp
      multline string''')
print(type(2+3j)); #complex
print(type(223222222224234324232343222222222243234.23)); #float
x=14e3
print(x);#14000.0
