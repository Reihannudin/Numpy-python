'''
Distribusi Seragam
Digunakan untuk menggambarkan probabilitas di mana setiap 
peristiwa memiliki peluang yang sama untuk terjadi.

Misalnya Generasi nomor acak.
'''

'''
Ini memiliki tiga parameter:

a - pasti kecil - default 0 .0.

b - pasti besar - default 1.0.

size - Bentuk array yang dikembalikan.
'''
'Buat sampel distribusi seragam 2x3:'
from numpy import random

x = random.uniform(size=(2,3))
print(x)

'Visualisasi Distribusi Uniform'
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000),hist=False)
plt.show()