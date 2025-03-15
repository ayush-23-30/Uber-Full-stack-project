import numpy as np
# import matplotlib.pyplot as plt 

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 19000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub

    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

print("==== Zomato sales analysis ==== ")
# print("\n Sales data shape", sales_data.shape)
# print("\n Sample data for 1st 3 restau: ", sales_data[:3])

# total sales per year 

# print("Total Sales per year : " , np.sum(sales_data, axis=0)).--- sum of whole array 

year_total = np.sum(sales_data[:,1:], axis=0)
# print("year ", year_total).

# minimum sales 

min_Sales =  np.min(sales_data[:, 1:] , axis=1)
# print("min" , min_Sales)

single_sum = np.sum(sales_data[:, 1:],axis=1)

# print(single_sum).

max_per_year = np.max(sales_data [:, 1:],axis=0)
# print("max", max_per_year)
# average sales 

avg_Sale = np.mean(sales_data[:, 1:], axis=1)
# print(avg_Sale)
# axis = 0 === top to bottom run 
# axis - 1 === left to right 


cumsum = np.cumsum(sales_data[:,1:],axis=1);

# print("curm" , cumsum)

vector1 = np.array([1,2,3,4,5,6])
vector2 = np.array([1,2,3,4,5,6])

# print("vector addition", vector1 + vector2)

# print("mul", vector1 * vector2)

# print("dot product" , np.dot(vector1 , vector2));

print('angle', np.arccos(np.dot(vector1 ,vector2)/(np.linalg.norm(vector1) * np.linalg.norm(vector2))))
