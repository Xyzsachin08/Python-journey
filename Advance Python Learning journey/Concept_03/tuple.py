# tuple Indexing & Slicing
t = (10, 20, 30, 40)

print(t[1])     # 20
print(t[-1])    # 40
print(t[1:3])   # (20, 30)





#Tuple Packing & Unpacking

t = (1, 2, 3)  #packing tuple


#unpacking divide tuple in variable
t = (10, 20, 30)

a, b, c = t

print(a)  # 10
print(b)  # 20
print(c)  # 30


# Swap using tuple
a = 5
b = 10

a, b = b, a

print(a, b)   # 10 5



#Nested tuple
t = ((1, 2), (3, 4), (5, 6))

#Access
print(t[1])      # (3, 4)
print(t[1][0])   # 3


#Tuple method
t = (1, 2, 2, 3)

t.count(2)   # 2
t.index(3)   # 3


#tuple is same like a list but cannot not be changed