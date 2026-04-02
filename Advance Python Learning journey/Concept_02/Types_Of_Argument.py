'''. Positional Arguments

def show(name, age):
    print(name, age)
    
show("sachin",19)
show(19,"sachin")


#2. Keyword Arguments
def sachin(id, dept):
    print(id, dept) 
    
sachin(id=18, dept="Comp")
sachin(dept="IT", id=785)


# 3 Default Argument
def greet(name="user"):
    print("Hello",name)
    
greet(name="Sachin")

'''
#4 *args
def add(*sach):
    print(staticmethod)
    
add(1, 2, 3, 4)



# 5 **kwargs(key-value pairs)
def info(**data):
    print(data)
    
info(name="sachin", age=19)

#real life example
def student(Name, Age=18, *marks, **info):
    print("Name:", Name)
    print("Age:",Age)
    print("Marks:", marks)
    print("Extra:",info)
    
student("Sachin",78,(85,96,99,97), City="Pune")

