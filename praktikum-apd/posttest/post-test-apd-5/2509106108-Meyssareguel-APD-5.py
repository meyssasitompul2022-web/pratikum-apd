import os


admin_user = "admin"
admin_pass = "108"
guest_user = "guest"
guest_pass = "801"


akun_tambahan = []  

paket_photobox = [
    ["Paket Silver", 30, 50000],
    ["Paket Gold", 60, 90000],
    ["Paket Platinum", 90, 130000],
    ["Paket Diamond", 120, 170000]
]


data_pelanggan = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM MANAJEMEN PENYEWAAN PHOTOBOX ===")
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar")

    pilih_awal = input("Pilih menu: ")

    
    if pilih_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        new_user = input("Masukkan username baru: ")
        new_pass = input("Masukkan password baru: ")

       
        duplikat = False
        if new_user == admin_user or new_user == guest_user:
            duplikat = True
        for a in akun_tambahan:
            if a[0] == new_user:
                duplikat = True

        if duplikat:
            print("Username sudah terdaftar! Silakan coba lagi.")
        else:
            akun_tambahan.append([new_user, new_pass])
            print("Akun berhasil dibuat! Silakan login menggunakan akun baru.")

        input("\nTekan Enter untuk kembali ke menu awal...")

    
    elif pilih_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN SISTEM PHOTOBOX ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        login = False
        is_admin = False

        
        if username == admin_user and password == admin_pass:
            login = True
            is_admin = True
        elif username == guest_user and password == guest_pass:
            login = True
        else:
            for a in akun_tambahan:
                if username == a[0] and password == a[1]:
                    login = True
                    break

        if not login:
            print("Login gagal! Username atau password salah.")
            input("\nTekan Enter untuk kembali...")
            continue

        print("Login berhasil!\n")

        
        while login:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== MENU UTAMA ===")
            print("1. Tambah Data Pelanggan (Create)")
            print("2. Lihat Data Pelanggan (Read)")
            if is_admin:
                print("3. Ubah Data Pelanggan (Update)")
                print("4. Hapus Data Pelanggan (Delete)")
            print("5. Lihat Daftar Paket Photobox")
            print("6. Logout")

            menu = input("Pilih menu: ")

           
            if menu == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== TAMBAH DATA PELANGGAN ===")
                id_p = input("Masukkan ID pelanggan: ")
                nama = input("Masukkan nama pelanggan: ")

                print("\nPilih paket yang diambil:")
                for i, p in enumerate(paket_photobox):
                    print(f"{i+1}. {p[0]} - {p[1]} menit - Rp{p[2]:,}")

                pilih_paket = input("Masukkan nomor paket: ")
                if pilih_paket.isdigit() and 1 <= int(pilih_paket) <= len(paket_photobox):
                    paket = paket_photobox[int(pilih_paket)-1][0]
                else:
                    print("Pilihan tidak valid, paket diatur ke 'Custom'")
                    paket = "Custom"

                status = "Belum Bayar"
                data_pelanggan.append([id_p, nama, paket, status])
                print("\nData pelanggan berhasil ditambahkan!")
                input("Tekan Enter untuk kembali...")

            
            elif menu == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== DATA PELANGGAN ===")
                if len(data_pelanggan) == 0:
                    print("Belum ada data pelanggan.")
                else:
                    for p in data_pelanggan:
                        print(f"ID: {p[0]}")
                        print(f"Nama: {p[1]}")
                        print(f"Paket: {p[2]}")
                        print(f"Status Pembayaran: {p[3]}")
                        print("-" * 35)
                    print(f"Total pelanggan terdaftar: {len(data_pelanggan)}")
                input("\nTekan Enter untuk kembali...")

            
            elif menu == "3" and is_admin:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== UBAH DATA PELANGGAN ===")
                id_cari = input("Masukkan ID pelanggan yang ingin diubah: ")
                ketemu = False
                for p in data_pelanggan:
                    if p[0] == id_cari:
                        ketemu = True
                        print("\nData ditemukan!")
                        print("1. Ubah nama")
                        print("2. Ubah paket")
                        print("3. Ubah status pembayaran")
                        pilihan = input("Pilih data yang ingin diubah: ")

                        if pilihan == "1":
                            p[1] = input("Masukkan nama baru: ")
                        elif pilihan == "2":
                            print("\nPilih paket baru:")
                            for i, x in enumerate(paket_photobox):
                                print(f"{i+1}. {x[0]} - {x[1]} menit - Rp{x[2]:,}")
                            pilih_paket = input("Masukkan nomor paket: ")
                            if pilih_paket.isdigit() and 1 <= int(pilih_paket) <= len(paket_photobox):
                                p[2] = paket_photobox[int(pilih_paket)-1][0]
                            else:
                                print("Pilihan tidak valid, tidak ada perubahan paket.")
                        elif pilihan == "3":
                            p[3] = input("Masukkan status baru (Belum Bayar / Lunas): ")
                        else:
                            print("Pilihan tidak valid.")

                        print("\nData berhasil diubah!")
                        break

                if not ketemu:
                    print("Data dengan ID tersebut tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")

            
            elif menu == "4" and is_admin:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== HAPUS DATA PELANGGAN ===")
                id_hapus = input("Masukkan ID pelanggan yang ingin dihapus: ")
                ketemu = False
                for p in data_pelanggan:
                    if p[0] == id_hapus:
                        ketemu = True
                        data_pelanggan.remove(p)
                        print("Data pelanggan berhasil dihapus!")
                        break
                if not ketemu:
                    print("Data dengan ID tersebut tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")

            
            elif menu == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== DAFTAR PAKET PHOTOBOX ===")
                for p in paket_photobox:
                    print(f"{p[0]} | Durasi: {p[1]} menit | Harga: Rp{p[2]:,}")
                input("\nTekan Enter untuk kembali...")

            
            elif menu == "6":
                print("\nAnda telah logout. Terima kasih!")
                login = False
                input("Tekan Enter untuk kembali ke menu awal...")
                break

            else:
                print("Menu tidak valid!")
                input("Tekan Enter untuk kembali...")

    elif pilih_awal == "3":
        print("\nTerima kasih telah menggunakan sistem penyewaan photobox!")
        print("Sampai jumpa ")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        