'''
Apa itu ufunc?
ufuncs adalah singkatan dari "Fungsi Universal" dan mereka adalah 
fungsi NumPy yang beroperasi pada ndarray objek.
'''
'''
Mengapa menggunakan ufunc?
ufuncs digunakan untuk mengimplementasikan vektorisasi di NumPy 
yang jauh lebih cepat daripada mengulangi elemen.

Mereka juga menyediakan penyiaran dan metode tambahan seperti 
pengurangan, akumulasi dll yang sangat membantu untuk perhitungan.
'''
'''
ufuncs juga mengambil argumen tambahan, seperti:

where array boolean atau kondisi yang menentukan di mana operasi 
 harus dilakukan.

dtype mendefinisikan jenis kembali elemen.

out larik keluaran tempat nilai kembalian harus disalin.
'''
'''
Apa itu Vektorisasi?
Mengubah pernyataan iteratif menjadi operasi berbasis vektor disebut vektorisasi.

Ini lebih cepat karena CPU modern dioptimalkan untuk operasi semacam itu.

Tambahkan Elemen Dua Daftar
daftar 1: [1, 2, 3, 4]

daftar 2: [4, 5, 6, 7]

Salah satu cara melakukannya adalah dengan mengulangi kedua daftar dan kemudian 
menjumlahkan setiap elemen.
'''
'Tanpa ufunc, kita dapat menggunakan zip()metode bawaan Python :'
x = [1,2,3,4]
y = [4,5,6,7]
z = []

for i, j in zip(x, y):
    z.append(i + j)
print(z)

'NumPy memiliki ufunc untuk ini, yang disebut add(x, y) yang akan menghasilkan hasil yang sama.'
'Dengan ufunc, kita dapat menggunakan add() fungsi:'
import numpy as np

z = np.add(x,y)
print(z)