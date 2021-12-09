Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=int(input("MASUKKAN JUMLAH MAHASISWA = "))
print('-------------------')
i=0
a=[]
for i in range(n) :
    a.append(input("Nama Mahasiswa = "))
    a.sort()
for i in range(n) :
    print(a[i],'(',len(a[i]), ' karakter )')