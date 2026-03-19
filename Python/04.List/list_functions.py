# list functions
# li=[10,20,30,40,50,60,70];
# del(li[1]);# remove value at given index

# print(li)
# print(li.pop(1));# removes value at given index and return poped element'

# li.remove(60);# removes given value 

# print(li);

#  li.clear();# clear the list
# print(li);


#insert(), append(), extends()

li=[10,20,30,40,50,60,70];
# li.insert(0,100);
# li.insert(10,100);# if index value is greater than size than pushes  elem at the end 
# li.insert(9,23);
# print(li)
# li.append(90);# push_back
li2=[82,435];
# li.append(li2);# push li2 at the end, not elements of the list

li.extend(li2);# push elements of the li2 at the end
# li.extend(92);# throws error becz it takes only iterable object
li.reverse();
print(li);

# List Methods
#len
#sort
#append
#extend
#del
#reverse
#sorted
#max
#min
#pop
#sum
#remove
#clear
#copy
#insert
#count
#index
print(li.index(20));# index of value __ throws error if vaue not present

st1=["hello","w"]# ans w (ASCII >h)
print(max(st1))
st2 =st1.copy();
print(st2)
