username = "Meyssa"
password = "12345678"

attempt = 0
login_success = False

while attempt < 3:
    nama = input("Masukkan username: ")
    nim = input("Masukkan NIM: ")
    
    if nama == username and nim == password:
        print("Login berhasil Selamat datang di Toko Furnitur Infordeh.")
        login_success = True
        break
    else:
        attempt += 1
        print(f"Login gagal Percobaan ke-{attempt}/3.")

if not login_success:
    print("Anda gagal login 3 kali. Program berhenti.")
    exit()

harga_furnitur = {
    "1": {"nama": "Sofa", "harga": 500000},
    "2": {"nama": "Meja Belajar", "harga": 250000},
    "3": {"nama": "Rak Lemari", "harga": 150000}
}

total_bayar = 0
daftar_pembelian = []

while True:
    print("=== Menu Pembelian Furnitur ===")
    print("1. Sofa (Rp 500.000/unit)")
    print("2. Meja Belajar (Rp 250.000/unit)")
    print("3. Rak Lemari (Rp 150.000/unit)")
    print("4. Keluar")
    
    pilihan = input("Pilih opsi (1-4): ")
    
    if pilihan == "4":
        print("Terima kasih telah berbelanja!")
        break
    elif pilihan in ["1", "2", "3"]:
        try:
            jumlah = int(input(f"Masukkan jumlah {harga_furnitur[pilihan]['nama']}: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                continue
        except:
            print("Input tidak valid! Masukkan angka.")
            continue

        subtotal = 0
        for i in range(jumlah):
            subtotal += harga_furnitur[pilihan]["harga"]
        
        total_bayar += subtotal
        daftar_pembelian.append({"nama": harga_furnitur[pilihan]["nama"], "jumlah": jumlah, "subtotal": subtotal})
        print(f"{jumlah} {harga_furnitur[pilihan]['nama']} berhasil ditambahkan ke keranjang.")
    else:
        print("Opsi tidak valid! Silakan pilih 1-4.")

print("=== Rincian Pembelian ===")
for item in daftar_pembelian:
    print(f"{item['nama']} - Jumlah: {item['jumlah']} unit - Subtotal: Rp {item['subtotal']:}")

if total_bayar >= 700000:
    diskon = 0.20
    total_akhir = int(total_bayar * (1 - diskon))
    print(f"Total bayar: Rp {total_bayar:}")
    print(f"Diskon 20% diterapkan! Total akhir: Rp {total_akhir:}")
elif total_bayar >= 500000:
    diskon = 0.08
    total_akhir = int(total_bayar * (1 - diskon))
    print(f"Total bayar: Rp {total_bayar:}")
    print(f"Diskon 8% diterapkan! Total akhir: Rp {total_akhir:}")
elif total_bayar >= 150000:
    print(f"Total bayar: Rp {total_bayar:}")
    print("Selamat! Anda mendapat hadiah Kitchen Set!")

else:
    print(f"Total bayar: Rp {total_bayar:}")