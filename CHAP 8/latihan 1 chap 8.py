Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=int(input("ANDA INGIN MEMASUKKAN BERAPA BILANGAN : "))
print ('------------------------------------')
b=[]
for i in range (a):
    b.append(int(input("Masukkan Bilangan : ")))
b.sort(reverse=True)
print(b)