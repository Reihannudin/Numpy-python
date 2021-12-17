'''
Distribusi eksponensial

Distribusi eksponensial digunakan untuk menggambarkan waktu sampai 
peristiwa berikutnya misalnya kegagalan/keberhasilan dll.
'''

'''
Ini memiliki dua parameter:

scale - kebalikan dari tingkat ( lihat lam dalam distribusi poisson ) default ke 1.0.

size - Bentuk array yang dikembalikan.
'''

'Buatlah contoh untuk distribusi eksponensial dengan skala 2.0 dengan ukuran 2x3:'

from numpy import random

x = random.exponential(scale=2, size=(2,3))
print(x)

'''
Visualisasi Distribusi Eksponensial
'''
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size=1000), hist = False)

plt.show()

'''
Hubungan Antara Poisson dan Distribusi Eksponensial
Distribusi Poisson berkaitan dengan jumlah kejadian suatu peristiwa 
dalam periode waktu sedangkan distribusi eksponensial berkaitan dengan
waktu antara peristiwa-peristiwa ini.
'''