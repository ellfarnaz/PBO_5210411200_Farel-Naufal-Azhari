#5210411200
#Farel Naufal Azhari

# parent
class computerPart:
    def __init__(self,part,pabrikan, nama, harga):
        self.part = part
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

class processor(computerPart):
    def __init__(self,part,pabrikan,nama,harga,jumlahCore,speed):
        self.part = part
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.jumlahCore = jumlahCore
        self.speed = speed

    def detailProcessor(self):
        print('Detail Processor :')
        print(f'''   Pabrikan    : {self.pabrikan}
   Nama        : {self.nama}
   Jumlah Core : {self.jumlahCore}
   Speed       : {self.speed}
   Harga       : {self.harga}\n''')

class ram(computerPart):
    def __init__(self,part,pabrikan, nama, harga,speed):
        self.part = part
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.speed = speed

    def detailRam(self,kapasitas):
        print('Detail Ram :')
        print(f'''   Pabrikan    : {self.pabrikan}
   Nama        : {self.nama}
   Kapasitas   : {kapasitas}
   Harga       : {self.harga}\n''')


class hardDisk(computerPart):
    def __init__(self,part, pabrikan, nama, harga,rpm):
        self.part = part
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.rpm = rpm

    def detailHardisk(self,kapasitas):
        print('Detail Harddisk :')
        print(f'''   Pabrikan    : {self.pabrikan}
   Nama        : {self.nama}
   Kapasitas   : {kapasitas}
   Speed       : {self.rpm}
   Harga       : {self.harga}''')
        
print('\n------------------ Spesifikasi Laptop Asus K45VD ------------------\n')
pcsor = processor('Processor','Intel', 'Core i3 2370M', 2400000, 4, '2.4GHz')

ramm = ram('RAM','V-Gen', 'DDR4 SODimm 2400MHz', 360000,66)

hdd = hardDisk('HardDisk','Seagate', 'HDD 2.5 inch', 295000, 7200)

# Detail Computer
parts = [pcsor,ramm,hdd]
for part in parts:
    print(f'{part.part} {part.nama} Produksi {part.pabrikan}')

# Detail processor
print('')
pcsor.detailProcessor()
ramm.detailRam("6GB")
hdd.detailHardisk("1TB")
"\n"
