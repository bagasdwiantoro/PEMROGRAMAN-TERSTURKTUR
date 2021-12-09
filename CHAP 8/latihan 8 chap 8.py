Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
harga_buah ={'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def ratarata_harga_buah(x) :
    y=list(x.values())
    v= sum(y)/len(y)
    print("rata-rata harga buaha adalah Rp " , v)

ratarata_harga_buah(harga_buah)


    
