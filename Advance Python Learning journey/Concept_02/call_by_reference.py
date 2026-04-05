my_list = [1, 2, 3, 4]
def modify_list(li):
    li.append(5)
    print(li)
    
print("Before calling fun",my_list)
modify_list(my_list)
print("After calling fun",my_list)