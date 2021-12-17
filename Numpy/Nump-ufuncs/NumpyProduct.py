'''
Produk
Untuk menemukan produk dari elemen dalam array, 
gunakan prod()fungsi.
'''
'Temukan produk dari elemen-elemen array ini:'
import numpy as np

'Temukan produk dari elemen-elemen array ini:'
arr = np.array([1,2,3,4])
x = np.prod(arr)
print(x)

'Pengembalian: 24 karena 1*2*3*4 = 24'

'cari product dar element dari dua array:'

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print(x)

'Pengembalian: 40320 karena 1*2*3*4*5*6*7*8 = 40320'


'''
Produk Di Atas Sumbu
Jika Anda menentukan axis=1, NumPy akan mengembalikan produk dari setiap larik.
'''

'Lakukan penjumlahan dalam larik berikut pada sumbu pertama:'
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)

'Pengembalian: [24 1680]'

'''
Produk Kumulatif
Produk kumulatif berarti mengambil produk sebagian.

Misal Hasil kali parsial [1, 2, 3, 4] adalah [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

Lakukan penjumlahan parsial dengan cumprod()fungsi.
'''
'Ambil produk kumulatif dari semua elemen untuk array berikut:'

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)

'Pengembalian: [5 30 210 1680]'