'''
Fungsi Hiperbolik
NumPy menyediakan ufuncs sinh(), cosh() dan tanh() 
yang mengambil nilai dalam radian dan menghasilkan nilai 
sinh, cosh, dan tanh yang sesuai..
'''
'Cari nilai sinh dari PI/2:'

import numpy as np

x = np.sinh(np.pi/2)

print(x)

'Temukan nilai cosh untuk semua nilai di arr:'

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.cosh(arr)

print(x)

'''
Menemukan Sudut
Menemukan sudut dari nilai sinus hiperbolik, cos, tan. 
Misalnya sinh, cosh dan tanh kebalikan (arcsinh, arccosh, arctanh).

Numpy menyediakan ufuncs arcsinh(), arccosh() dan arctanh() 
yang menghasilkan nilai radian untuk nilai sinh, cosh, 
dan tanh yang sesuai yang diberikan.
'''
'Tentukan sudut 1,0:'
x = np.arcsinh(1.0)

print(x)

'Sudut Setiap Nilai dalam Array'
'Temukan sudut untuk semua nilai tanh dalam array:'
arr = np.array([0.1, 0.2, 0.5])

x = np.arctanh(arr)

print(x)