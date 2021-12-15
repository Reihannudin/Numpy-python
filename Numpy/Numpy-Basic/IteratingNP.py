'Iterating Arrays'

'''
Iterasi Array
Iterasi berarti menelusuri elemen satu per satu.

Saat kita berurusan dengan array multi-dimensi di numpy,
 kita bisa melakukan ini menggunakan forloop dasar python.

Jika kita mengulangi pada larik 1-D, ia akan melewati setiap elemen satu per satu
'''
'Iterasi pada elemen larik 1-D berikut:'
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)

'''
Iterasi Array 2-D
Dalam array 2-D itu akan melewati semua baris.
'''
'Ulangi elemen larik 2-D berikut:'
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

'''
Jika kita melakukan iterasi pada array n -D maka akan melewati dimensi
 n-1 satu per satu.
'''

'Untuk mengembalikan nilai aktual, skalar, kita harus mengulangi array di setiap dimensi.'


'Iterasi pada setiap elemen skalar dari larik 2-D:'
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)


'''
Iterasi Array 3-D
Dalam array 3-D itu akan melalui semua array 2-D.
'''
'ulangi element larik 3-D berikut'
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

'Untuk mengembalikan nilai aktual, skalar, kita harus mengulangi array di setiap dimensi.'
for x in arr:
  for y in x:
    for z in y:
      print(z)

'''
Iterasi Array Menggunakan nditer()
Fungsi tersebut nditer() adalah fungsi bantuan yang dapat digunakan dari iterasi yang sangat dasar 
hingga yang sangat lanjut. Ini memecahkan beberapa masalah dasar yang kita hadapi dalam iterasi, 
mari kita membahasnya dengan contoh.

Iterasi pada Setiap Elemen Skalar
Dalam forloop dasar , iterasi melalui setiap skalar array kita perlu menggunakan n for loop yang 
mungkin sulit untuk ditulis untuk array dengan dimensi yang sangat tinggi.
'''
'Iterasi melalui larik 3-D berikut:'

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

'''
Iterasi Array Dengan Tipe Data Berbeda
Kita dapat menggunakan op_dtypesargumen dan meneruskan tipe data yang diharapkan untuk mengubah 
tipe data elemen saat iterasi.

NumPy tidak mengubah tipe data elemen di tempat (di mana elemen berada dalam array) sehingga perlu
 beberapa ruang lain untuk melakukan tindakan ini, ruang ekstra itu disebut buffer, dan untuk mengaktifkannya
 di nditer() we pass flags=['buffered'].
'''
'Iterasi melalui array sebagai string:'

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

'''
Iterasi Dengan Ukuran Langkah Berbeda
Kita bisa menggunakan filtering dan diikuti dengan iterasi.
'''
'Ulangi setiap elemen skalar dari larik 2D dengan melewatkan 1 elemen:'

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

'''
Enumerated Iteration Menggunakan ndenumerate()

Pencacahan berarti menyebutkan nomor urut sesuatu satu per satu.

Terkadang kami memerlukan indeks elemen yang sesuai saat iterasi,
 ndenumerate()metode ini dapat digunakan untuk kasus penggunaan tersebut.
'''
'Hitung pada elemen array 1D berikut:'

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

'Hitung elemen array 2D berikut:'

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)