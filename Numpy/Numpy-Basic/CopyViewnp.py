'NumPy Array Copy vs View'
'''
Perbedaan Antara Menyalin dan Melihat
Perbedaan utama antara salinan dan tampilan array adalah bahwa
 salinan adalah array baru, dan tampilan hanyalah tampilan array asli.

Salinan memiliki data dan setiap perubahan yang dibuat pada salinan 
tidak akan memengaruhi larik asli, dan setiap perubahan yang dibuat 
pada larik asli tidak akan memengaruhi salinan.

Tampilan tidak memiliki data dan perubahan apa pun yang dilakukan
 pada tampilan akan memengaruhi larik asli, dan setiap perubahan yang
 dibuat pada larik asli akan memengaruhi tampilan.

'''

'Copy'

'Buat salinan, ubah array asli, dan tampilkan kedua array:'

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

'Salinan TIDAK HARUS terpengaruh oleh perubahan yang dibuat pada larik asli.'

'View'
'Buat tampilan, ubah array asli, dan tampilkan kedua array:'

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

'Tampilan HARUS dipengaruhi oleh perubahan yang dibuat pada larik asli.'


'Lakukan Perubahan pada VIEW:'
'Buat tampilan, ubah tampilan, dan tampilkan kedua array:'

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

'Array asli akan terpengaruh oleh perubahan yang dibuat pada tampilan.'


'''
Periksa apakah Array Memiliki Datanya
Seperti disebutkan di atas, salinan memiliki data,
 dan tampilan tidak memiliki data, tetapi bagaimana kami dapat memeriksanya?

Setiap array NumPy memiliki atribut baseyang kembali Nonejika array memiliki data.

Jika tidak, base  atribut mengacu pada objek asli.
'''

'Cetak nilai atribut dasar untuk memeriksa apakah array memiliki datanya atau tidak:'

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)