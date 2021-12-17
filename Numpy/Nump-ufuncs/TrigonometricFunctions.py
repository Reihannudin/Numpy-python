'''
Fungsi trigonometri
NumPy menyediakan ufuncs sin(), cos() dan tan()
yang mengambil nilai dalam radian dan menghasilkan nilai sin, 
cos dan tan yang sesuai.
'''
'Cari nilai sinus PI/2:'
import numpy as np

x = np.sin(np.pi/2)

print(x)

'Temukan nilai sinus untuk semua nilai di arr:'
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)

'''
Ubah Derajat Menjadi Radian
Secara default semua fungsi trigonometri mengambil radian 
sebagai parameter tetapi kita dapat mengonversi radian ke 
derajat dan sebaliknya juga di NumPy.
'''
'Catatan: nilai radian adalah pi/180 * derajat_nilai.'

'Ubah semua nilai dalam array arr berikut ke radian:'
arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)

'Radian ke Derajat'

'Ubah semua nilai dalam array arr berikut ke derajat:'
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)

'''
Menemukan Sudut
Mencari sudut dari nilai sinus, cos, tan. Misal sin, cos dan tan invers 
(arcsin, arccos, arctan).

NumPy menyediakan ufuncs arcsin(), arccos()dan arctan() 
yang mengh
'''
'Tentukan sudut 1,0:'
x = np.arcsin(1.0)

print(x)

'Sudut Setiap Nilai dalam Array'
'Temukan sudut untuk semua nilai sinus dalam array'
arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)

'''
sisi miring
Menemukan sisi miring menggunakan teorema pythagoras di NumPy.

NumPy menyediakan hypot()fungsi yang mengambil nilai dasar dan tegak lurus 
dan menghasilkan sisi miring berdasarkan teorema pythagoras.
'''
'Cari hipotenue untuk 4 alas dan 3 tegak lurus:'
base = 3
perp = 4

x = np.hypot(base, perp)

print(x)