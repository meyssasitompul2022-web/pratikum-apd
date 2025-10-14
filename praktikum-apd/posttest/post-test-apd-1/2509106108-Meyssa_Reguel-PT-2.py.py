nama_lengkap = input("Masukan Nama Lengkap:")
nim  = input("Masukan Nim:")

# Data harga dan diskon tiap merek
harga = 12000000
diskon = {
    "Acer":0.05,
    "Asus":0.07,
    "Lenovo":0.10
}
#input pilih merek laptop
merek = input("Pilih merek laptop (Acer/Asus/Lenovo):")
# Hitung harga akhir
harga_akhir= harga - (harga*diskon.get(merek,0))
print(f"Harga{merek}setelah diskon:Rp{harga_akhir:,.0f}")

# --- output ringkasan pesanan ---
print("=" * 40)
print("         PEMBELIAN LEPTOP")
print("=" * 40)
print(f"NAMA{'':<25}: {nama_lengkap}")
print(f"NIM{'':<26}: {nim}")
print(f"MEREK{'':<24}: {merek}")
print("-" * 40)
print(f"TOTAL KESELURUHAN{'':<11}: {harga_akhir}")
print("=" * 40)