'Tipe Data NumPy'

'''
Tipe Data dengan Python
Secara default Python memiliki tipe data ini:

strings- digunakan untuk mewakili data teks, teks diberikan di bawah tanda kutip. misalnya "ABD"
integer- digunakan untuk mewakili bilangan bulat. misalnya -1, -2, -3
float- Digunakan untuk menyatakan bilangan real. misalnya 1.2, 42.42
boolean - digunakan untuk mewakili Benar atau Salah.
complex- Digunakan untuk merepresentasikan bilangan kompleks. misalnya 1.0 + 2.0j, 1.5 + 2.5j
'''

'''
Tipe Data di NumPy
NumPy memiliki beberapa tipe data tambahan, dan merujuk ke tipe data dengan satu karakter, 
 i untuk bilangan bulat, u untuk bilangan bulat yang tidak ditandatangani, dll.

Di bawah ini adalah daftar semua tipe data di NumPy dan karakter yang digunakan untuk mewakilinya.

i - bilangan bulat
b - boolean
u - bilangan bulat tak bertanda
f - mengambang
c - pelampung kompleks
m - delta waktu
M - tanggal Waktu
O - objek
S - rangkaian
U - string unicode
V - potongan memori tetap untuk tipe lain (void)
'''

'''
Memeriksa Tipe Data Array
Objek array NumPy memiliki properti yang disebut dtype yang mengembalikan tipe data array:
'''
'Dapatkan tipe data object'
import numpy as np 

arrINT = np.array([1,2,3,4])

print(arrINT.dtype)

'Dapatkan tipe data array yang berisi string:'
arrSTR = np.array(["Nam Do-san","Kim Yong-san.", " Lee Chul-san"])

print(arrSTR.dtype)


'Membuat Array Dengan Tipe Data yang Ditetapkan'
'''
Kami menggunakan array()fungsi untuk membuat array, fungsi ini dapat mengambil argumen opsional:
 dtype yang memungkinkan kami untuk menentukan tipe data yang diharapkan dari elemen array
'''
'Buat array dengan tipe data string:'
arrts = np.array([1, 2, 3, 4], dtype='S')

print(arrts)
print(arrts.dtype)


'Untuk i, u, f, Sdan Ukita dapat mendefinisikan ukuran juga.'
arrti = np.array([1, 2, 3, 4], dtype='i4')

print(arrti)
print(arrti.dtype)


'''
Bagaimana jika Nilai Tidak Dapat Dikonversi?
Jika suatu tipe diberikan di mana elemen tidak dapat dicor maka NumPy 
akan menaikkan ValueError.
'''

'''
ValueError: Dalam Python ValueError dimunculkan ketika jenis argumen 
yang diteruskan ke suatu fungsi tidak terduga/salah.
'''
'''
Contoh :
String non integer seperti 'a' tidak dapat dikonversi ke
 integer (akan menimbulkan kesalahan):
'''
#  arr = np.array(['a', '2', '3'], dtype='i')  Error


'''
Mengonversi Tipe Data pada Array yang Ada

Cara terbaik untuk mengubah tipe data array yang ada, adalah dengan membuat
 salinan array dengan astype()metode.

The astype()fungsi membuat salinan dari array, dan memungkinkan Anda untuk 
menentukan tipe data sebagai parameter.

Tipe data dapat ditentukan menggunakan string, seperti 'f'untuk float, 
'i'untuk integer dll. Atau Anda dapat menggunakan tipe data secara langsung
 seperti floatuntuk float dan intinteger.
'''

'''
Contoh 
Ubah tipe data dari float menjadi integer dengan menggunakan 'i'nilai parameter:
'''
arrCg = np.array([1.1, 2.1, 3.1])

newarr = arrCg.astype('i')

print(newarr)
print(newarr.dtype)

"Ubah tipe data dari float menjadi integer dengan menggunakan 'i'nilai parameter:"

newarrINT = arrCg.astype(int)

print(newarrINT)
print(newarrINT.dtype)


'Ubah tipe data dari integer ke boolean:'
arrb = np.array([1, 0, 3])

newarrb = arrb.astype(bool)

print(newarrb)
print(newarrb.dtype)