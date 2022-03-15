#5210411200
#Farel Naufal Azhari

#Multiple Inheritance
class Mahasiswa1() :
    def __init__(self, nama, nim ) :
        self.nama = nama
        self.nim = nim
    
class Mahasiswa2() :
    def __init__(self, alamat, jurusan) :
        self.alamat = alamat
        self.jurusan = jurusan
    
class Siswa(Mahasiswa1, Mahasiswa2) :
    def __init__(self, nama, nim, alamat, jurusan) :
        Mahasiswa1.__init__(self, nama, nim)
        Mahasiswa2.__init__(self, alamat, jurusan)

siswa = Siswa("Mikasa", 135105, "Wall Rose", "Informatika") 
print(f"Nim : {siswa.nim}, Nama : {siswa.nama} Alamat : {siswa.alamat} Jurusan : {siswa.jurusan}")
