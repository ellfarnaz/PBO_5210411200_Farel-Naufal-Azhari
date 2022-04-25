from ast import Break
import csv 
import os
import sys


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali...")
    clear_screen()

def main_menu():
    while(True):
        print("\n            Selamat Datang di Perpustakaan            ")
        print("------------------------------------------------------")
        print("1. Mencari Buku")
        print("2. Mencari Majalah")
        print("3. Mencari DVD")
        print("4. Mencari Manga")
        print("5. List Buku")
        print("6. Keluar Aplikasi")
        try:
            menu = int(input("Input pilihan menu sesuai yang anda inginkan >>> "))
            print()
            if(menu == 1):
                Data_Buku()
                kembali()
            
            elif(menu == 2):
                Data_Majalah()
                kembali()
                
            elif(menu == 3):
                Data_DVD()
                kembali()      

            elif(menu == 4):
                s_manga()
                kembali()

            elif(menu == 5):
                List_Buku()
                kembali()

            elif(menu == 6):
                Keluar()
                break
            
            else:
                print("Masukan pilihan menu yang anda inginkan")
                continue

        except ValueError:
            print("masukkan sesuai petunjuk !")
            # kembali()
            continue

def Data_Buku():
    with open('Buku.txt') as temp_f:
        data_b = temp_f.readlines()
        search = str(input("Masukkan judul buku yang anda ingin cari >>> "))
    for b in data_b:
        if search in b:
            return True, print(b,"---------- Buku yang anda cari tersedia ----------")
    return False, print("Maaf buku yang anda cari tidak tersedia")

def Data_Majalah():
    with open('stock.txt') as temp_f:
        data_m = temp_f.readlines()
        search = str(input("Masukkan judul buku yang anda ingin cari >>> "))
    for m in data_m:
        if search in m:
            return True, print(m,"---------- Buku yang anda cari tersedia ----------")
    return False, print("Maaf buku yang anda cari tidak tersedia")

def Data_DVD():
    with open('stock.txt') as temp_f:
        data_D = temp_f.readlines()
        search = str(input("Masukkan judul buku yang anda ingin cari >>> "))
    for D in data_D:
        if search in D:
            return True, print(D,"---------- Buku yang anda cari tersedia ----------")
    return False, print("Maaf buku yang anda cari tidak tersedia")

def s_manga():
    with open('stock.txt') as temp_f:
        data_mn = temp_f.readlines()
        search = str(input("Masukkan judul buku yang anda ingin cari >>> "))
    for mn in data_mn:
        if search in mn:
            return True, print(mn,"---------- Buku yang anda cari tersedia ----------")
    return False, print("Maaf buku yang anda cari tidak tersedia")

def List_Buku():
    with open('stock.txt', 'r+') as f:
        list = f.read()
        print(list)
        print()

def Keluar():
    print("----- Terimakasih Telah menggunakan sistem kami :) -----")


main_menu()