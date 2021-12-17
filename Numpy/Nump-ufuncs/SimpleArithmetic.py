'''
Aritmatika Sederhana
Anda dapat menggunakan operator aritmatika + - * / secara langsung di antara array NumPy, 
tetapi bagian ini membahas ekstensi yang sama di mana kita memiliki fungsi yang dapat
mengambil objek seperti array seperti daftar, tupel, dll. dan melakukan aritmatika bersyarat.
'''
'Aritmatika Bersyarat: berarti kita dapat menentukan kondisi di mana operasi aritmatika harus terjadi.'
'Semua fungsi aritmatika yang dibahas mengambil where parameter di mana kita dapat menentukan kondisi itu.'

'''
Penambahan
The add()Fungsi merangkum isi dua array, dan mengembalikan hasil dalam array baru.
'''
'Tambahkan nilai di arr1 ke nilai di arr2:'

import numpy as np

arr1 = np.array([10,11,12,13,14,15])
arr2 = np.array([20,21,22,23,24,25])

newarr = np.add(arr1, arr2)
print(newarr)

'''
Contoh di atas akan mengembalikan [30 32 34 36 38 40] 
yang merupakan jumlah dari 10+20, 11+21, 12+22 dst.
'''

'''
Pengurangan
The subtract()Fungsi mengurangi nilai-nilai dari satu array
 dengan nilai-nilai dari array lain, dan mengembalikan hasil 
 dalam array baru.
'''

'kurangi nilai di arr2 dari nilai di arr1:'
newarr = np.subtract(arr1, arr2)
print(newarr)

'''
Perkalian
The multiply()mengalikan fungsi nilai dari satu array dengan 
nilai-nilai dari array lain, dan mengembalikan hasil dalam array baru.
'''
'Kalikan nilai di arr1 dengan nilai di arr2:'

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)
print(newarr)

'''
Contoh di atas akan mengembalikan [200 420 660 920 1200 1500] 
yang merupakan hasil dari 10*20, 20*21, 30*22 dst.
'''

'''
Pembagian
The divide()Fungsi membagi nilai-nilai dari satu array dengan 
nilai-nilai dari array lain, dan mengembalikan hasil dalam array baru
'''
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)
print(newarr)
'Contoh di atas akan mengembalikan [3.33333333 4. 3. 5. 25. 1.81818182] yang merupakan hasil dari 10/3, 20/5, 30/10 dst.'


'''
Pangkat
The power() Fungsi naik nilai dari array pertama dengan kekuatan nilai-nilai dari array kedua, 
dan mengembalikan hasil dalam array baru.
'''
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)


'''
Sisa
Baik fungsi mod() maupun remainder() fungsi mengembalikan sisa nilai dalam larik pertama yang sesuai 
dengan nilai dalam larik kedua, dan mengembalikan hasilnya dalam larik baru.
'''
'kembalikan sisanya:'

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)

print(newarr)

'''
Contoh di atas akan mengembalikan [1 6 3 0 0 27] 
yang merupakan sisa saat Anda membagi 10 dengan 3 (10%3), 
20 dengan 7 (20%7) 30 dengan 9 (30%9) dst.
'''
'Anda mendapatkan hasil yang sama saat menggunakan remainder()fungsi:'
'kembalikan sisanya'

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.remainder(arr1, arr2)

print(newarr)


'''
Hasil bagi dan Mod
The divmod()fungsi kembali baik hasil bagi dan mod. 
Nilai kembalian adalah dua larik, larik pertama berisi 
hasil bagi dan larik kedua berisi mod.
'''
'Kembalikan hasil bagi dan mod'
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr)

''''
Nilai Absolut
Baik absolute()dan abs()fungsi fungsi melakukan operasi mutlak 
yang sama elemen-bijaksana tetapi kita harus menggunakan absolute() 
untuk menghindari kebingungan dengan inbuilt pythonmath.abs()
'''
'Kembalikan hasil bagi dan mod:'

arr = np.array([-1,-2,1,2,3,-4])
newarr = np.absolute(arr)
print(newarr)

'Contoh di atas akan mengembalikan [1 2 1 2 3 4].'