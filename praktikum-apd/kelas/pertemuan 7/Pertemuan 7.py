def perkenalan():
    print("Halo, aku Nabil")
def salam():
     print("Halo, Ridho")
def kali():
    X = 5*5
    print(X)

salam()
salam()
salam()
kali()
kali()
kali()

def luas_persegi_panjang(panjang, lebar):
  luas = panjang * lebar
print ("luas persegi panjang adalah ", luas)

#Pemanggilan Fungsi luas_persegi_panjang
luas_persegi_panjang(4, 5)

def faktorial(n):
# Basis (Base Case): Kondisi berhenti
   if n == 1 or n == 0:
    return 1
# Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
   else:
    return n * faktorial(n - 1)
# Memanggil fungsi
hasil = faktorial(5)
print(f"Hasil dari 5! adalah: {hasil}")

def show_data():
  if len(film) <= 0:
   print("Belum Ada data")
  else:
    print("ID | Judul Film")
for indeks in range(len(film)):
    print(indeks, "|", film[indeks])

    def show_menu():
     print ("\n")
print ("----------- MENU---------- ")
print ("[1] Show Data")
print ("[2] Insert Data")
print ("[3] Edit Data")
print ("[4] Delete Data")
print ("[5] Exit")
menu = input("PILIH MENU> ")
print ("\n")
if menu == "1":
show_data()elif menu == "2":
insert_data()
elif menu == "3":
edit_data()
elif menu == "4":
delete_data()
elif menu == "5":
exit()
else:
print ("Salah pilih!")