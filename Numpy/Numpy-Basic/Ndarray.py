'Numpy membuat Array'

'''
Buat Objek NumPy ndarray
NumPy digunakan untuk bekerja dengan array. Objek array di NumPy disebut ndarray.

Kita dapat membuat ndarrayobjek NumPy dengan menggunakan array()fungsi.
'''

'Contoh menggunakan List untuk membuat array numpy'
import numpy as np 

arr = np.array([1,2,3,4,5])

print(arr)

print(type(arr))

''''
type(): Fungsi Python bawaan ini memberi tahu kita jenis objek yang diteruskan ke sana.
Seperti pada kode di atas itu menunjukkan bahwa arradalah numpy.ndarraytipe.
'''

'''
Untuk membuat ndarray, kita dapat meneruskan daftar, tuple, atau objek seperti array apa
 pun ke dalam array() metode, dan itu akan diubah menjadi ndarray:
'''

'Contoh : Gunakan Tuple untuk membuat array NumPy:'
arrt =  np.array([3,4,5,6,7])

print(arrt)


'''
Dimensi dalam Array
Dimensi dalam array adalah satu tingkat kedalaman array (Nested Array).
'''

'Nested Array adalah array yang memiliki array sebagai elementnya'

'''
Array 0-D
Array 0-D, atau Skalar, adalah elemen dalam array. 
Setiap nilai dalam array adalah array 0-D.
'''

'Contoh buat Array 0-D dengan nilai 41'

arr0d = np.array(41)

print(arr0d)


'''
Array 1-D
Array yang memiliki array 0-D sebagai elemennya 
disebut array uni-dimensi atau 1-D.

Ini adalah array yang paling umum dan dasar.
'''
'Buat larik 1-D yang berisi nilai 1,2,3,4,5:'

arr1d = np.array([4,2,7,6,9])

print(arr1d)


'''
Array 2-D
Array yang memiliki array 1-D sebagai elemennya 
disebut array 2-D.

Ini sering digunakan untuk mewakili matriks 
atau tensor orde ke-2.
'''

'''NumPy memiliki seluruh sub modul yang didedikasikan
 untuk operasi matriks yang disebut numpy.mat'''

arr2d = np.array([[1,2,3], [4,5,6]]) 

print(arr2d)


'''
Array 3-D
Array yang memiliki array 2-D (matriks) sebagai 
elemennya disebut array 3-D.

Ini sering digunakan untuk mewakili tensor orde ke-3.
'''
'''
Buat larik 3-D dengan dua larik 2D,
keduanya berisi dua larik dengan nilai 1,2,3 dan 4,5,6:
'''

arr3d = np.array([[[1,2,3], [4,5,6]], [[6,5,4],[3,2,1]]])

print(arr3d)


'''
Periksa Jumlah Dimensi?
NumPy Arrays menyediakan ndim atribut yang mengembalikan 
bilangan bulat yang memberi tahu kita berapa banyak dimensi 
yang dimiliki array.
'''

'Periksa berapa banyak dimensi yang dimiliki array:'

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


'''
Array Dimensi Lebih Tinggi
Array dapat memiliki sejumlah dimensi.

Saat array dibuat, Anda dapat menentukan jumlah dimensi dengan
menggunakan ndmin argumen.
'''

andimn = np.array([1,2,3,4], ndmin=5)

print(andimn)
print('number of dimensions : ', andimn.ndim)