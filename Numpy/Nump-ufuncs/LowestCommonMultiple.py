'''
Mencari KPK (Kelipatan Persekutuan Terendah)

Kelipatan Persekutuan Terkecil adalah bilangan terkecil 
yang merupakan kelipatan persekutuan dari kedua bilangan tersebut.
'''
'Tentukan KPK dari dua bilangan berikut:'
import numpy as np

num1 = 4 
num2 = 6
x = np.lcm(num1, num2)
print(x)

'''
Pengembalian: 12 karena itu adalah kelipatan persekutuan terendah 
dari kedua angka (4*3=12 dan 6*2=12).
'''

'''
Menemukan KPK dalam Array

Untuk menemukan Kelipatan Persekutuan Terendah dari semua nilai dalam array,
Anda dapat menggunakan reduce()metode.
'''
'''
The reduce()Metode akan menggunakan ufunc, dalam hal ini lcm()fungsi, 
pada setiap elemen, dan mengurangi array dengan satu dimensi.
'''

'Carilah KPK dari nilai-nilai array berikut:'
arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)

'Pengembalian: 18 karena itu adalah kelipatan persekutuan terkecil dari ketiga angka (3*6=18, 6*3=18 dan 9*2=18).'

'Temukan KPK dari semua array di mana array berisi semua bilangan bulat dari 1 hingga 10:'

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)