'''
Menyaring Array
Mengeluarkan beberapa elemen dari larik yang ada dan 
membuat larik baru darinya disebut dengan filtering .

Di NumPy, Anda memfilter array menggunakan boolean index list .
'''

'Sebuah daftar index boolean adalah daftar boolean sesuai dengan indeks dalam array.'

'''
Jika nilai pada indeks adalah Trueelemen yang terkandung dalam larik yang difilter,
 jika nilai pada indeks itu adalah Falseelemen tersebut dikecualikan dari larik yang difilter.
'''

'Buat array dari elemen pada indeks 0 dan 2:'
import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

'''
Contoh di atas akan kembali [41, 43], mengapa?

Karena filter baru hanya berisi nilai di mana array filter memiliki nilai True, 
dalam hal ini, indeks 0 dan 2.
'''

'''
Membuat Array Filter
Dalam contoh di atas kami mengkodekan nilai True and False,
tetapi penggunaan yang umum adalah membuat larik filter berdasarkan kondisi.
'''

'Buat array filter yang hanya akan mengembalikan nilai yang lebih tinggi dari 42:'

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

'Buat larik filter yang hanya akan mengembalikan elemen genap dari larik asli'
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

'''

Membuat Filter Langsung Dari Array
Contoh di atas adalah tugas yang cukup umum di NumPy dan NumPy menyediakan cara yang
 bagus untuk mengatasinya.

Kami dapat langsung mengganti array alih-alih variabel yang dapat diubah dalam kondisi
 kami dan itu akan berfungsi seperti yang kami harapkan.
'''
'Buat array filter yang hanya akan mengembalikan nilai yang lebih tinggi dari 42:'
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

'Buat larik filter yang hanya akan mengembalikan elemen genap dari larik asli:'

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
