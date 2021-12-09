Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
file = open("file.txt", "a+")

while True:
    nim = input('\nMasukkan NIM           :')
    nama = input('Masukkan Nama Mhs      :')
    alamat = input('Masukkan Alamat        :')
    file.write((f'{nim}|{nama}|{alamat}\n'));
    file.seek(0,0)
    ulangi = input('\nUlangi input lagi [y/n] :')
    if ulangi.lower() not in 'y': break

print(f'\n{file.read()}')

file.close()
