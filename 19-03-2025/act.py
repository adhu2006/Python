1.) import numpy as np

# Create a 1D NumPy array from a list of numbers from 1 to 10.
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create a 1D array of 20 equally spaced numbers between 0 and 1.
array2 = np.linspace(0, 1, 20)

# Generate a 1D array of 10 random integers between 1 and 100.
array3 = np.random.randint(1, 101, size=10)

print(array1, array2, array3)

2.)# Create a 2D array with 3 rows and 4 columns filled with zeros.
array4 = np.zeros((3, 4))

# Generate a 2D array with the shape (5,5) containing random floating-point numbers.
array5 = np.random.random((5, 5))

# Create a 2x2 identity matrix.
array6 = np.eye(2)

print(array4, array5, array6)

3.)# Create a 3D array with the shape (3,4,2) filled with zeros.
array7 = np.zeros((3, 4, 2))

# Generate a 3D array with the shape (2,3,3) containing random integers between 1 and 10.
array8 = np.random.randint(1, 11, (2, 3, 3))

# Convert a list of 24 sequential numbers into a 3D array with shape (2,3,4).
array9 = np.arange(24).reshape(2, 3, 4)

# Calculate the mean along the row and column
mean_row = np.mean(array9, axis=1)  # mean along rows
mean_column = np.mean(array9, axis=2)  # mean along columns

print(array7, array8, array9, mean_row, mean_column)

4.)# Create a 3D array with the shape (2,3,4) filled with ones.
array10 = np.ones((2, 3, 4))

# Generate a 4D array with the shape (2,2,2,2) containing all zeros.
array11 = np.zeros((2, 2, 2, 2))

print(array10, array11)

5.)# Given a 1D array [3, 7, 2, 9, 5, 8, 1]
array12 = np.array([3, 7, 2, 9, 5, 8, 1])

# Extract elements at indices 1, 3, and 5
indices_1_3_5 = array12[[1, 3, 5]]

# 2D array with shape (4,5)
array13 = np.random.randint(1, 10, (4, 5))

# Extract the element at row 2, column 3
element = array13[2, 3]

# Extract the entire second row
second_row = array13[1, :]

# Extract a subarray containing rows 1 to 3 and columns 2 to 4
subarray = array13[1:4, 2:5]

print(indices_1_3_5, element, second_row, subarray)

6.)# 3D array with shape (3,4,5)
array14 = np.random.randint(1, 10, (3, 4, 5))

# Extract the element at position (depth 1, row 2, col 3)
element_3D = array14[1, 2, 3]

# Extract the entire first "layer" (all rows and columns of the first depth index)
first_layer = array14[0, :, :]

# Extract a subarray containing depths 1 to 3, rows 2 to 4, and columns 3 to 5
subarray_3D = array14[1:4, 1:3, 2:5]

print(element_3D, first_layer, subarray_3D)

7.)# Reshape a 1D array of 12 elements into a 3x4 2D array.
array15 = np.arange(12).reshape(3, 4)

# Reshape a 2D array of shape (3,4) into a 1D array.
array16 = array15.reshape(-1)

# Transpose a 2D array of shape (2,5)
array17 = np.random.random((2, 5))
transposed = array17.T

print(array15, array16, transposed)

8.)# Reshape a 3D array of shape (2,3,4) into a 2D array of shape (6,4).
array18 = np.zeros((2, 3, 4))
reshaped_3D = array18.reshape(6, 4)

# Transpose a 3D array, swapping the first and third dimensions.
transposed_3D = array18.transpose(2, 1, 0)

# Stack two 2D arrays of shape (3,4) to create a 3D array of shape (2,3,4).
array19 = np.random.random((3, 4))
stacked_3D = np.stack((array19, array19))

print(reshaped_3D, transposed_3D, stacked_3D)

9.)# Add two 1D arrays of the same length element-wise.
array20 = np.array([1, 2, 3, 4])
array21 = np.array([5, 6, 7, 8])
addition = array20 + array21

# Multiply a 2D array by a scalar value.
array22 = np.random.random((3, 4))
scalar_multiply = array22 * 5

