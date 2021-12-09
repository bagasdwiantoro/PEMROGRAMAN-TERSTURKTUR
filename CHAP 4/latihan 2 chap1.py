Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Jarak Kota A ke Kota C adalah 795 Km
#Satu liter bbm bisa menempuh 12 km
#Berapa liter yang diperlukan oleh mobil pak budi agar sampai dari kota a ke kota c ?
Jarak=795
BensinPerKilo=1/12
BanyakBensinYangDiperlukan=Jarak*BensinPerKilo
print (" Banyak bensin yang diperlukan oleh mobil Pak Budi adalah " ,
        round (BanyakBensinYangDiperlukan,1),
         (" liter " ))