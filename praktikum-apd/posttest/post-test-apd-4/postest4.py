Nama = "Meyssa"
Nim = "12345678"

login = 0
login_success = False

while login < 3:
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    if nama == Nama and nim == Nim:
        print("\nLogin berhasil! Selamat datang di toko sofa")
        login_success = True
        break
    else:
        login += 1
        print(f"Login gagal! Percobaan ke-{login}/3.\n")

if not login_success:
    print("Anda gagal login sebanyak 3 kali. maka sistemnya berhenti")
    exit()

furniturpertama = "Sofa"
harga1 = 500000

furniturkedua = "Meja Belajar"
harga2 = 250000

furniturketiga = "Rak Lemari"
harga3 = 150000

total_bayar = 0

while True:
    print("\n=== MENU FURNITUR INFORDEH ===")
    print("1.", furniturpertama, "- Rp", harga1)
    print("2.", furniturkedua, "- Rp", harga2)
    print("3.", furniturketiga, "- Rp", harga3)
    print("4. Keluar")

    pilihan = input("Pilih menu (1 sampai 4): ")

    if pilihan == "4":
        print("\nTerima kasih telah belanja di Toko Furnitur Infordeh!")
        break

    elif pilihan == "1" or pilihan == "2" or pilihan == "3":
        jumlah_input = input("Masukkan jumlah furnitur: ")

        if jumlah_input.isdigit():
            jumlah = int(jumlah_input)
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                continue
        else:
            print("Input tidak valid! Masukkan angka positif.")
            continue

        if pilihan == "1":
            nama_barang = furniturpertama
            harga = harga1
        elif pilihan == "2":
            nama_barang = furniturkedua
            harga = harga2
        else:
            nama_barang = furniturketiga
            harga = harga3

        subtotal = 0
        for i in range(jumlah):
            subtotal += harga

        total_bayar += subtotal
        print(f"{jumlah} {nama_barang} berhasil ditambahkan ke keranjang. Subtotal: Rp{subtotal}")

    else:
        print("Opsi tidak valid! Silakan pilih 1 sampai 4.")

print("\n=== RINCIAN PEMBAYARAN ===")
print(f"Total Pembelian: Rp{total_bayar}")

if total_bayar >= 700000:
    potongan = 0.20
    total_akhir = int(total_bayar * (1 - potongan))
    print("kamu dapat diskon 20%!")
    print(f"Total akhir setelah diskon: Rp{total_akhir}")

elif total_bayar >= 500000 and total_bayar < 700000:
    potongan = 0.08
    total_akhir = int(total_bayar * (1 - potongan))
    print("kamu dapat diskon 8%!")
    print(f"Total akhir setelah diskon: Rp{total_akhir}")

elif total_bayar >= 150000 and total_bayar < 500000:
    print(f"Total bayar: Rp{total_bayar}")
    print("Selamat! Anda dapat hadiah ayam")

else:
    print(f"Total bayar: Rp{total_bayar}")
