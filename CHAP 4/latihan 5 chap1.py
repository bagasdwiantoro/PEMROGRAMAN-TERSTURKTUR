Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
%matplotlib inline
gender = ['Perempuan', 'Laki Laki']
jumlah_mhs = [29,41]

plt.figure(figsize=(12,7))
plt.bar(gender, jumlah_mhs, color='red')
plt.title('Jumlah Mahasiswa PTIK Berdasarkan Gender', size=20)
plt.ylabel('Jumlah Mahasiswa', size=16)
plt.xticks(size=13)
plt.yticks(size=13)
plt.show()