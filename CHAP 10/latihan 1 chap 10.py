Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 file = open('datacp10.txt', 'r')

ganjil = 0
genap = 0 

for i in file :
    teks = int(i)
    if teks % 2 == 0 :
        genap += 1
    else :
        ganjil += 1

print(f'Banyak bilangan genap   : {genap}')
print (f'Banyak bilangan ganjil  : {ganjil}')

file.close()
