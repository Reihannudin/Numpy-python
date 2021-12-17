'''
Distribusi Logistik

Distribusi Logistik digunakan untuk menggambarkan pertumbuhan.

Digunakan secara luas dalam pembelajaran mesin dalam regresi logistik, 
jaringan saraf, dll.
'''

'''
Ini memiliki tiga parameter:

loc- Mean, di mana puncaknya. Standar 0.

scale- standar deviasi, kerataan distribusi. Standar 1.

size - Bentuk array yang dikembalikan.
'''

'Gambarkan sampel 2x3 dari distribusi logistik dengan rata-rata pada 1 dan stddev 2.0:'

from numpy import random

x = random.logistic(loc=1, scale=2, size=(2,3))
print(x)

'Visualisasi Distribusi Logistik'
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size=1000),hist=False)
plt.show()


'''
Perbedaan Antara Distribusi Logistik dan Normal
Kedua distribusi hampir identik, tetapi distribusi logistik memiliki lebih banyak area di bawah ekor.
 yaitu. Ini mewakili lebih banyak kemungkinan terjadinya suatu peristiwa lebih jauh dari rata-rata.

Untuk nilai skala yang lebih tinggi (standar deviasi) distribusi normal dan logistik hampir identik terlepas dari puncaknya.
'''
sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show()