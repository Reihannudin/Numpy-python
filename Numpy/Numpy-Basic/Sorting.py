'''
Menyortir Array
Sorting berarti menempatkan elemen dalam urutan yang teratur .

Urutan berurutan adalah setiap urutan yang memiliki urutan yang sesuai dengan elemen, seperti numerik atau abjad, menaik atau menurun.

Objek NumPy ndarray memiliki fungsi yang disebut sort(), yang akan mengurutkan array yang ditentukan.
'''
'Urutkan array:'
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

'Catatan: Metode ini mengembalikan salinan larik, membiarkan larik asli tidak berubah.'

'Anda juga dapat mengurutkan array string, atau tipe data lainnya:'

'Urutkan array menurut abjad:'
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

'Urutkan array boolean:'

arr = np.array([True, False, True])
print(np.sort(arr))


'''
Menyortir Array 2-D
Jika Anda menggunakan metode sort() pada larik 2-D, kedua larik tersebut akan diurutkan:
'''
'Mengurutkan Larik 2-D'
arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))