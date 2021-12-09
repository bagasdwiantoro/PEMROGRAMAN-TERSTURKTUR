Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 dataFile = open('datamahasiswa.txt', 'r')
data = dataFile.read()
data = data.replace('|', ' ')
data = data.replace('\n', ' ')
data = data.split(' ')

while True:
    cari = input('Masukkan NIM yang mau dicari : ')
    if cari in data:
        search = data.index(cari)
        print('Data Mahasiswa')
        print('NIM            : ', data[search])
        print('Nama Mahasiswa : ', data[search + 1])
        print('Alamat         : ', data[search + 2])
    else:
        print('Data tidak ditemukan')

    lagi = input('Ulangi lagi (y/n) ? ')
    lagi = lagi.lower()
    if lagi in ('N', 'n'):
        break
