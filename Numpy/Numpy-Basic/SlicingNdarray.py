'Slicing Array NumPy'
'''
Mengiris array
Mengiris dengan python berarti mengambil elemen
 dari satu indeks yang diberikan ke indeks lain 
 yang diberikan.

Kami melewati slice alih-alih indeks seperti ini:
 .[start:end]

Kita juga bisa mendefinisikan langkahnya, seperti ini: .[start:end:step]

Jika kita tidak lulus mulai dianggap 0

Jika kita tidak melewati akhir yang dianggap panjang array dalam dimensi itu

Jika kita tidak melewati langkah itu dianggap 1
'''

import numpy as np 

arr = np.array([1,2,3,4,5,6,7])

print(arr[1:5])

'Catatan: Hasilnya termasuk indeks awal, tetapi tidak termasuk indeks akhir.'

'Iris elemen dari indeks 4 hingga akhir array:'
print(arr[4:])

'Elemen irisan dari awal hingga indeks 4 (tidak termasuk):'
print(arr[:4])

'''
Irisan Negatif
Gunakan operator minus untuk merujuk ke indeks dari akhir:
'''
'Iris dari indeks 3 dari akhir ke indeks 1 dari akhir:'

print(arr[-3:-1])


'''
MELANGKAH
Gunakan stepnilai untuk menentukan langkah pemotongan:
'''
print(arr[1:5:2])

'Kembalikan setiap elemen lain dari seluruh array:'
print(arr[::2])


'Slicing Array 2-D'

'dari element kedua, iris element dari indeks 1 ke indeks 4'

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

'Catatan: Ingat bahwa elemen kedua memiliki indeks 1.'

'Dari kedua elemen, kembalikan indeks 2:'

print(arr[0:2, 2])

'''
Dari kedua elemen, iris indeks 1 hingga indeks 4 (tidak termasuk),
 ini akan mengembalikan larik 2D:
 '''
print(arr[0:2, 1:4])