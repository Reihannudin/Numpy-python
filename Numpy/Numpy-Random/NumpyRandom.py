'''
Apa itu Angka Acak?
Nomor acak TIDAK berarti nomor yang berbeda setiap saat. 
Acak berarti sesuatu yang tidak dapat diprediksi secara logis.
'''

'''
Pseudo Random dan True Random.
Komputer bekerja pada program, dan program adalah kumpulan instruksi yang pasti.
Jadi itu berarti harus ada beberapa algoritma untuk menghasilkan angka acak juga.

Jika ada program untuk membangkitkan bilangan acak maka dapat diprediksi,
sehingga tidak benar-benar acak.

Angka acak yang dihasilkan melalui algoritma generasi disebut pseudo random .

Bisakah kita membuat angka yang benar-benar acak?

Ya. Untuk menghasilkan angka yang benar-benar acak di komputer kita, 
kita perlu mendapatkan data acak dari beberapa sumber luar. 
Sumber luar ini umumnya adalah penekanan tombol, gerakan mouse, data di jaringan, dll.

Kami tidak membutuhkan angka yang benar-benar acak, kecuali yang terkait dengan keamanan (misalnya kunci enkripsi) atau dasar penerapannya adalah keacakan (misalnya roda roulette digital).

Dalam tutorial ini kita akan menggunakan nomor acak semu.
'''

'''
Hasilkan Nomor Acak
NumPy menawarkan randommodul untuk bekerja dengan angka acak.
'''
from numpy import random

'Hasilkan Bilangan bulat acak dari 0 hingga 100'
x = random.randint(100)
print(x)

'Hasilkan Float Acak'
'Metode modul acak rand()mengembalikan float acak antara 0 dan 1.'

x = random.rand()
print(x)


'''
Hasilkan Array Acak

Di NumPy kami bekerja dengan array, dan Anda dapat menggunakan dua metode 
dari contoh di atas untuk membuat array acak.
'''
'''
bilangan bulat
The randint()Metode mengambil size parameter di mana Anda dapat menentukan 
bentuk array.
'''
'Hasilkan larik 1-D yang berisi 5 bilangan bulat acak dari 0 hingga 100:'
x = random.randint(100, size=(5))
print(x)

'Hasilkan array 2-D dengan 3 baris, setiap baris berisi 5 bilangan bulat acak dari 0 hingga 100:'
x = random.randint(100, size=(3,5))
print(x)


'''
mengapung
The rand()Metode ini juga memungkinkan Anda untuk menentukan bentuk array.
'''
'Hasilkan array 1-D yang berisi 5 float acak:'
x = random.rand(5)
print(x)

'Hasilkan array 2-D dengan 3 baris, setiap baris berisi 5 angka acak:'
x = random.rand(3,5)
print(x)

'''
Hasilkan Nomor Acak Dari Array
The choice()Metode memungkinkan Anda untuk menghasilkan nilai acak 
berdasarkan sebuah array nilai.

The choice()Metode mengambil array sebagai parameter dan secara acak 
mengembalikan salah satu nilai.
'''

'Kembalikan salah satu nilai dalam array:'
x = random.choice([3,5,7,9])
print(x)

'''
The choice()Metode juga memungkinkan Anda untuk mengembalikan berbagai nilai.

Tambahkan sizeparameter untuk menentukan bentuk array.
'''

'Buat larik 2D yang terdiri dari nilai dalam parameter larik (3, 5, 7, dan 9):'
x = random.choice([3,5,7,9] , size=(3,5))
print(x)