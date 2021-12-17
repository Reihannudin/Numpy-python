'''
Permutasi Acak dari Elemen
Permutasi mengacu pada pengaturan elemen. 
misalnya [3, 2, 1] adalah permutasi dari [1, 2, 3] dan sebaliknya.

Modul NumPy Random menyediakan dua metode untuk ini: shuffle()dan permutation().
'''

'''
Mengacak Array
Shuffle berarti mengubah susunan elemen di tempat. yaitu dalam array itu sendiri.
'''
'Acak elemen array berikut secara acak:'
import numpy as np
from numpy import random

arr = np.array([1,2,3,4,5])

random.shuffle(arr)

print(arr)

'The shuffle()Metode membuat perubahan pada array yang asli.'

'Menghasilkan Permutasi Array'
'Hasilkan permutasi acak elemen array berikut:'
arr = np.array([1,2,3,4,5])
print(random.permutation(arr))

'The permutation()Metode mengembalikan array re-diatur (dan daun array asli un-berubah).'