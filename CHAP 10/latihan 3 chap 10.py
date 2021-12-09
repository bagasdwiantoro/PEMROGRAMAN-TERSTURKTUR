Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
file = open("file.txt", "r")
readFile = file.readlines()
dataMhs = []

for i in range(len(readFile)):
    data = readFile[i].rstrip("\n")
    pecahData = data.split("|")
    dataDict = {'nim':pecahData[0], 'nama':pecahData[1], 'alamat':pecahData[2]}
    dataMhs.append(dataDict)

print(f'dataMhs = {dataMhs}')
file.close()
