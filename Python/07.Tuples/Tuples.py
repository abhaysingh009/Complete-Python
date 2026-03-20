
# Tuple = ordered collection

# Written using ()

# Immutable (cannot change after creation) ❗

# Allows duplicate values

# Faster than list (slightly)

# Can store different data types
t=(1,2,3,4);
print(t[0]);
print(max(t))
print(min(t))
print(sum(t))
print(t.count(4))# count freq
print(t.index(3))#to get index of a value
t1=(1)#type=int
t1=(1,)#type=tuple

# for i in range(len(t)):
#     print(t[i] ,end=" ");
for i in t:
    print(i,end=" ");
