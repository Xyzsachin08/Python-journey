'''
#Local vaiable 
x = 10 #global variable

def sachin():
    x = 20 #local variable
    print("This is the local variable",x)
    
sachin()
print("This is the global variable",x)



#global variable 
x = 10 #global variable

def sachin():
    x = 20 #local variable
    print("This is the local variable",x)
    
sachin()
print("This is the global variable",x)
'''


#Enclosing (non-local)
num = 50 # global variable

def onkar():
    num = 100 #enclosing
   
    
    def anisha():
        nonlocal num
        num = 500   #change outer variable 
        
    anisha()
    print(num)
    
onkar()
print(num)

#built-in function


print((lambda a ,b : a+b )(5,6))
        