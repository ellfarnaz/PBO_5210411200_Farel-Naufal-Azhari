class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit


buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'Hamka', 1938)
buku2 = Buku('The Memoirs of Sherlock Holmes', 'Arthur Conan Doyle', 1893)
buku3 = Buku('Laskar Pelangi', 'Andrea Hirata', 2005)


data_buku = [buku1, buku2, buku3]

print('\nDaftar Buku\n')
for i in data_buku:
    print(
        f'Buku {i.judul} Karangan {i.pengarang} Pertama Kali Diterbitkan Tahun {i.tahun_terbit}')