'''
Distribusi Binomial
Distribusi Binomial adalah Distribusi Diskrit .

Ini menggambarkan hasil dari skenario biner, misalnya lemparan koin, 
itu akan menjadi kepala atau ekor.
'''
'''
Ini memiliki tiga parameter:

n - jumlah percobaan.

p - probabilitas terjadinya setiap percobaan (misalnya untuk lemparan koin 0,5 masing-masing).

size - Bentuk array yang dikembalikan.
'''
'''
Distribusi Diskrit: Distribusi didefinisikan pada rangkaian peristiwa yang terpisah, '
misalnya hasil lemparan koin adalah diskrit karena hanya dapat berupa kepala atau ekor 
sedangkan tinggi orang kontinu seperti dapat 170, 170.1, 170.11 dan seterusnya.
'''

'''
Diberikan 10 percobaan untuk lempar koin menghasilkan 10 poin data:
'''
import numpy
from numpy import random

x = random.binomial(n=10, p=0.5, size=10)
print(x)

'Visualisasi Distribustion Binominal'

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5,size=1000), hist=True, kde=False)

plt.show()

'''
Perbedaan Distribusi Normal dan Binomial
Perbedaan utama adalah bahwa distribusi normal kontinu sedangkan binomial diskrit, 
tetapi jika ada titik data yang cukup akan sangat mirip dengan distribusi normal 
dengan lokasi dan skala tertentu.
'''
'contoh'
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label="normal")
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()