#5210411200
#Farel Naufal Azhari

#Multilevel Inheritance
class Mahasiswa() :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim

class Siswa1(Mahasiswa) :
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        
class Siswa2(Siswa1) :
    def __init__(self, nama, nim):
        super().__init__(nama, nim)

mhsw1 = Mahasiswa("Mikasa", 135105)
mhsw2 = Siswa1("Eren", 135501)
mhsw3 = Siswa2("Levi", 132100)

print(mhsw1.nama, mhsw1.nim)
print(mhsw2.nim)   
print(mhsw3.nama)
