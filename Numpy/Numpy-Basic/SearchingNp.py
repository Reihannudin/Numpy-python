'''
Mencari Array
Anda dapat mencari array untuk nilai tertentu,
 dan mengembalikan indeks yang cocok.

Untuk mencari array, gunakan where() metode.
'''
'Temukan indeks di mana nilainya adalah 4:'
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

'''
Contoh di atas akan mengembalikan Tuple: (array([3, 5, 6],)

Yang artinya nilai 4 terdapat pada indeks 3, 5, dan 6.
'''

'Temukan indeks di mana nilainya ganjil:'
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

'Temukan indeks di mana nilainya genap:'
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)

'''
Cari Diurutkan
Ada metode yang disebut searchsorted()
yang melakukan pencarian biner dalam array, dan mengembalikan 
indeks di mana nilai yang ditentukan akan dimasukkan untuk
mempertahankan urutan pencarian.
'''

'The searchsorted() Metode diasumsikan digunakan pada array diurutkan.'

'Temukan indeks di mana nilai 7 harus dimasukkan:'
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

'''
Contoh menjelaskan: Angka 7 harus dimasukkan pada indeks 1 untuk tetap
mengurutkan urutan.

Metode ini memulai pencarian dari kiri dan mengembalikan indeks pertama 
di mana angka 7 tidak lebih besar dari nilai berikutnya.
'''

'''
Cari Dari Sisi Kanan
Secara default indeks paling kiri dikembalikan, tetapi kami dapat 
memberikan side='right'untuk mengembalikan indeks paling kanan sebagai gantinya.
'''

'Temukan indeks tempat nilai 7 harus dimasukkan, mulai dari kanan:'
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)

'''
Contoh menjelaskan: Angka 7 harus dimasukkan pada indeks 2 untuk tetap mengurutkan.

Metode memulai pencarian dari kanan dan mengembalikan indeks pertama di mana angka 7
 tidak lebih kecil dari nilai berikutnya.
'''

'''
Beberapa Nilai
Untuk mencari lebih dari satu nilai, gunakan larik dengan nilai yang ditentukan.
'''

'Temukan indeks di mana nilai 2, 4, dan 6 harus dimasukkan:'
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)