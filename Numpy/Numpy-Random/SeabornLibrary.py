'''
Visualisasikan Distribusi Dengan Seaborn

Seaborn adalah pustaka yang menggunakan Matplotlib di bawahnya untuk memplot grafik.
Ini akan digunakan untuk memvisualisasikan distribusi acak.
'''
'Instal Seaborn.'
'Pastikan kamu sudah menginstall python dan pip'
'!pip install seaborn'

'''
Distplot
Distplot adalah singkatan dari distribution plot, 
dibutuhkan sebagai input array dan plot kurva yang sesuai dengan distribusi titik dalam array.
'''

'''
Impor Matplotlib
Impor objek pyplot dari modul Matplotlib dalam kode Anda menggunakan pernyataan berikut:
'''
import matplotlib.pyplot as plt

'''
Impor Seaborn
Impor modul Seaborn dalam kode Anda menggunakan pernyataan berikut:
'''
import seaborn as sns

'Merencanakan Displot'
sns.distplot([0,1,2,3,4,5])
plt.show()

'Membuat Distplot Tanpa Histogram'
sns.distplot([0,1,2,3,4,5], hist=False)
plt.show()

'Catatan: Kami akan menggunakan: sns.distplot(arr, hist=False)untuk memvisualisasikan distribusi acak dalam tutorial ini.'