#5210411200
#Farel Naufal Azhari

#Multilevel Inheritance

#Parent Class
class Hewan :
    def bersuara(self) :
        print("Kucing Bersuara")

# child class dari hewan
class Kucing(Hewan) :
    def suara(self) :   
        print("Meong...")

# child class dari kucing
class AnakKucing(Kucing) :
    def minum(self) :   
        print("Minum Susu")

#Objek
cat = AnakKucing()
cat.bersuara()
cat.suara()
cat.minum()