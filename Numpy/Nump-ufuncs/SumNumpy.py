'''
penjumlahan
Apa perbedaan penjumlahan dan penjumlahan?

Penjumlahan dilakukan antara dua argumen sedangkan 
penjumlahan terjadi pada n elemen.
'''
'Tambahkan nilai di arr1 ke nilai di arr2:'
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)

'Pengembalin : [2, 4, 6 ]'

'Jumlahkan nilai di arr1 dan nilai di arr2:'

newarr = np.sum([arr1, arr2])

print(newarr)


'''
Penjumlahan Pada Sebuah Sumbu

Jika Anda menentukan axis=1, NumPy akan 
menjumlahkan angka di setiap array.
'''
'Lakukan penjumlahan dalam larik berikut pada sumbu pertama:'

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)

'Pengembalian: [6 6]'


''''
Jumlah Kumulatif
Jumlah kumulatif berarti menambahkan sebagian elemen dalam array.

Misalnya Jumlah parsial [1, 2, 3, 4] akan menjadi [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

Lakukan penjumlahan parsial dengan cumsum() fungsi.
'''
'Lakukan penjumlahan kumulatif dalam array berikut:'

arr = np.array([1, 2, 3, 4])

newarr = np.cumsum(arr)

print(newarr)

'Pengembalian [1 3 6 10]'