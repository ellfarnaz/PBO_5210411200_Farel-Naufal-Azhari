#5210411200
#Farel Naufal Azhari

#Single Inheritance
class Mahasiswa :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
        
    def detailMhs(self) :
        return self.nim, self.nama

    def cekMhs(self) :  
        if self.nim < 150000 :
            return "Mahasiswa Aktif"
        else :
            return "Mahasiswa Tidak Terdaftar"

class Siswa(Mahasiswa) :
    def End(self) : 
        print("Mahasiswa belum melakukan daftar ulang")

mhsw1 = Mahasiswa("Farel", 135103)
print(mhsw1.detailMhs(), mhsw1.cekMhs())

mhsw2 = Siswa("Mantan", 150503)
print(mhsw2.detailMhs(), mhsw2.cekMhs())
mhsw2.End()