# Calculate the square root of each element in an array.
sqrt_array = np.sqrt(array22)

print(addition, scalar_multiply, sqrt_array)

10.)# Element-wise addition between two 3D arrays of the same shape.
array23 = np.random.random((2, 3, 3))
array24 = np.random.random((2, 3, 3))
addition_3D = array23 + array24

# Calculate the mean along the second axis of a 3D array.
mean_3D = np.mean(array23, axis=1)

# Apply a function (like np.sin) to each element of a 3D array.
sin_array = np.sin(array23)

print(addition_3D, mean_3D, sin_array)

11.)# Add a 1D array of shape (3,) to each row of a 2D array with shape (4,3).
array25 = np.random.random((4, 3))
array26 = np.array([1, 2, 3])
broadcast_add = array25 + array26

# Multiply a 2D array of shape (3,4) with a 1D array of shape (4,).
array27 = np.random.random((3, 4))
array28 = np.array([1, 2, 3, 4])
broadcast_multiply = array27 * array28

print(broadcast_add, broadcast_multiply)

12.)# Add a 1D array of shape (4,) to each "row" across all "layers" of a 3D array with shape (3,5,4).
array29 = np.random.random((3, 5, 4))
array30 = np.array([1, 2, 3, 4])
broadcast_3D_add = array29 + array30

# Multiply a 2D array of shape (3,4) with each "layer" of a 3D array with shape (2,3,4).
array31 = np.random.random((2, 3, 4))
array32 = np.random.random((3, 4))
broadcast_3D_multiply = array31 * array32

# Scale each "layer" of a 3D array with shape (4,3,5) by a different scalar value from a 1D array of shape (4,).
array33 = np.random.random((4, 3, 5))
array34 = np.array([1, 2, 3, 4])
broadcast_scale = array33 * array34[:, np.newaxis, np.newaxis]

print(broadcast_3D_add, broadcast_3D_multiply, broadcast_scale)

13.)import pandas as pd

# Create a pandas Series with the values [5, 10, 15, 20, 25].
series1 = pd.Series([5, 10, 15, 20, 25])

# Create a Series with values [100, 200, 300, 400, 500] and index labels ['a', 'b', 'c', 'd', 'e'].
series2 = pd.Series([100, 200, 300, 400, 500], index=['a', 'b', 'c', 'd', 'e'])

# Create a Series from this dictionary: {'apple': 3, 'banana': 5, 'orange': 2}.
series3 = pd.Series({'apple': 3, 'banana': 5, 'orange': 2})

# For the Series s = pd.Series

14.)# Create a DataFrame from this dictionary:
data = {
    'Name': ['John', 'Emma', 'Alex'],
    'Age': [25, 30, 22],
    'City': ['New York', 'London', 'Paris']
}
df1 = pd.DataFrame(data)

# Create a simple DataFrame with 3 rows and 2 columns named 'A' and 'B' with any numbers you choose.
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Convert this list of lists into a DataFrame with column names 'Product', 'Price', 'Quantity':
data2 = [
    ['Apple', 1.2, 10],
    ['Banana', 0.5, 15],
    ['Orange', 0.8, 8]
]
df3 = pd.DataFrame(data2, columns=['Product', 'Price', 'Quantity'])

print(df1, df2, df3)

15.)# For the DataFrame created in question 14:
# Display the column names
columns = df1.columns

# Display the first 2 rows
first_two_rows = df1.head(2)

# Display information about the DataFrame (hint: use .info())
info = df1.info()

# Using this DataFrame:
df4 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Select column 'A'
col_a = df4['A']

# Select columns 'A' and 'C'
cols_a_c = df4[['A', 'C']]

# Select the value at row 1, column 'B'
value_at_1_b = df4.at[1, 'B']

print(columns, first_two_rows, info, col_a, cols_a_c, value_at_1_b)

