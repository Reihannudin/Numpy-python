'''
Bergabung dengan NumPy Array
Bergabung berarti menempatkan isi dari dua atau lebih 
array dalam satu array.

Dalam SQL kami menggabungkan tabel berdasarkan kunci,
 sedangkan di NumPy kami menggabungkan array dengan sumbu.

Kami melewati urutan array yang ingin kami gabungkan 
ke concatenate()fungsi, bersama dengan sumbu.
Jika sumbu tidak dilewatkan secara eksplisit, itu diambil sebagai 0.
'''

'Bergabunglah dengan dua array'
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

'Gabungkan dua larik 2D di sepanjang baris (sumbu=1):'

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

'''
Bergabung dengan Array Menggunakan Fungsi Stack
Penumpukan sama dengan penggabungan, satu-satunya perbedaan adalah
bahwa penumpukan dilakukan di sepanjang sumbu baru.

Kita dapat menggabungkan dua larik 1-D di sepanjang sumbu kedua 
yang akan menghasilkan menempatkannya satu di atas yang lain,
yaitu. menumpuk.

Kami melewati urutan array yang ingin kami gabungkan ke stack()
metode bersama dengan sumbu. Jika sumbu tidak dilewatkan secara
eksplisit, itu diambil sebagai 0.
'''
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

'''
Susun Sepanjang Baris
NumPy menyediakan fungsi pembantu: hstack() untuk menumpuk di sepanjang baris.
'''

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)

'''
Penumpukan Sepanjang Kolom
NumPy menyediakan fungsi pembantu: vstack()  untuk menumpuk di sepanjang kolom.
'''
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)

'''
Susun Sepanjang Tinggi (kedalaman)
NumPy menyediakan fungsi pembantu: dstack() untuk menumpuk di sepanjang ketinggian,
 yang sama dengan kedalaman.
'''
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)
