'Distribusi Data Acak'
'''
Apa itu Distribusi Data?
Distribusi Data adalah daftar semua nilai yang mungkin, dan seberapa sering setiap nilai muncul.

Daftar tersebut penting ketika bekerja dengan statistik dan ilmu data.

Modul acak menawarkan metode yang mengembalikan distribusi data yang dihasilkan secara acak.
'''

'''
Distribusi Acak
Distribusi acak adalah himpunan bilangan acak yang mengikuti fungsi kerapatan peluang tertentu .

Fungsi Kepadatan Probabilitas: Sebuah fungsi yang menggambarkan probabilitas kontinu. 
yaitu probabilitas semua nilai dalam array.

Kita dapat menghasilkan angka acak berdasarkan probabilitas yang ditentukan menggunakan choice()
metode random modul.

The choice()Metode memungkinkan kita untuk menentukan probabilitas untuk setiap nilai.

Probabilitas ditentukan oleh angka antara 0 dan 1, di mana 0 berarti nilai tidak akan pernah terjadi 
dan 1 berarti nilai akan selalu muncul.
'''

'''
Hasilkan array 1-D yang berisi 100 nilai, di mana setiap nilai harus 3, 5, 7 atau 9.

Probabilitas nilai menjadi 3 ditetapkan menjadi 0,1

Probabilitas nilai menjadi 5 diatur menjadi 0,3

Probabilitas nilai menjadi 7 diatur menjadi 0,6

Probabilitas nilai menjadi 9 diatur menjadi 0
'''

from numpy import random

x = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(100))
print(x)

'''
Jumlah semua angka probabilitas harus 1.

Bahkan jika Anda menjalankan contoh di atas 100 kali, nilai 9 tidak akan pernah muncul.

Anda dapat mengembalikan array dalam bentuk dan ukuran apa pun dengan menentukan bentuk 
di sizeparameter.
'''

'''
Contoh
Contoh yang sama seperti di atas, tetapi mengembalikan array 2D dengan 3 baris, 
masing-masing berisi 5 nilai.
'''
x = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(3,5))
print(x)