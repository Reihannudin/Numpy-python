'''
Mencari GCD (Denominator Persekutuan Terbesar)
FPB (Penyebut Persekutuan Terbesar), juga dikenal sebagai HCF (Faktor Persekutuan Tertinggi) 
adalah bilangan terbesar yang merupakan faktor persekutuan dari kedua bilangan tersebut.
'''
'Tentukan KPK dari dua bilangan berikut:'
import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x)
'Pengembalian: 3 karena itu adalah angka tertinggi, kedua angka dapat dibagi (6/3=2 dan 9/3=3).'

'''
Menemukan GCD dalam Array
Untuk menemukan Faktor Persekutuan Tertinggi dari semua nilai dalam array, 
Anda dapat menggunakan reduce() metode.
'''
'''
The reduce() Metode akan menggunakan ufunc, dalam hal ini gcd() fungsi, pada setiap elemen, 
dan mengurangi array dengan satu dimensi.
'''
'Temukan GCD untuk semua angka dalam larik berikut:'
arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)

'Pengembalian: 4 karena itu adalah angka tertinggi, semua nilai dapat dibagi.'