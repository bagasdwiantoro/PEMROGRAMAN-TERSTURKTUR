Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
def suffleString(x, n):
    randomString=[]
    i = 0
    while i < n:
        if (''.join(random.sample(x,len(x)))) not in randomString:
            randomString.append(''.join(random.sample(x,len(x))))
            i += 1
    print(randomString)

suffleString('aku', 2)
suffleString('aku', 3)
suffleString('aku', 4)
