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


#booleon masking
array = np.array([[1 , 2, 3, 5],
                 [10   , 2, 4, 7]])
mask = array>=3
print(mask)
print(array[mask])
print(array[array>=3])

#arithmetic

array = np.array([1 , 2, 3, 5])
print(array+1)
print(array - 1)
print(array *2)
print(array/2)
print(np.sqrt(array))

print(np.round(np.sqrt(array)))
print(np.ceil(np.sqrt(array)))

#broadcasting


#to broadcast the shape of both array either have 1 or have sam dimensions
array = np.array([1 , 2, 3 , 4])
array2 = np.array([[1],
                 [2],
                 [3],
                 [4]])
print(array.shape)
print(array2.shape)

print(array * array2)
print(array2 * array)