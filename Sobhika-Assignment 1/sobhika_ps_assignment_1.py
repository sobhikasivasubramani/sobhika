# -*- coding: utf-8 -*-
"""Sobhika PS -Assignment 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F2JWyDqqRCRsCufpy7zxTyq3FAq2DO30

# Basic Python

## 1. Split this string
"""

s = "Hi there Sam!"

words = s.split(',')
print(words)

"""## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

print ('the diameter of {} is {} kilometres.'format.(planet, diameter))

"""## 3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

lst = [1,2,[3,4],[5,[100,200,
['hello']],23,11],1,7]
lst = [1,2,[3,4],[5,[100,200,
['hello']],23,11],1,7]
a=lst[3][1][2];
print(a)

"""# Numpy"""

import numpy as np

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

import numpy as np
array=np.zeros(10)
print("An array of 10 zeros:")
print(array)

array=np.ones(10)*5
print("An array of 10 fives:")
print(array)

"""## 5. Create an array of all the even integers from 20 to 35"""

import numpy as np
array=np.arange(20,36,2)
print("Array of all the even integers from 20 to 35")
print(array)

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

np.arange(0,9).reshape((3,3))
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])

"""## 7. Concatinate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

import numpy as geek
  
arr1 = geek.array([1,2,3])
arr2 = geek.array([4,5,6])
  
gfg = geek.concatenate((arr1, arr2), axis = 0)
  
print (gfg)

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

data = [10,20,30]
df = pd.DataFrame(data, columns=['Numbers'])
print (df)

"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

import datetime
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 2, 10)
delta = datetime.timedelta(days=1)
while (start_date <= end_date): 
print(start_date, end="\n")
start_date += delta

"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

df = pd.DataFrame(lst, columns =['FNo', 'LNo', 'Age'],
dtype = float)