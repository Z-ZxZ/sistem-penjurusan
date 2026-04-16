harga = {
    "R": [2000, 4500, 6500],
    "C": [5000, 7000, 10000],
    "V": [7500, 10000, 15000]
}

kode = input("Masukkan kode barang (R/C/V): ").upper()
mb = int(input("Masukkan jumlah pemakaian (MB): "))

if mb <=50:
    idx = 0
elif mb <=80:
    idx = 1
else:
    idx = 2
    
harga_per_mb = harga[kode][idx]

total = harga_per_mb * mb

print("\n Rincian Pembayaran")
print(f"Kode pelanggan :", kode)
print(f"Jumlah Pemakaian: ", mb, "MB")
print(f"Harga per MB: ",harga_per_mb)
print(f"Total Pembayaran: ", total)