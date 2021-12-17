'''
Rayleigh Distribution

Distribusi Rayleigh digunakan dalam pemrosesan sinyal.

Ini memiliki dua parameter:

scale - (deviasi standar) memutuskan seberapa datar distribusi akan menjadi default 1.0).

size - Bentuk array yang dikembalikan.
'''

'Gambarkan sampel untuk distribusi rayleigh skala 2 dengan ukuran 2x3:'
from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)

'Visualisasi Distribusi Rayleigh'

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()

'''
Persamaan Antara Distribusi Rayleigh dan Chi Square
Pada unit stddev dan 2 derajat kebebasan rayleigh dan chi kuadrat mewakili distribusi yang sama
'''