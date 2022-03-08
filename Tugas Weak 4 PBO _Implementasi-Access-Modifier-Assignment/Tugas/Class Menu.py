class menuMinuman:
    def __init__(self, nama, deskripsi, harga,toping):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__toping = toping


mnm1 = menuMinuman('Jus Jambu', 'Jus jambu merah tanpa gula', 8500, 'Keju')
mnm2 = menuMinuman('Jus Alpukat Ori','Jus alpukat dengan tambahan air gula merah', 15000, 'Oreo')
mnm3 = menuMinuman('Jus Alpukat Xtra Milk','Jus alpukat dengan campuran susu coklat dan tamburan kepingan choco', 15000, 'Es krim')
mnm4 = menuMinuman('Red & Smoothie', 'Smoothie pisang susu dan strawberry', 17500, 'Wafer')
mnm5 = menuMinuman('Ice Matcha', 'Ice Matcha dengan mactha asli Jepang', 20000, 'Cake Matcha')
mnm6 = menuMinuman('Black Tea', 'Teh Hitam dengan rasa yang menarik', 15000, 'Jely')


pilihanMenu = [mnm1, mnm2, mnm3, mnm4, mnm5, mnm6]
print('\nDaftar Menu Healthy Fruits\n')

for i in pilihanMenu:
    print('{} harga Rp. {}, {} dengan toping {}'.format(i.nama, i.harga, i.deskripsi,i._menuMinuman__toping))