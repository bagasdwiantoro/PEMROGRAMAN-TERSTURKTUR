Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from datetime import *

def diffDate(x):
    now = datetime.date(datetime.now())
    x = datetime.strptime(x, '%Y-%m-%d').date()
    return abs((x - now).days)

print('Selisih harinya adalah {0} hari'.format(diffDate('2022-01-01')))