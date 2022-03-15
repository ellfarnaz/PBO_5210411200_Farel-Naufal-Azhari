#5210411200
#Farel Naufal Azhari

#Hierarchical Inheritance

#Parent Class
class Induk :
    def fungsiinduk(self) :
        print("Fungsi pada Induk")

# Child Class 1
class Anak1(Induk) :
    def fungsianak1(self) :
        print("Fungsi pada anak pertama")

# Child Class 2
class Anak2(Induk) :
    def fungsianak2(self) :
        print("Fungsi pada anak kedua")

#Objek
Kids1 = Anak1()
Kids2 = Anak2()

Kids1.fungsiinduk()
Kids1.fungsianak1()

Kids2.fungsiinduk()
Kids2.fungsianak2()
