Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dataFile = open('databil.txt', 'r')
for i in dataFile:
    ambil = i.split('|')
    hasil = int(ambil[0]) + int(ambil[1])
    print(hasil)

dataFile.close()


