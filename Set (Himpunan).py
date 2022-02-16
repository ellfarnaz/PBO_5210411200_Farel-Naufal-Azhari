####################---Set (Himpunan)---##################################

a = [10,20,30,20,40]
s=set(a)
print(s)

Y = set("pemrograman")
print(Y)

q = {1,2,3,4,5} 
print(q)
q.add(6)
q.add("A")
print(q) 
q.update([7,8,9])
print(q)

data = {'a', 'e', 'i', 'o', 'u'}
print(data)

data.discard("e")
print(data)
data.discard("k")
print(data)

data.clear()
print('Data (Setelah clear):', data)

q1 = q.copy()
print(q1) 

data1 = {1,2,3,4}
data2 = {1,2,7,8}
print(data1 & data2) #### "&" ####
data3 = data1.intersection(data2)
print (data3)

data1 = {1,2,3,4}
data2 = {1,2,7,8}
print(data1 - data2) #### "-" ####
data3 = data1.difference(data2)
print (data3)

data1 = {1,2,3,4}
data2 = {1,2,7,8}
print(data1|data2) #### "|" ####
data3 = data1.union(data2)
print (data3)


nilai = frozenset('a', 'i', 'u', 'e', 'o')
print(nilai)
nilai.add('4') #
print(nilai)