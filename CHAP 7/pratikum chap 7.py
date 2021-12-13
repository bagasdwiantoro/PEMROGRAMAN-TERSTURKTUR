def menghitung ():
    try :
        file = open('data.txt','r')
        sum = 0
        for data in file :
            sum = sum + int(data)
        print(sum)
    except ValueError :
        print("data bukan angka")
a=0
a<5
while True :
    menghitung()
    a+=1
    
