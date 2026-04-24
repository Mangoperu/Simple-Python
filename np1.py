import numpy as np
array  = np.array([1  ,3 ,4 ,5])
print(array)
array = array * 2
print(array)

#2d  , 3d 4d 

narray = np.array([[['A' , 'B ', 'C' , 'D'] , ['A' , 'B ', 'C' , 'D'] ,['A' , 'B ', 'C' , 'D']],
                    [['A' , 'B ', 'C' , 'D'] ,['A' , 'B ', 'C' , 'D'] ,['A' , 'B ', 'C' , 'D']],
                    [['A' , 'B ', 'C' , 'D'] ,['A' , 'B ', 'C' , 'D'] ,['A' , 'B ', 'C' , 'D']]])

word  = narray[2 , 0 ,1]
print(word)
print(narray.shape)

#slicing

array = np.array([[1, 2, 3, 4],
                  [5 ,6 ,7, 8],
                  [6 , 9 , 3, 5]])

print(array[2])
print(array[: , 2])
print(array[:  , 1:4:2])
#if step is negative then it is reversed
print(array[0:2 , 0:2])


