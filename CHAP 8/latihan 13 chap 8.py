Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
                        {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
                        {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
                        {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
                        {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
a=dict(nilaiMhs[0])
b=dict(nilaiMhs[1])
c=dict(nilaiMhs[2])
d=dict(nilaiMhs[3])
e=dict(nilaiMhs[4])
nilai_a=(a['mid'] + 2*a['uas'])/3
nilai_b=(b['mid'] + 2*b['uas'])/3
nilai_c=(c['mid'] + 2*c['uas'])/3
nilai_d=(d['mid'] + 2*d['uas'])/3
nilai_e=(e['mid'] + 2*e['uas'])/3
a['nilai akhir'] = nilai_a
b['nilai akhir'] = nilai_b
c['nilai akhir'] = nilai_c
d['nilai akhir'] = nilai_d
e['nilai akhir'] = nilai_e
v=[]
v.append(a)
v.append(b)
v.append(c)
v.append(d)
v.append(e)
v.sort()
print(v)
