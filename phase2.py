import numpy as np; 

arr = np.array([1,2,3,4,5,6,6,7,7,8,8]); 
# print(arr);
# print('basic' , arr[2:7]); 
# 2 indexx se leke 7 index tak 

# print('with step' , arr[1:8:2]); 
# kha se suru ; kha tak karni hai ; aur kitne step p 
# print('-ve index', arr[-3]);

arr_2d = np.array([[1,2,3],[4,5,6]]); 
# print('specfix', arr_2d[1,2])
# print('row', arr_2d[1]); 
# print('col', arr_2d[:, 1]); 

# sorting 

sorted = np.random.random((3,4)); 
# print('un sorted ', sorted);
# print('sorted', np.sort(sorted));

arr_2d_sorted = np.array([[2,3,4,1],[2,56,34,1], [13,43,21,3]])
 
# print('2d ',arr_2d_sorted)
# print('2d sorted',np.sort(arr_2d_sorted))

filtering = np.array([1,2,3,4,5,6,7,8,]); 
even = filtering[filtering % 2 == 0] 

# print('even', even);

index =np.array([1,2,3,4,5,6,7,8,]); 
Wherr_result = np.where(index > 5); 
# print(index[Wherr_result])

condition_array  = np.where(filtering > 4 , index*2, index)
# print(condition_array)

# aading and removing 

arr_merge = np.array([12,3,33,3]); 
arr_merge2 = np.array([123,321,3213,332,]); 
arr_merge3 = np.array([112,453,3354,334,]); 

# print(arr_merge3 + arr_merge2 + arr_merge)

print('shape' , arr_merge3.shape== arr_merge.shape)
# print(np.concatenate([arr_merge3, arr_merge2]))