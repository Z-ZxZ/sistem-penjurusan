harga_barang = {
    "indomie": 3500,
    "susu": 8000,
    "roti": 12000,
    "kopi": 5000
}

nama_pembeli = input("Masukkan nama pembeli: ")

total_harga = 0

while True:
    barang = input("Masukkan nama barang: ").lower()
    
    if barang not in harga_barang:
        print("Barang tidak tersedia.")
        continue
    
    jumlah = int(input("Masukkan jumlah barang: "))
    
    while jumlah <= 0:
        print("Jumlah harus lebih dari 0")
        jumlah = int(input("Masukkan jumlah barang: "))
    
    subtotal = harga_barang[barang] * jumlah
    total_harga += subtotal
    
    print(f"Subtotal: {subtotal}")
    
    lagi = input("Tambah barang lagi? (y/n): ").lower()
    
    if lagi == "n":
        break

# hitung diskon
if total_harga >= 50000:
    diskon = total_harga * 0.10
elif total_harga >= 30000:
    diskon = total_harga * 0.05
else:
    diskon = 0

total_bayar = total_harga - diskon

print("\n===== STRUK =====")
print("\nNama Pembeli:", nama_pembeli)
print("\nTotal Belanja:", total_harga)
print("\nDiskon:", diskon)
print("\nTotal Bayar:", total_bayar)
print("\nTerima kasih telah berbelanja di toko kami!")