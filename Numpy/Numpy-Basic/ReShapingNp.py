'Pembentukan Ulang Array NumPy'

'''
Membentuk kembali array
Reshaping berarti mengubah bentuk array.

Bentuk array adalah jumlah elemen dalam setiap dimensi.

Dengan membentuk kembali kita dapat menambah atau menghapus dimensi
 atau mengubah jumlah elemen di setiap dimensi.
'''

'''
Bentuk Ulang Dari 1-D ke 2-D
Konversikan larik 1-D berikut dengan 12 elemen menjadi larik 2-D.

Dimensi terluar akan memiliki 4 array, masing-masing dengan 3 elemen:
'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)


'''
Bentuk Ulang Dari 1-D ke 3-D

Konversikan larik 1-D berikut dengan 12 elemen menjadi larik 3-D.

Dimensi terluar akan memiliki 2 larik yang berisi 3 larik, masing-masing dengan 2 elemen:
'''
newarr = arr.reshape(2, 3, 2)

print(newarr)


'''
Bisakah Kita Membentuk Kembali Ke Bentuk Apapun?
Ya, selama elemen yang diperlukan untuk membentuk kembali sama di kedua bentuk.

Kita dapat membentuk ulang 8 elemen larik 1D menjadi 4 elemen dalam 2 baris larik 2D tetapi
 kita tidak dapat membentuknya kembali menjadi 3 elemen 3 baris larik 2D karena akan membutuhkan
 3x3 = 9 elemen.
'''

'''
Coba ubah array 1D dengan 8 elemen menjadi array 2D dengan 3 elemen di setiap dimensi (akan memunculkan kesalahan):

# Error
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(3, 3)

print(newarr)
'''

'''
Mengembalikan Salin atau Lihat?

Periksa apakah array yang dikembalikan adalah salinan atau tampilan:
'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

'Contoh di atas mengembalikan array asli, jadi ini adalah tampilan.'

'''
Dimensi Tidak Diketahui
Anda diperbolehkan memiliki satu dimensi "tidak diketahui".

Artinya Anda tidak perlu menentukan angka pasti untuk salah satu dimensi dalam metode reshape.

Lulus -1sebagai nilainya, dan NumPy akan menghitung angka ini untuk Anda.
'''
'Konversi array 1D dengan 8 elemen ke array 3D dengan elemen 2x2:'

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

'Catatan: Kami tidak dapat melewati -1lebih dari satu dimensi.'

'''
Flattening array
Flattening array berarti mengubah array multidimensi menjadi array 1D.

Kita bisa gunakan reshape(-1)untuk melakukan ini.
'''
'ubah Array menjadi Array 1D'

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)