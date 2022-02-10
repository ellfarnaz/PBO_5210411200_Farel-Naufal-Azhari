# Nana : Farel Naufal AZhari
# NPM  : 5210411200

print ("\n--- Program Menghitung Volume dan Luas Tabung ---\n")

tinggi=int(input("Masukan Tinggi : "))
jari=int(input("Masukan Jari-jari Lingkaran : "))

phi=22/7

luas=int(2*phi*jari*(tinggi+jari))
volume=int((phi*(jari*jari))*tinggi)

print ("\nLuas tabung   = ", luas)
print ("Volume tabung = ", volume)
