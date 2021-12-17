'''
Distribusi Multinomial
Distribusi multinomial adalah generalisasi dari distribusi binomial.

Ini menggambarkan hasil dari skenario multi-nomial tidak seperti binomial 
di mana skenario harus hanya satu dari dua. misalnya Golongan darah suatu populasi, 
hasil lemparan dadu.
'''

'''
Ini memiliki tiga parameter:

n - jumlah hasil yang mungkin (misalnya 6 untuk lemparan dadu).

pvals - daftar probabilitas hasil (mis. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] untuk pelemparan dadu).

size - Bentuk array yang dikembalikan.
'''

'Gambarkan Sample untuk lemparan Dadu'
from numpy import random

x = random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)

'''
Catatan: Sampel multinomial TIDAK akan menghasilkan nilai tunggal! 
Mereka akan menghasilkan satu nilai untuk masing-masing pval.
'''
'''
Catatan: Karena merupakan generalisasi dari distribusi binomial, 
representasi visual dan kesamaan distribusi normalnya sama dengan beberapa distribusi binomial
'''