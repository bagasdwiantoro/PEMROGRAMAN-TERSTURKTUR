Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
p=[1,3,4,5,6,7,8]
def dataStat(x) :
    z=[]
    a=round(sum(x)/len(x),2)
    b=max(x)
    c=min(x)
    z.append(a)
    z.append(b)
    z.append(c)
    print(z)
    return z
dataStat(p)