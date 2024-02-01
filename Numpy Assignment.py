#!/usr/bin/env python
# coding: utf-8

# ### 1. What is a Python library? Why do we use Python libraries?
# Collection of related modules with precompiled code
#     Contains functions, classes, and resources for specific tasks.
#     Facilitates code reuse and modularity in different programs.
# 
# Purpose of Using Python Libraries:
# 
#     Efficiency:
#         Avoids rewriting existing code, saving time and effort.
#         Access to optimized, pre-built functions for common tasks.
# 
#     Specialized Functionality:
#         Provides tools and functionalities for specific domains.
#         Example: TensorFlow for machine learning, Matplotlib for plotting.
# 
#     Promotes Code Reusability:
#         Encourages reuse of well-tested, reliable code.
#         Reduces redundancy and enhances maintainability.
# 
#     Community Contribution:
#         Libraries often developed and maintained by communities.
#         Benefits from diverse expertise and ongoing improvements.
# 
#     Modularity:
#         Breaks down complex tasks into manageable modules.
#         Easier to develop, update, and maintain.
# 
#     Standardization:
#         Python Standard Library sets conventions and provides core functionality.
#         Ensures consistency and compatibility across projects.
# 
#     Enhanced Capabilities:
#         Extends Python's capabilities for various applications.
#         Example: Pandas for data manipulation in data science.

# ## 2.What is the difference between Numpyarray and list?

# Performance: NumPy arrays excel in performance for numerical computations due to their fixed size, data type, and optimized operations.
# 
# Memory usage: NumPy arrays are more memory-efficient for numerical data due to their compact storage.
# 
# Flexibility: Lists offer more flexibility in terms of data types and dynamic resizing.
# 
# Use cases:
# 
# NumPy arrays: Ideal for numerical data processing, scientific computing, data analysis, and machine learning.
# Lists: Well-suited for storing collections of mixed data types, general data manipulation, and situations where frequent modifications are needed.

# ## 3. Find the shape, size and dimension of the following array?
# 
# [[1, 2, 3, 4]
# 
# [5, 6, 7, 8],
# 
# [9, 10, 11, 12]]

# The shape of the array is (3,4) 3 rows and 4 columns and size of the array is 12 elements and the dimension of the array is 2-d array which is called as 2-dimensional array

# ## 4. Write python code to access the first row of the following array?
# 
# [[1, 2, 3, 4]
# 
# [5, 6, 7, 8],
# 
# [9, 10, 11, 12]]

# In[8]:


import numpy as np


# In[11]:


arr1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[12]:


arr1


# In[23]:


first_row=arr1[0]


# In[24]:


print("first_row",first_row)


# ## 5. How do you access the element at the third row and fourth column from the given numpy array?
# 
# [[1, 2, 3, 4]
# 
# [5, 6, 7, 8],
# 
# [9, 10, 11, 12]]

# In[35]:


arr2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[37]:


element=arr2[2,3]


# In[39]:


print("third row and fourth column is:",element)


# ## 6. Write code to extract all odd-indexed elements from the given numpy array?
# 
# [[1, 2, 3, 4]
# 
# [5, 6, 7, 8],
# 
# [9, 10, 11, 12]]

# In[45]:


arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[46]:


odd_numbers=arr[arr[:, :] %2 !=0]


# In[47]:


print("Odd numbers:",odd_numbers)


# ## 7. How can you generate a random 3x3 matrix with values between 0 and 1?

# In[50]:


import numpy as np
# generate random matrix
randommatrix = np.random.rand(3, 3)
print(randommatrix)


# ## 8. Describe the difference between np.random.rand and np.random.randn?

# 1.np.random.rand will have uniform distaribution values like 0 and 1 but for np.random.randn will have guassian distribution values with mean of 0 and standard deviation 1
# 
# 2.both 0 and 1 have equal probability in random.rand but in random.randn have most values occuring on mean value 0 with positive and negative directions.
# 
# 3.creating values with in a specified range but in random.randn simulating real_world phenomena with inherent randomness or noise
# 

# ## 9. Write code to increase the dimension of the following array?
# 
# [[1, 2, 3, 4]
# 
# [5, 6, 7, 8],
# 
# [9, 10, 11, 12]]

# In[51]:


arr = ([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[52]:


new_arr=np.expand_dims(arr, axis=0)


# In[53]:


print("new arrays:",new_arr )


# ## 10. How to transpose the following array in NumPy?
# 
# [[1, 2, 3, 4]
# 
# [5, 6, 7, 8],
# 
# [9, 10, 11, 12]]

# In[55]:


import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
Transposed_arr = arr.T
print(Transposed_arr)


# ## 11. Consider the following matrix:
# 
# Matrix A: [[1, 2, 3, 4] [5, 6, 7, 8],[9, 10, 11, 12]]
# 
# Matrix B: [[1, 2, 3, 4] [5, 6, 7, 8],[9, 10, 11, 12]]

# In[79]:


import numpy as np
A = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
B = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])

#index wise multiplication
index_wise_multiplication = A * B
print(" index wise multiplication:",index_wise_multiplication)



# Matrix wise multiplication
matrix_multiplication = np.dot(A, B.T)
print("matrix wise multiplication:",matrix_multiplication)



# Add both the matrics
Add_matrices = A + B
print("Adding matrices:",Add_matrices)


# Subtract matrix B from A
Sub_matrices = A - B
print("subtracting matrices:", Sub_matrices)

# Divide matrix B by A
Div_matrix = np.divide(A, B)
print("Divide matrices:", Div_matrix)


# ## 12. Which function in Numpy can be used to swap the byte order of an array?

# In[80]:


import numpy as np

original_array = np.array([1,2,3,4],dtype=np.int32)
swapped_array = original_array.byteswap()

print("Original array:", original_array)
print(" Swapped array:", swapped_array)


# ## 13.What is the significance of the np.linalg.inv function?

# In[81]:


import numpy as np

# Coefficient matrix
A = np.array([[2, 1], [5, 3]])

# Constants vector
B = np.array([4, 10])

# Solve for variables using inverse
X = np.linalg.inv(A).dot(B)

print("Solution:", X)


# ## 14. What does the np.reshape function do, and how is it used?

# The np.reshape function in NumPy is used to change the shape (dimensions) of an array without modifying its data. It allows you to reshape the array into a new desired shape, as long as the total number of elements remains the same

# In[86]:


arr = np.arange(12).reshape(3,4)
print(arr)


# In[87]:


reshaped_arr = arr.reshape(4,3)
print(reshaped_arr)


# ## 15. What is broadcasting in Numpy?

# In[90]:


import numpy as np
# create a 1d array
arr1 = np.array([1,2,3])
arr2 = np.array([[4], [5], [6]])
result = arr1 + arr2
print(result)


#Benefits of broadcasting:

Benefits of broadcasting:

    Efficiency: Avoids unnecessary array copying, leading to faster computations.
    Conciseness: Enables shorter and more readable code for many array operations.
    Versatility: Supports operations on arrays with different shapes as long as broadcasting rules are met#   Efficiency: Avoids unnecessary array copying, leading to faster computations.
#   Conciseness: Enables shorter and more readable code for many array operations.
#  Versatility: Supports operations on arrays with different shapes as long as broadcasting rules are met

