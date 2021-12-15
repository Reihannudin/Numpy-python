'Bentuk Array NumPy'

'''
Bentuk Array
Bentuk array adalah jumlah elemen dalam setiap dimensi.
'''
'''
Dapatkan Bentuk Array
Array NumPy memiliki atribut yang disebut shape yang 
mengembalikan tuple dengan setiap indeks memiliki jumlah elemen yang sesuai.
'''
'Cetak bentuk larik 2D:'

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

'''
Contoh di atas mengembalikan (2, 4), yang berarti bahwa array memiliki 2 dimensi,
 di mana dimensi pertama memiliki 2 elemen dan yang kedua memiliki 4.
'''

'''
Buat array dengan 5 dimensi menggunakan ndminvektor dengan nilai 1,2,3,4 
dan verifikasi bahwa dimensi terakhir memiliki nilai 4:
'''

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)