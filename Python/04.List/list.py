# List in Python

# A list is a collection of items stored in a single variable.

# 👉 Lists are:

# Ordered

# Mutable (can be changed)

# Allow duplicate values

# Creating a List
# my_list = [1, 2, 'abhay', 4]
# my_list[0]="singh"
# print(my_list,type(my_list))


#nested List

# li=[1,2,3,[5,6,7]]
# print(li[3])# [5,6,7]
# print(li[3][0]) # 5



#List Slicing
# li=[12,234,45,576,2,2,3,6,7,8,56,34,32,234,5,6,7,5,3,2];
# print(li);
# print(li[0:]);
# print(li[:]);
# print(li[1:2]);#print(li[x:y]); x-->start(inclusive),  y-->end(exclusive)
# print(li[1::2]);#2=gap
# print(li[-1::-1]); #reverse list
# print(li[-1::]); 
# print(li[::-1]); #reverse list


# print(li[:-2]);


#list iteration
import time
li=[12,234,45,576,2,2,3,6,7,8,56,34,32,234,5,6,7,5,3,2];

x=len(li);
# print(x);

# for i in range(x):
#     # print(li[x-1-i],end=" ");
#     print(li[i],end=" ");

for i in li:
    # print(li[x-1-i],end=" ");
    print(i,end=" ");

