import os

akun = {
    "admin": "108",
    "guest": "801"
}

akun_tambahan = {}

paket_photobox = {
    "1": {"nama": "Paket Silver", "durasi": 30, "harga": 50000},
    "2": {"nama": "Paket Gold", "durasi": 60, "harga": 90000},
    "3": {"nama": "Paket Platinum", "durasi": 90, "harga": 130000},
    "4": {"nama": "Paket Diamond", "durasi": 120, "harga": 170000}
}


data_pelanggan = {}

while True:
    os.system('cls' )
    print("=== SISTEM MANAJEMEN PENYEWAAN PHOTOBOX ===")
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar")

    pilih_awal = input("Pilih menu: ")


    if pilih_awal == "2":
        os.system('cls' )
        print("=== REGISTER AKUN BARU ===")
        new_user = input("Masukkan username baru: ")
        new_pass = input("Masukkan password baru: ")

        if new_user in akun or new_user in akun_tambahan:
            print("Username sudah terdaftar! Silakan coba lagi.")
        else:
            akun_tambahan[new_user] = new_pass
            print("Akun berhasil dibuat! Silakan login menggunakan akun baru.")

        input("\nTekan Enter untuk kembali ke menu awal...")

   
    elif pilih_awal == "1":
        os.system('cls' )
        print("=== LOGIN SISTEM PHOTOBOX ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        login = False
        is_admin = False

        if username in akun and akun[username] == password:
            login = True
            if username == "admin":
                is_admin = True
        elif username in akun_tambahan and akun_tambahan[username] == password:
            login = True

        if not login:
            print("Login gagal! Username atau password salah.")
            input("\nTekan Enter untuk kembali...")
            continue

        print("Login berhasil!\n")

       
        while login:
            os.system('cls')
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
                os.system('cls')
                print("=== TAMBAH DATA PELANGGAN ===")
                id_p = input("Masukkan ID pelanggan: ")

                if id_p in data_pelanggan:
                    print("ID pelanggan sudah ada!")
                else:
                    nama = input("Masukkan nama pelanggan: ")
                    print("\nPilih paket yang diambil:")
                    for k, v in paket_photobox.items():
                        print(f"{k}. {v['nama']} - {v['durasi']} menit - Rp{v['harga']:,}")

                    pilih_paket = input("Masukkan nomor paket: ")
                    if pilih_paket in paket_photobox:
                        paket = paket_photobox[pilih_paket]['nama']
                    else:
                        paket = "Custom"

                    data_pelanggan[id_p] = {
                        "nama": nama,
                        "paket": paket,
                        "status": "Belum Bayar"
                    }
                    print("\nData pelanggan berhasil ditambahkan!")

                input("Tekan Enter untuk kembali...")

          
            elif menu == "2":
                os.system('cls' )
                print("=== DATA PELANGGAN ===")
                if not data_pelanggan:
                    print("Belum ada data pelanggan.")
                else:
                    for id_p, info in data_pelanggan.items():
                        print(f"ID: {id_p}")
                        print(f"Nama: {info['nama']}")
                        print(f"Paket: {info['paket']}")
                        print(f"Status Pembayaran: {info['status']}")
                        print("-" * 35)
                    print(f"Total pelanggan terdaftar: {len(data_pelanggan)}")
                input("\nTekan Enter untuk kembali...")

           
            elif menu == "3" and is_admin:
                os.system('cls')
                print("=== UBAH DATA PELANGGAN ===")
                id_cari = input("Masukkan ID pelanggan: ")

                if id_cari in data_pelanggan:
                    print("1. Ubah Nama")
                    print("2. Ubah Paket")
                    print("3. Ubah Status Pembayaran")
                    pilihan = input("Pilih data yang ingin diubah: ")

                    if pilihan == "1":
                        data_pelanggan[id_cari]['nama'] = input("Masukkan nama baru: ")
                    elif pilihan == "2":
                        for k, v in paket_photobox.items():
                            print(f"{k}. {v['nama']} - {v['durasi']} menit - Rp{v['harga']:,}")
                        pilih_paket = input("Masukkan nomor paket: ")
                        if pilih_paket in paket_photobox:
                            data_pelanggan[id_cari]['paket'] = paket_photobox[pilih_paket]['nama']
                    elif pilihan == "3":
                        data_pelanggan[id_cari]['status'] = input("Masukkan status baru (Belum Bayar/Lunas): ")
                    else:
                        print("Pilihan tidak valid.")
                    print("Data berhasil diubah!")
                else:
                    print("Data pelanggan tidak ditemukan.")

                input("\nTekan Enter untuk kembali...")

            
            elif menu == "4" and is_admin:
                os.system('cls' )
                print("=== HAPUS DATA PELANGGAN ===")
                id_hapus = input("Masukkan ID pelanggan: ")

                if id_hapus in data_pelanggan:
                    del data_pelanggan[id_hapus]
                    print("Data pelanggan berhasil dihapus!")
                else:
                    print("Data pelanggan tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")

           
            elif menu == "5":
                os.system('cls' )
                print("=== DAFTAR PAKET PHOTOBOX ===")
                for v in paket_photobox.values():
                    print(f"{v['nama']} | Durasi: {v['durasi']} menit | Harga: Rp{v['harga']:,}")
                input("\nTekan Enter untuk kembali...")

           
            elif menu == "6":
                print("Anda telah logout. Terima kasih!")
                login = False
                input("Tekan Enter untuk kembali ke menu awal...")
                break

            else:
                print("Menu tidak valid!")
                input("Tekan Enter untuk kembali...")

   
    elif pilih_awal == "3":
        print("\nTerima kasih telah menggunakan sistem penyewaan photobox!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")