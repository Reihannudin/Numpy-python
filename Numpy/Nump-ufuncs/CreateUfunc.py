'''
Cara Membuat Ufunc Anda Sendiri

Untuk membuat ufunc Anda sendiri, Anda harus mendefinisikan suatu fungsi, 
seperti yang Anda lakukan dengan fungsi normal di Python, lalu Anda menambahkannya
 ke pustaka ufunc NumPy Anda dengan frompyfunc()metode.
'''
'''
The frompyfunc()metode mengambil argumen berikut:

1. function - nama fungsi.
2. inputs - jumlah argumen input (array).
3. outputs - jumlah larik keluaran.
'''

import numpy as np
def myadd(x,y):
    return x+y
myadd = np.frompyfunc(myadd, 2,1)
print(myadd([1,2,3,4],[5,6,7,8]))

'''
Periksa apakah suatu Fungsi adalah ufunc
Periksa jenis fungsi untuk memeriksa apakah itu ufunc atau tidak.

Sebuah ufunc harus kembali <class 'numpy.ufunc'>.
'''
'periksa apakah suatu fungsi adalah ufunc:'
print(type(np.add))

'''
Jika bukan ufunc, itu akan mengembalikan tipe lain, 
seperti fungsi NumPy bawaan ini untuk menggabungkan dua atau lebih array:
'''
'Periksa jenis fungsi lain: concatenate():'
print(type(np.concatenate))

'Jika fungsinya tidak dikenali sama sekali, itu akan mengembalikan kesalahan:'
'Periksa jenis sesuatu yang tidak ada. Ini akan menghasilkan kesalahan:'
'print(type(np.blahblah))'

'''
Untuk menguji apakah fungsinya adalah ufunc dalam pernyataan if, gunakan numpy.ufuncn ilainya 
(atau np.ufunc jika Anda menggunakan np sebagai alias untuk numpy):
'''
'Gunakan pernyataan if untuk memeriksa apakah fungsinya adalah ufunc atau bukan:'

if type(np.add) == np.ufunc:
    print('Ini adalah ufunc')
else:
    print('Ini bukan ufunc')