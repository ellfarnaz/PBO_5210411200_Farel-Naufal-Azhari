class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, halaman):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__halaman = halaman


buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'Hamka', 1938, 224)
buku2 = Buku('The Memoirs of Sherlock Holmes', 'Arthur Conan Doyle', 1893, 410)
buku3 = Buku('Laskar Pelangi', 'Andrea Hirata', 2005, 529)


buku = [buku1, buku2, buku3]

print('\nDaftar Buku\n')
for i in buku:
    print(
        f'Buku {i.judul} Karangan {i.pengarang} Pertama Kali Diterbitkan Tahun {i.tahun_terbit} Dengan Jumlah {i._Buku__halaman} Halaman.')