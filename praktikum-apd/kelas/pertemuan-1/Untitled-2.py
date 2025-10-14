nama = str(input("input nama kamu : "))
nim = int(input("input nim kamu : "))

ukt = 6000000

print("""opsi:
1. lunas
2. cicilan 2x
3. cicilan 4x
4. cicilan 6x""")

opsi= int(input("(1/2/3/4): "))

if opsi == 1:
    biaya_administrasi = 0.01
    total_bayar = ukt + (ukt * biaya_administrasi)
    print(f"total biaya ukt =Rp {total_bayar:,.0f}".replace (",","."))
elif opsi == 2:
    biaya_administrasi = 0.05
    cicilan = 2
    total_bayar = ukt + (ukt * biaya_administrasi)
    total_cicilan = total_bayar / cicilan
    print(f"total biaya ukt =Rp{total_bayar:,.0f}".replace (","))
    print(f"cicilan perpriode =Rp{cicilan:,.}")
elif opsi == 3:
    biaya_administrasi = 0.08
    cicilan = 4
    total_bayar = ukt + (ukt * biaya_administrasi)
    total_cicilan = total_bayar / cicilan
    
elif opsi == 4:
    biaya_administrasi = 0.12
    cicilan = 6
    total_bayar = ukt + (ukt * biaya_administrasi)
    total_cicilan = total_bayar / cicilan


