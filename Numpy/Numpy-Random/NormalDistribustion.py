'''
Distribusi normal
Distribusi Normal adalah salah satu distribusi yang paling penting.

Ini juga disebut Distribusi Gauss setelah matematikawan Jerman Carl Friedrich Gauss.

Ini cocok dengan distribusi probabilitas banyak peristiwa, misalnya. Skor IQ, Detak Jantung, dll.

Gunakan random.normal()metode untuk mendapatkan Distribusi Data Normal.
'''

'''
Ini memiliki tiga parameter:

loc - (Mean) di mana puncak bel ada.

scale - (Standar Deviasi) seberapa datar distribusi grafik seharusnya.

size - Bentuk array yang dikembalikan.
'''
'Hasilkan distribusi normal acak ukuran 2x3:'
import numpy
from numpy import random

x = random.normal(size=(2,3))
print(x)

print('--------------------------------------')
'Hasilkan distribusi normal acak berukuran 2x3 dengan mean pada 1 dan standar deviasi 2:'
x = random.normal(loc=1, scale=2, size=(2,3))
print(x)

'Visualisasi Distribusi Normal'
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)
plt.show()

'Catatan: Kurva Distribusi Normal juga dikenal sebagai Kurva Lonceng karena kurva berbentuk lonceng'