####################---LIST---##################################
list=[0,1,2,3,4,5,6,7,8,9]
print("1",list[5])

print("2",list[:3])

print('3',len(list))

print('4',list[10-3:])

print('5',list[2:9])

print('6',list[-10])

list.append(10)
print('7',list)

list.insert(1,11)
print('8',list)

list2=['Halo']
list.extend(list2)
print('9',list)

list.extend('hai')
print('10',list)

del list[1]
print('11',list)

list.remove(10)
print('12',list)

list.pop()
print('13',list)

list.pop(2)
print('14',list)

print()
a=[50,10,20,30,40]
b=sorted(a)
print('1',b)

a.sort(reverse=True)
print('2',a)

print("3 Min",min(a),"Max",max(a))
