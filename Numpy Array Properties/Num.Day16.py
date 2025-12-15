import numpy as np 
#Simple array float type convert the int type
arr = np.array([12.3, 45.4, 34.6, 78.6])
print(arr.dtype)
arr_in = arr.astype(int)
print(arr_in)
print(arr_in.dtype)

#the short method of the operator.
print(arr + 2)
print(arr - 2)
print(arr * 2)
print(arr / 2)