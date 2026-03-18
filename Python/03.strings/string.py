#A string is a sequence of characters

#indexing
# rev idx-->-8 -7 -6 -5 -4 -3 -2 -1
# string-->  a  b  c  d  e  f  g  h
# index -->  0  1  2  3  4  5  6  7

# s="Abhay"
# print(s[0])# A
# print(s[-5])# A
# print(s[-1])# y


#Slicing
st="Hello my name is Abhay"
# print(st[0:5]);
# print(st[x:y]);#x=>start(inclusive),    y=>end(exclusive)

# print(st[0::2])# start from zero end (till last) inc of 2

# print(st[2:]) # start from 2 ----till last idx
# print(st[2::1])#,,
# print(st[2::])#,,

print(st[-1::-1]) #reverse the string
x=len(st);# find length of string
print(x);

#string iteration
for i in range(x):
    print(st[i]);

