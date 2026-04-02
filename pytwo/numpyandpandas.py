import numpy as np
# students_marks = [1,2,3]
# print(type(students_marks))

# n = np.array([[1,2,3],(1,2,5)], dtype=float)
# n1 = np.array([[1,2,3],(1,2,5)], dtype=str)
# print(type(n))
# print(n)
# print(n[0])
# print(n[1])
# n2 = np.zeros((2,3))
# print(n2)
# n3 = np.zeros([5,6], dtype= str)
# n4 = np.ones((2,3))
# print(n4)
# print(np.random.random((2,2)))
# np.save("myarray.npy",n4)
# print(n4.shape)
# print(n4.ndim)
# n5 = np.ones([2,3],[4,5])
# print(n5.ndim)

# first = np.array([1,2,3])
# second = np.array([4,5,6])
# print(np.add(first,second))
# print(first + second)
import pandas as pd
df= pd.DataFrame(
 {"a" : [4, 5, 6],
 "b" : [7, 8, 9],
 "c" : [10, 11, 12]},
 index = [1, 2, 3])
print(df)