16.)# Using this DataFrame:
df5 = pd.DataFrame({
    'Name': ['John', 'Emma', 'Alex', 'Sarah', 'Mike'],
    'Age': [25, 30, 22, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Berlin', 'Tokyo'],
    'Salary': [50000, 60000, 45000, 55000, 65000]
})

# Select rows where Age > 25
age_gt_25 = df5[df5['Age'] > 25]

# Select rows where City is 'London' or 'Paris'
city_london_paris = df5[df5['City'].isin(['London', 'Paris'])]

# Select rows where Salary is between 45000 and 60000
salary_range = df5[(df5['Salary'] >= 45000) & (df5['Salary'] <= 60000)]

print(age_gt_25, city_london_paris, salary_range)

17.)# Create a DataFrame with some missing values:
df6 = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': [9, 10, 11, None]
})

# Count the number of missing values in each column
missing_values = df6.isnull().sum()

# Drop rows with any missing values
df_drop = df6.dropna()

# Fill all missing values with 0
df_fill_zero = df6.fillna(0)

# Fill missing values in column 'A' with the mean of column 'A'
mean_a = df6['A'].mean()
df6['A'].fillna(mean_a, inplace=True)

# Fill missing values in column 'B' with the value 100
df6['B'].fillna(100, inplace=True)

# Replace all missing values with the previous valid value (use .ffill())
df6.ffill(inplace=True)

print(missing_values, df_drop, df_fill_zero, df6)

18.)# Create a DataFrame with student test scores:
df7 = pd.DataFrame({
    'Student': ['Alex', 'Bob', 'Charlie', 'David'],
    'Math': [85, 90, 70, 80],
    'Science': [90, 85, 75, 85],
    'English': [80, 95, 80, 75]
})

# Add a new column 'Average' that contains the average score for each student
df7['Average'] = df7[['Math', 'Science', 'English']].mean(axis=1)

# Sort the DataFrame by the Math scores in descending order
df7_sorted = df7.sort_values(by='Math', ascending=False)

# Find the student with the highest Science score
highest_science = df7.loc[df7['Science'].idxmax()]

print(df7, df7_sorted, highest_science)

19.)# Mean Calculation: Given the data set [3, 7, 9, 12, 15], calculate the mean.
data = [3, 7, 9, 12, 15]
mean_value = np.mean(data)

# Kurtosis Interpretation: What does kurtosis indicate about a data set?
# High kurtosis: heavy tails or outliers, low kurtosis: light tails or fewer outliers.

# Median vs. Mean:
# Median is the middle value, while mean is the average. Median is more robust to outliers.

# Mode Identification: Mode of the data set [2, 4, 4, 6, 8, 8, 8, 10].
from scipy import stats
mode_value = stats.mode([2, 4, 4, 6, 8, 8, 8, 10])[0][0]

# Range Calculation: Calculate the range for the data set [3, 5, 8, 12, 14].
data2 = [3, 5, 8, 12, 14]
range_value = np.ptp(data2)

# Variance Calculation: Sample variance for [1, 3, 5, 7].
variance = np.var([1, 3, 5, 7], ddof=1)

# Standard Deviation: Standard deviation for [5, 7, 10, 12, 14].
std_dev = np.std([5, 7, 10, 12, 14])

# Skewness Analysis: Skewness of [2, 3, 4, 5, 100].
from scipy.stats import skew
skewness = skew([2, 3, 4, 5, 100])

print(mean_value, mode_value, range_value, variance, std_dev, skewness)

20.)# Create a dictionary with the following key-value pairs:
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Print the dictionary.
print(my_dict)

21.)# Write a Python program to read the contents of a file named data.txt.
with open('data.txt', 'r') as file:
    content = file.readlines()
    for line in content:
        print(line)
        
22.)# Write a Python program to create a file called output.txt and write the text "Hello, World!" into it.
with open('output.txt', 'w') as file:
    file.write("Hello, World!")

23.)# Create a dictionary with the key "product" and the value "laptop".
product_dict = {"product": "laptop"}

# Update the dictionary by adding a new key-value pair "price": 1000.
product_dict["price"] = 1000

# Print the updated dictionary.
print(product_dict)

24.)
# Use the with statement to open a file named example.txt for reading, and then print its contents.
with open('example.txt', 'r') as file:
    print(file.read())

# Advantage of using `with`: It automatically handles file closing, even if an error occurs.

