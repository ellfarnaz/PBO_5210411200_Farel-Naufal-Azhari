#5210411200
#Farel Naufal Azhari

#Multiple Inheritance

#Parent Class 1
class Perhitungan1 :
    def penjumlahan(self, a, b) :
        return a + b

#Parent Class 2
class Perhitungan2 :
    def perkalian(self, a, b) :
        return a * b    

#Child
class Hitung(Perhitungan1, Perhitungan2) :
    def pembagian(self, a, b):
        return a / b    

#Objek
h = Hitung()    
print(h.penjumlahan(10, 5))
print(h.perkalian(1, 3))
print(h.pembagian(6066, 3))
