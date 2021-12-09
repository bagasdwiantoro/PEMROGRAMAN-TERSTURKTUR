Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from datetime import *

# Membuka file, dengan mode a+ (dibaca dan ditulis)
file = open("dataPeminjam.txt", "a+")

# Variable untuk menyimpan waktu saat ini
now = datetime.date(datetime.now())

# Variable untuk menyatakan maksimal pengembalian
maks = datetime.date(datetime.now()) + timedelta(days=7)

# Looping untuk input data
while True:
    kode, nama, buku = input("\nMasukkan Kode Member : "), input("Masukkan Nama Member : "), input("Masukkan Judul Buku  : ")
    file.write((f'{kode}|{nama}|{buku}|{now}|{maks}\n'))
    again = input("\nUlangi lagi (y/n) ? : ")
    if again.lower() != 'y': break

# Menutup file
file.close()