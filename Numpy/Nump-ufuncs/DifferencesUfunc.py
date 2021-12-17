'''
Perbedaan
Selisih diskrit berarti mengurangkan dua unsur yang berurutan.

Misal untuk [1, 2, 3, 4], selisih diskritnya adalah [2-1, 3-2, 4-3] = [1, 1, 1]

Untuk menemukan perbedaan diskrit, gunakan diff()fungsi.
'''

'Hitunglah selisih diskrit dari larik berikut:'
import numpy as np
arr = np.array([10,15,25,5])
newarr = np.diff(arr)
print(newarr)

'Pengembalian: [5 10 -20] karena 15-10=5, 25-15=10, dan 5-25=-20'

'''
Kita dapat melakukan operasi ini berulang kali dengan memberikan parameter n.

Misalnya untuk [1, 2, 3, 4], perbedaan diskrit dengan n = 2 adalah [2-1, 3-2, 4-3] = [1, 1, 1] , 
maka, karena n=2, kita akan melakukannya sekali lagi, dengan hasil baru: [1-1, 1-1] = [0, 0]
'''

'Hitung perbedaan diskrit dari array berikut dua kali:'
arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr, n=2)

print(newarr)

'Pengembalian: [5 -30] karena: 15-10=5, 25-15=10, dan 5-25=-20 DAN 10-5=5 dan -20-10=-30'