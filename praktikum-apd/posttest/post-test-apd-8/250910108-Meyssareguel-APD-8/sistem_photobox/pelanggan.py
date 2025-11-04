import os
from prettytable import PrettyTable
from data import data_pelanggan, paket_photobox

def tampilkan_pelanggan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== DATA PELANGGAN ===\n")

    if not data_pelanggan:
        print("Belum ada data pelanggan.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama", "Paket", "Status Pembayaran"]

        for id_p, info in data_pelanggan.items():
            tabel.add_row([id_p, info["nama"], info["paket"], info["status"]])

        print(tabel)
        print(f"\nTotal pelanggan terdaftar: {len(data_pelanggan)}")
    input("\nTekan Enter untuk kembali...")


def tambah_pelanggan(id_pelanggan, nama_pelanggan):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TAMBAH DATA PELANGGAN ===\n")

    if id_pelanggan in data_pelanggan:
        print("ID pelanggan sudah ada!")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Paket", "Durasi (menit)", "Harga (Rp)"]
        for k, v in paket_photobox.items():
            tabel.add_row([k, v["nama"], v["durasi"], f"{v['harga']:,}"])
        print(tabel)

        pilih_paket = input("Masukkan nomor paket: ")
        if pilih_paket in paket_photobox:
            paket = paket_photobox[pilih_paket]["nama"]
        else:
            paket = "Custom"

        data_pelanggan[id_pelanggan] = {
            "nama": nama_pelanggan,
            "paket": paket,
            "status": "Belum Bayar"
        }
        print("\nData pelanggan berhasil ditambahkan!")
    input("\nTekan Enter untuk kembali...")


def ubah_data(id_pelanggan):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== UBAH DATA PELANGGAN ===\n")

    if id_pelanggan in data_pelanggan:
        print("1. Ubah Nama")
        print("2. Ubah Paket")
        print("3. Ubah Status Pembayaran")
        pilihan = input("Pilih data yang ingin diubah: ")

        if pilihan == "1":
            data_pelanggan[id_pelanggan]['nama'] = input("Masukkan nama baru: ")
        elif pilihan == "2":
            tabel = PrettyTable()
            tabel.field_names = ["No", "Nama Paket", "Durasi (menit)", "Harga (Rp)"]
            for k, v in paket_photobox.items():
                tabel.add_row([k, v["nama"], v["durasi"], f"{v['harga']:,}"])
            print(tabel)
            pilih_paket = input("Masukkan nomor paket: ")
            if pilih_paket in paket_photobox:
                data_pelanggan[id_pelanggan]['paket'] = paket_photobox[pilih_paket]['nama']
        elif pilihan == "3":
            data_pelanggan[id_pelanggan]['status'] = input("Masukkan status baru (Belum Bayar/Lunas): ")
        else:
            print("Pilihan tidak valid.")
        print("\nData berhasil diubah!")
    else:
        print("Data pelanggan tidak ditemukan.")
    input("\nTekan Enter untuk kembali...")
