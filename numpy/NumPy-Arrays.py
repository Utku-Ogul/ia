import numpy as np


my_list = [1, 2, 3, 4, 5]

type(my_list)  # <class 'list'>
my_array = np.array(my_list)

type(my_array)  # <class 'numpy.ndarray'>

np.arange(0,100,10)  # Create an array with values from 0 to 100 with a step of 10

np.zeros((3, 4)) # Create a 3x4 array filled with zeros


np.random.seed(101)  # Set a random seed for reproducibility. 101 is a common choice and initial condition.
arr = np.random.randint(0, 100, 10)  # Create an array of 10 random integers between 0 and 100


arr.max()  # Find the maximum value in the array
arr.min()  # Find the minimum value in the array
arr.mean()  # Calculate the mean of the array
arr.shape  # Get the shape of the array (number of rows, number of columns)
arr.reshape(2, 5)  # Reshape the array to have 2 rows
        #  array([[95, 11, 81, 70, 63],
        # [87, 75,  9, 77, 40]])

       


arr.argmax()  # Get the index of the maximum value in the array
arr.argmin()  # Get the index of the minimum value in the array
arr.dtype  # Get the data type of the array elements
arr.size  # Get the total number of elements in the array


mat = np.arange(0, 100).reshape(10, 10)  # Create a 10x10 matrix with values from 0 to 99

#array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
#       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
#       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
#       [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
#       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
#       [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
#       [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
#       [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
#       [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
#       [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]])


row=0
col=1
mat[row, col]  # Access the element at row 0, column 1 (
    
mat[:, 1]  # Access all rows in column 1 (returns a 1D array)

mat[:, 1].reshape(10, 1)# Reshape the column to a 2D array with 10 rows and 1 column

# [[ 1]
#  [11]
#  [21]
#  [31]
#  [41]
#  [51]
#  [61]
#  [71]
#  [81]
#  [91]]

mat[0:3, 0:3]# Access a submatrix (first 3 rows and first 3 columns)
 
#  [[ 0  1  2]
#  [10 11 12]
#  [20 21 22]]

mat[0:3, 0:3]= 0# Set the first 3 rows and first 3 columns to zero


mynewmat = mat.copy()  # Create a copy of the matrix

mynewmat[0:6,:]=999 # Set the first 6 rows of the copied matrix to 999

