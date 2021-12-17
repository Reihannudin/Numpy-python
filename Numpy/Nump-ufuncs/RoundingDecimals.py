'''
Pembulatan Desimal
Ada lima cara utama pembulatan desimal di NumPy:

pemotongan    (truncation)
memperbaiki   (fix)
pembulatan    (rounding)
lantai        (floor)
langit-langit (ceil)
'''

'''
Truncation
Hapus desimal, dan kembalikan angka float yang paling dekat dengan nol. 
Gunakan fungsi trunc() dan fix().
'''
import numpy as np

'potong elemen array berikut'
arr = np.trunc([-3.1666, 3.6667])
print(arr)

'Contoh yang sama, menggunakan fix()'
arr = np.fix([-3.1666, 3.6667])
print(arr)


'''
Rounding / Pembulatan
The around()bertahap fungsi sebelumnya digit atau desimal dengan 1 jika> = 5 lain melakukan apa-apa.

Misalnya dibulatkan menjadi 1 titik desimal, 3.16666 adalah 3.2
'''

arr = np.around(3.1666, 2)
print(arr)


'''
Floor
Fungsi floor() membulatkan desimal ke bilangan bulat bawah terdekat.

Misalnya lantai 3.166 adalah 3.
'''
arr = np.floor([-3.1666, 3.6667])
print(arr)

'''
Catatan: The floor() mengembalikan fungsi mengapung, tidak seperti trunc()
fungsi yang kembali bilangan bulat.
'''

'''
Ceil

Fungsi ceil() membulatkan desimal ke bilangan bulat atas terdekat.

Misalnya langit-langit 3,166 adalah 4.
'''
'Langit-langit elemen array berikut:'
arr = np.ceil([-3.1666, 3.6667])

print(arr)