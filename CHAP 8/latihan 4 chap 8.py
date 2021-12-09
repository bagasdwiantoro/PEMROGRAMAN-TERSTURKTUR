Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
sayur=['bayam','kangkung','wortel','selada']
print('Menu :\nA. Tambah Data Sayur\nB. Hapus Data Sayur\nC. Tampilkan Data Sayur')
b=input("Pilihan Anda : ")
a=b.upper()
if a=='A' :
    sayur.append(input("Nambah Sayur Apa ? : "))
elif a=='B' :
    try:
        x=input("Sayur Apa Yang Ingin Dihapus ? : ")
        sayur.remove(x)
    except ValueError :
        print("Data Sayur Tidak Ada")
elif a=='C' :
    print(sayur)
else :
    print("pilihan anda salah , harap coblos lagi")