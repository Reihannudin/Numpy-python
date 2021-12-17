'''
Distribusi Chi Square
Distribusi Chi Square digunakan sebagai dasar untuk memverifikasi hipotesis.
'''
'''
Ini memiliki dua parameter:

df - (derajat kebebasan).

size - Bentuk array yang dikembalikan.
'''

'Gambarkan sampel untuk distribusi chi kuadrat dengan derajat kebebasan 2 dengan ukuran 2x3:'
from numpy import random

x = random.chisquare(df=2, size=(2,3))
print(x)

'''
Visualisasi Distribusi Chi Square
'''
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()