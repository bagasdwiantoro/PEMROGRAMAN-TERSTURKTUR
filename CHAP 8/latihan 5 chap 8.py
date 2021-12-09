Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def kuadrat(bil) :
    i=0
    x=[]
    for i in range (len(bil)) :
        x.append(bil[i]**2)
    print(x)

bil=[2,3,4,5]

kuadrat(bil)
        