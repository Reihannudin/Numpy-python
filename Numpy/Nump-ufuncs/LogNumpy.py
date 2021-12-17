'''
Log
NumPy menyediakan fungsi untuk melakukan log di basis 2, e dan 10.

Kami juga akan mengeksplorasi bagaimana kami dapat mengambil log 
untuk basis apa pun dengan membuat ufunc khusus.

Semua fungsi log akan menempatkan -inf atau inf dalam elemen jika 
log tidak dapat dihitung.
'''

'''
Masuk di Basis 2
Gunakan log2() fungsi untuk melakukan log di basis 2.
'''
'Temukan log di basis 2 dari semua elemen array berikut:'
import numpy as np
arr = np.arange(1, 10)

print(np.log2(arr))

'''
Catatan: The arange(1, 10)mengembalikan fungsi array dengan bilangan
 bulat mulai dari 1 (termasuk) ke 10 (tidak termasuk).
'''

'''
Masuk di Basis 10
Gunakan log10()fungsi untuk melakukan log di basis 10.
'''
'Temukan log di basis 10 dari semua elemen array berikut:'
arr = np.arange(1, 10)

print(np.log10(arr))


'''
Natural Log, or Log at Base e
Menggunakan log()fungsi untuk melakukan log di pangkalan e.
'''
arr = np.arange(1, 10)

print(np.log(arr))

'''
Masuk ke Pangkalan Apa Saja
NumPy tidak menyediakan fungsi apa pun untuk mengambil log di basis mana pun, 
jadi kita dapat menggunakan frompyfunc() fungsi tersebut bersama dengan fungsi
bawaan math.log() dengan dua parameter input dan satu parameter output:
'''
from math import log 
nplog = np.frompyfunc(log, 2,1)

print(nplog(100, 15))
