Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 def bintang(n):
    space = 2*n-1
    n = (-(-n//2))
    for i in range(0, n):
        print((''(2*i+1)).center(space))
    for i in reversed(range(0, n)):
        print((''(2*i-1)).center(space))
bintang(7)

