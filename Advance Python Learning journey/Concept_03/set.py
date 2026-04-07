# Unique element
s = {1, 2, 2, 3, 3, 4}
print(s)

# Unordered (no index)
s = {10, 20, 30}

#print(s[0])



#Set Operations
A = {1, 2, 3}
B = {3, 4, 5}

#Union
print(A | B)
# OR
print(A.union(B))


#Intersection
print(A & B)
# OR
print(A.intersection(B))



#Difference(A-B)
print(A - B)
# OR
print(A.difference(B))


#Symmetric Differnce
print(A ^ B)



#Set method
s = {1, 2, 3}

s.add(4)        # add element
s.remove(2)     # remove element
s.discard(10)   # no error if not found


#Extra method
len(s)          # size
s.pop()         # random element remove
s.clear()       # empty set



#remove duplicate from the list

lst = [1, 2, 2, 3, 3, 5]
unique = list(set(lst))
print(unique)

