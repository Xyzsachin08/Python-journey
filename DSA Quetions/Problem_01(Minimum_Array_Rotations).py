def minimum_rotations(arr1,arr2):
    n = len(arr1)
    
    if n != len(arr2):
        return -1
    
    
    for i in range(n):
        rotated = arr1[i:] + arr1[:i]
        
        if rotated == arr2:
            lef_rot = i
            right_rot = n-i
            
            return min (lef_rot,right_rot)
        
    return -1
arr1 = [1,2,3,4,5]
arr2 = [3,4,5,1,2]

print("minimum_rotations:",minimum_rotations(arr1,arr2))
    