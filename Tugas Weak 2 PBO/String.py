str="aku cinta indonesia"
str=str[:10]+"tanah air ku"+str[9:]
print (str)

str=""
print (str)
######################################################
str1="aku cinta tanah air ku Indonesia"
str1=str1[:9]+""+str1[22:]
print (str1)
######################################################
kelas="Praktikum pemrograman berorientasi objek"
up=kelas.upper()
lo=kelas.lower()
print(kelas)
print(up)
print(lo)
######################################################
txt = "     banana     "
x = txt.strip()
y = txt.lstrip()
z = txt.rstrip()

print("of all fruits", x,"is my favorite")
print("of all fruits", y,"is my favorite")
print("of all fruits", z,"is my favorite")
######################################################
len(kelas)
jumlah=len(kelas)
print("Panjang string adalah ",jumlah)
######################################################
s1="Python"
s2="Programing"
print(s1+s2)
######################################################
print(kelas.index('a'))
######################################################
kelas2=kelas.replace('Praktikum','praktik')
print(kelas2)
######################################################
a='satu'
b='dua'
c='tiga'
print('saya mempunyai %s mangga'% (b))
######################################################
print(kelas2)
print (kelas2.split())
######################################################
hari=input("Hari ini Adalah Hari :")
print(hari)
######################################################
data1=input('angka 1: ')
data2=input('angka 2: ')
hasil=int(data1)*int(data2)
print(data1,'*',data2,'=',hasil)

