Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Sewa Mobil Selama 12 Jam = Rp 200.000,00
#Sewa Berikutnya = 10.000 / Jam
#Jika customer menyewa mobil dari jam 06,00 sampai jam 23,50 , maka total tarif yang harus dibayar adalah ?
# Menghitung Lama Sewa
JamAkhirSewa=23 + (50/60)
JamAwalSewa=6.00
LamaSewa=JamAkhirSewa-JamAwalSewa
print ("lama sewa mobil adalah ",
          (round(LamaSewa,2)),
           "  jam") 
#Menghitung Total Tarif
TarifSewaAwal=200000
TarifSewaSetelahnya=10000
TotalTarif=TarifSewaAwal + (LamaSewa-12)*TarifSewaSetelahnya
print ("total tarif yang harus dibayarkan adalah ",
       (round(TotalTarif,-2)),
       " rupiah")
