####################---Dictionary---##################################

d={1:100, 2:200, 3:300, 4:400, 5:500}
print('1',d)
print("2",d[2])
print('3',d.get(4))
print('4',d.keys())
print('5',d.values())
del d[1]
print('6',d)

b=d.copy()
print('7',b)
print('8',d.clear())
print('9',len(d))


t=(100,200,300,400)
print('10',t[0])
print('11',t[3])

print('15',t.index(200))

t2=(10,20,10,30,10,40,20)
print(t2)
print('12',t.count(10))
print('13',t2.count(20))
print('14',t2.count(10))
print('15',t.count(30))
print('16',t2.count(30))
