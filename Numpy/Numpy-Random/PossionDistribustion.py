'''
Distribusi racun
Distribusi Poisson adalah Distribusi Diskrit .

Ini memperkirakan berapa kali suatu peristiwa dapat terjadi dalam waktu tertentu. 
misalnya jika seseorang makan dua kali sehari berapa probabilitas dia akan makan tiga kali?
'''

'''
Ini memiliki dua parameter:

lam - tingkat atau jumlah kejadian yang diketahui misalnya 2 untuk masalah di atas.

size - Bentuk array yang dikembalikan.
'''

import numpy 
from numpy import random

x = random.poisson(lam=2, size=10)
print(x)

'Visualisasi Distribusi Poisson'
import matplotlib.pyplot as plt
import seaborn as sns


sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()

'''
Perbedaan Antara Distribusi Normal dan Poisson
Distribusi normal kontinu sedangkan poisson diskrit.

Tetapi kita dapat melihat bahwa mirip dengan binomial untuk 
distribusi poisson yang cukup besar akan menjadi mirip dengan 
distribusi normal dengan std dev dan mean tertentu.
'''
sns.distplot(random.normal(loc=50,scale=7,size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist= False, label='poisson')

plt.show()

'''
Perbedaan Antara Poisson dan Distribusi Binomial
Perbedaannya sangat tipis, distribusi binomial untuk uji diskrit, 
sedangkan distribusi poisson untuk uji kontinu.

Tetapi untuk distribusi binomial yang sangat besar nd an mendekati nol p hampir identik 
dengan distribusi poisson sehingga n * phampir sama dengan lam.
'''

sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binominal')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()
