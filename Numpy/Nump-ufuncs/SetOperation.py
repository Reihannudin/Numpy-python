'''
Operasi Set NumPy

Apa itu Satuan?
Himpunan dalam matematika adalah kumpulan elemen unik.

Himpunan digunakan untuk operasi yang melibatkan operasi perpotongan, 
penyatuan dan perbedaan yang sering.
'''
'''
Buat Set di NumPy
Kita dapat menggunakan unique()metode NumPy untuk menemukan elemen 
unik dari array apa pun. Misalnya membuat set array, 
tetapi ingat bahwa set array hanya boleh berupa array 1-D.
'''
'Ubah array berikut dengan elemen berulang menjadi satu set:'
import numpy as np
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x)

'''
Menemukan Persatuan
Untuk menemukan nilai unik dari dua array, gunakan union1d() metode.
'''
'Temukan gabungan dari dua set array berikut:'
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)

'''
Menemukan Persimpangan

Untuk menemukan hanya nilai yang ada di kedua array, 
gunakan intersect1d()metode.
'''
'Temukan persimpangan dari dua set array berikut:'
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.intersect1d(arr1, arr2, assume_unique=True)

print(newarr)

'''
Catatan: yang intersect1d()metode membawa argumen opsional 
assume_unique, yang jika set ke True dapat mempercepat perhitungan. 
tu harus selalu disetel ke True ketika berhadapan dengan set.
'''

'''
Menemukan Perbedaan
Untuk menemukan hanya nilai di set pertama yang TIDAK ada di set detik, 
gunakan setdiff1d() metode ini.
'''
'Temukan perbedaan set1 dari set2:'
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique=True)

print(newarr)

'''
Catatan: yang setdiff1d()metode membawa argumen opsional assume_unique, 
yang jika set ke True dapat mempercepat perhitungan. 
Itu harus selalu disetel ke True ketika berhadapan dengan set
'''

'''
Menemukan Perbedaan Simetris
Untuk menemukan hanya nilai yang TIDAK ada di KEDUA set, gunakan setxor1d()metode.
'''
'Temukan perbedaan simetris dari set1 dan set2:'

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr)

''''
Catatan: yang setxor1d()metode membawa argumen opsional assume_unique, 
yang jika set ke True dapat mempercepat perhitungan. 
Itu harus selalu disetel ke True ketika berhadapan dengan set.
'''
