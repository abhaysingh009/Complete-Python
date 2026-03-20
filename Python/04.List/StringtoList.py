#covert string to list
#split() fun

s="hi my name is abhay"
li=s.split();
print(li)#['hi', 'my', 'name', 'is', 'abhay']


s="abhay pratap singh";
l=[x for x in s if x!=" " ]#stores characters one by one in x and makes a list of characters(string)
print(l,type(l))#list
print(type(l[0])) #str
