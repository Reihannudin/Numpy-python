'''
Distribusi Pareto
Distribusi mengikuti hukum Pareto yaitu distribusi 80-20 (20% faktor menyebabkan 80% hasil).
'''
'''
Ini memiliki dua parameter:

a - parameter bentuk.

size - Bentuk array yang dikembalikan.
'''
'''
Gambarkan sampel untuk distribusi pareto dengan bentuk 2 dengan ukuran 2x3:
'''
from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)

'Visualisasi Distribusi Pareto'
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()
