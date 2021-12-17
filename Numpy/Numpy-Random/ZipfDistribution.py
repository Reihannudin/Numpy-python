'''
Distribusi Zipf digunakan untuk mengambil sampel data berdasarkan hukum zipf.
'''
'''
Hukum Zipf: Dalam kumpulan, suku ke-n adalah 1/n kali suku paling umum. 
Misalnya kata umum ke-5 dalam bahasa Inggris telah muncul hampir 1/5 kali 
dari kata yang paling sering digunakan.
'''
'''
Ini memiliki dua parameter:

a - parameter distribusi.

size - Bentuk array yang dikembalikan.
'''
'Gambarkan contoh distribusi zipf dengan parameter distribusi 2 dengan ukuran 2x3:'

from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)

'Visualisasi Distribusi Zipf'
'Contoh 1000 poin tetapi plot hanya satu dengan nilai < 10 untuk grafik yang lebih bermakna.'
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()