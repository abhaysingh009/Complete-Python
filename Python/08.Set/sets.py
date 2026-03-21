# Key Points (Easy to Remember)

# Set = unordered collection

# Written using {}

# Stores unique elements only ❗

# No duplicates allowed

# Mutable (can add/remove)

# No indexing ❌

# Uses hashing (fast operations)

# set functions

# =>Adding Elements
# s.add(x)              # Adds single element
# s.update(iterable)    # Adds multiple elements

# =>Removing Elements
# s.remove(x)           # Removes element (error if not found)
# s.discard(x)          # Removes element (no error if not found)
# s.pop()               # Removes random element
# s.clear()             # Removes all elements

# =>Set Operations
# a.union(b)                    # Returns union (a ∪ b)
# a.intersection(b)             # Returns common elements
# a.difference(b)               # Elements in a but not in b
# a.symmetric_difference(b)     # Elements not common

# =>Update Operations (Modify Set)
# a.intersection_update(b)           # Keeps only common elements
# a.difference_update(b)             # Removes common elements
# a.symmetric_difference_update(b)   # Keeps non-common elements

# =>Checking Functions
# a.issubset(b)          # True if a ⊆ b
# a.issuperset(b)        # True if a ⊇ b
# a.isdisjoint(b)        # True if no common elements

# =>Copy
# s.copy()               # Returns shallow copy of set


#order is random
s={10,20,30,40}
print(s)

for i in s:
    print(i);

# s.remove(20);#gives error if 20 not present
# s.discard(20);# did n't gives error if 20 not present
# s.clear()
# print(s)#set()

s.add(28);
l=[83,93,72,10]
print(s.pop());#removes and returns random element
s.update(l)
print(s);#adds element of lists no duplicate
s2={10,72};
print(s2.issubset(s));
print(s.intersection(s2))
print(s.union(s2))

