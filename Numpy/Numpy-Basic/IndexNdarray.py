'Pengindeksan Array NumPy'

'''
Pengindeksan array sama dengan mengakses elemen array.

Anda dapat mengakses elemen array dengan mengacu pada nomor indeksnya.

Indeks dalam array NumPy dimulai dengan 0, artinya elemen pertama memiliki
 indeks 0, dan yang kedua memiliki indeks 1 dst.
'''

'Dapatkan elemen pertama dari array berikut:'

import numpy as np

arr = np.array([1,2,3,4])

print(arr[0])

'Dapatkan elemen kedua dari larik berikut'

print(arr[1])

'Dapatkan elemen ketiga dan keempat dari larik berikut dan tambahkan.'

print(arr[2] + arr[3])


'''
Akses Array 2-D
Untuk mengakses elemen dari array 2-D, kita dapat menggunakan bilangan bulat
 yang dipisahkan koma yang mewakili dimensi dan indeks elemen.

Pikirkan array 2-D seperti tabel dengan baris dan kolom, 
di mana baris mewakili dimensi dan indeks mewakili kolom.
'''

arr2d = np.array([[1,2,3,4,5,6], [6,5,4,3,2,1]])

print('Element ke 2 dari baris Pertama : ' , arr2d[0,1])

'Akses elemen pada baris ke-2, kolom ke-5:'

print('Element ke 2 dari baris Pertama : ' , arr2d[1,4])


'''
Akses Array 3-D
Untuk mengakses elemen dari array 3-D kita dapat menggunakan bilangan bulat
 yang dipisahkan koma yang mewakili dimensi dan indeks elemen.
'''

'Akses elemen ketiga dari larik kedua dari larik pertama:'

arr3d = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])

print(arr3d[0,1,2])

'''
Contoh Dijelaskan
arr[0, 1, 2]mencetak nilai 6.

Dan inilah alasannya:

# index pertama
Angka pertama mewakili dimensi pertama, yang berisi dua larik:
[[1, 2, 3], [4, 5, 6]]
dan:
[[7, 8, 9], [10, 11, 12]]
Sejak kami memilih 0, kami dibiarkan dengan array pertama:
[[1, 2, 3], [4, 5, 6]]

# index kedua
Angka kedua mewakili dimensi kedua, yang juga berisi dua larik:
[1, 2, 3]
dan:
[4, 5, 6]
Karena kami memilih 1, kami memiliki larik kedua:
[4, 5, 6]


# index ketiga
Angka ketiga mewakili dimensi ketiga, yang berisi tiga nilai:
4
5
6
Karena kami memilih 2, kami mendapatkan nilai ketiga:
6

'''

'''
Pengindeksan Negatif
Gunakan pengindeksan negatif untuk mengakses array dari akhir.
'''

'Cetak elemen terakhir dari redup ke-2:'

arrneg = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('element terakhir dari array kedua: ' , arrneg[1,-1])