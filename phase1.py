import numpy as np;

## Numpy Array and basics 

## creating array from list 

arr_id = np.array([1,2,3,4,5,6]); 

# print("1d Array ", arr_id); 


arr_2d = np.array([
    [1, 2, 3],
    [2, 23, 454]
])


# print(arr_2d); 


py_list = [1,2,3]; 
# print("Multiple List " , py_list * 2); 

np_array = np.array([1,2,3,4]); 
# print("np array ", np_array * 2) #  mutliple all elements

import time 

# start = time.time(); 

# py_listed = [i*2 for i in range(100000)]

np_start = time.time(); 

np_list = np.arange(1000000) * 2;
# print ('\n list time ', time.time() - np_start); 

zeros = np.zeros((4,4)); 
# print(zeros);

ones = np.ones((3,4));
# print(ones);

full = np.full((4,4), 7); 
# print(full);

random = np.random.random((2,4)); 
# print(random);

# seq = np.arange(0,10); 
seq = np.arange(0,10,2); 
# print(seq); 


vec = np.array([1,2,34,5]); 

matric = np.array([[1,2,3],[1323.2,32,32]]); 
# print(matric)

tensor = np.array([[[1, 2], [3, 4], [5, 6]], 
                   [[7, 8], [9, 10], [11, 12]]])
# print(tensor);

arr = np.array([[1,2,3,4,67], [4,3,2,1,56]]); 

# print("shape", arr.shape);
# print("Dimensons", arr.ndim);
# print("size", arr.size);
# print("data type", arr.dtype);

reshaping = np.arange(1,13); 
# print("res", reshaping.ndim)

reshaped = reshaping.reshape([3,4]); 
# print('new', reshaped); 
# print('new', reshaped.ndim);

flated = reshaped.flatten() 
# print(flated)
reveled = reshaped.ravel();
# print(reveled)

trans = reshaped.T; 
print(trans)

