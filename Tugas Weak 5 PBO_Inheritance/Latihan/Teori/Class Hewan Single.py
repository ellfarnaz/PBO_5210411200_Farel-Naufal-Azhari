#5210411200
#Farel Naufal Azhari

#Single Inheritance

# Class Parent
class Hewan :   
    def bersuara(self) :
        print("Kucing Bersuara")

# child class dari hewan
class Kucing(Hewan) :
    def suara(self) :
        print("Meong...")

#Objek
Cat = Kucing()
Cat.suara()
Cat.bersuara()

