#5210411200
#Farel Naufal Azhari

class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.jenis = jenis
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed) :
        super().__init__(pabrikan, nama, 'Processor', harga)
        self.jumlah_core = jumlah_core
        self.speed = speed

class Ram(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas) :
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas = kapasitas 
    
class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
        super().__init__(pabrikan, nama, 'Sata', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm  

p = Processor('Intel', 'Core i3 2370M', 2400000, 4, '2.4GHz')
m = Ram('V-Gen', 'DDR4 SODimm 2400MHz', 360000, '6GB')
h = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)

parts = [p, m, h]
for part in parts :
    print('{} {} Produksi {}'.format(part.jenis, part.nama, part.pabrikan))
