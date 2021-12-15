'''
Memisahkan Array NumPy
Pemisahan adalah operasi kebalikan dari Bergabung.

Bergabung menggabungkan beberapa larik menjadi satu dan 
Memisahkan memecah satu larik menjadi banyak.

Kami menggunakan array_split()untuk memisahkan array,
 kami memberikan array yang ingin kami bagi dan jumlah pemisahan.
'''

'Bagi array menjadi 3 bagian:'
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

'Catatan: Nilai yang dikembalikan adalah larik yang berisi tiga larik.'

'''
Jika array memiliki lebih sedikit elemen dari yang dibutuhkan,
array akan menyesuaikan dari akhir.
'''
'Bagi array menjadi 4 bagian:'
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)

'''
Catatan: Kami juga memiliki metode yang split()tersedia tetapi tidak 
akan menyesuaikan elemen ketika elemen kurang dalam array sumber untuk
pemisahan seperti pada contoh di atas, array_split()bekerja dengan baik
tetapi split()akan gagal.
'''

'''
Pisahkan Menjadi Array
Nilai kembalian dari array_split()metode ini adalah larik yang berisi 
setiap pecahan sebagai larik.

Jika Anda membagi sebuah array menjadi 3 array, Anda dapat mengaksesnya 
dari hasil seperti elemen array lainnya:
'''
'Akses array yang dipisah:'

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])


'''
Memisahkan Array 2-D
Gunakan sintaks yang sama saat memisahkan array 2-D.

Gunakan array_split()metodenya, berikan array yang ingin Anda bagi 
dan jumlah pemisahan yang ingin Anda lakukan.
'''
'Pisahkan larik 2-D menjadi tiga larik 2-D'
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

'''
Contoh di atas mengembalikan tiga array 2-D.

Mari kita lihat contoh lain, kali ini setiap elemen dalam array 2-D berisi 3 elemen.
'''
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)

'''
Contoh di atas mengembalikan tiga array 2-D.

Selain itu, Anda dapat menentukan sumbu mana yang ingin Anda lakukan pemisahan.

Contoh di bawah ini juga mengembalikan tiga larik 2-D, tetapi mereka dipisah di sepanjang baris (sumbu=1).
'''

'''
Contoh
Pisahkan larik 2-D menjadi tiga larik 2-D di sepanjang baris.
'''
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

'Solusi alternatif menggunakan hsplit() kebalikan dari hstack()'

'Gunakan hsplit()metode untuk membagi larik 2-D menjadi tiga larik 2-D di sepanjang baris.'
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)

'Catatan: Alternatif serupa dengan vstack()dan dstack()tersedia sebagai vsplit()dan dsplit().'