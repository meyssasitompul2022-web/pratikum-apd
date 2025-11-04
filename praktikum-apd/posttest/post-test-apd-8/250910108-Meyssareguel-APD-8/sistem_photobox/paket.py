# paket.py
import os
from prettytable import PrettyTable
from data import paket_photobox

def tampilkan_paket():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== DAFTAR PAKET PHOTOBOX ===\n")
    
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Paket", "Durasi (menit)", "Harga (Rp)"]
    
    for k, v in paket_photobox.items():
        tabel.add_row([k, v["nama"], v["durasi"], f"{v['harga']:,}"])
    
    print(tabel)
    input("\nTekan Enter untuk kembali...")
