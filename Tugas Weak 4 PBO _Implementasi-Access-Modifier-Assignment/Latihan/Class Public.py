class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi


segitiga_besar = segitiga(100, 80)

print('alas segitita = ', segitiga_besar.alas)
print('tinggi segitiga = ', segitiga_besar.tinggi)
print('luas segitiga = ', segitiga_besar.luas)
