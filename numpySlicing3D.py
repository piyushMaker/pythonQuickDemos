import numpy as np 

arr3d = np.array([[[1,2,3], [1,2,3],[1,2,3]],[[4,5,6],[4,5,6],[4,5,6]],[[7,8,9],[7,8,9],[7,8,9]]])

print(arr3d)
print(" ")

print(arr3d [:,0,0])  #output [1,4,7]

#array slicing [Front2Back,ToptoBottom,Left2Right]
