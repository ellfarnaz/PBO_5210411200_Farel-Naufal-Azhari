#5210411200
#Farel Naufal Azhari

#Hierarchial Inheritance
class Mahasiswa() :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim

class Siswa1(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
      
    def detSiswa1(self) :
        print(self.nama, "Alamat : Wall Rose")

class Siswa2(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim  

    def detSiswa2(self) :
        print(self.nama, "Jurusan : Informatika")

mhsw1 = Siswa1("Mikasa", 135105)
mhsw2 = Siswa2("Eren", 135501)

print(mhsw1.nim)   
mhsw1.detSiswa1()
print(mhsw2.nim)
mhsw2.detSiswa2()


