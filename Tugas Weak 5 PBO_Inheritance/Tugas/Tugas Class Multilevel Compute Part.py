#5210411200
#Farel Naufal Azhari

#Multilevel Inheritance

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

class ram(processor):
    def __init__(self,part,pabrikan, nama, harga, kapasitas,speed):
        self.part = part
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas
        self.speed = speed

    def detailRam(self):
        print('Detail Ram :')
        print(f'''   Pabrikan    : {self.pabrikan}
   Nama        : {self.nama}
   Kapasitas   : {self.kapasitas}
   Harga       : {self.harga}\n''')


class hardDisk(ram):
    def __init__(self,part, pabrikan, nama, harga,  kapasitas, rpm):
        self.part = part
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas
        self.rpm = rpm

    def detailHardisk(self):
        print('Detail Harddisk :')
        print(f'''   Pabrikan    : {self.pabrikan}
   Nama        : {self.nama}
   Kapasitas   : {self.kapasitas}
   Speed       : {self.kapasitas} RPM
   Harga       : {self.harga}''')
        
print('\n------------------ Spesifikasi Laptop Asus K45VD ------------------\n')
pcsor = processor('Processor','Intel', 'Core i3 2370M', 2400000, 4, '2.4GHz')

ramm = ram('RAM','V-Gen', 'DDR4 SODimm 2400MHz', 360000, '6GB',66)

hdd = hardDisk('HardDisk','Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)

# Detail Computer
parts = [pcsor,ramm,hdd]
for part in parts:
    print(f'{part.part} {part.nama} Produksi {part.pabrikan}')

# Detail processor
print('')
pcsor.detailProcessor()
"\n"
# Detail Ram
ramm.detailRam()
# Detail Harddisk
hdd.detailHardisk()