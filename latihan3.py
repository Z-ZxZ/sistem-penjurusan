a=int(input("Bilangan Pertama : "))
b=int(input("Bilangan Kedua : "))
kode=int(input("Kode operasi (1=jumlah, 2=kali) : "))

if kode == 1:
    hasil = a + b
    print(f"Hasil Penjumlahan: {hasil}")
elif kode == 2:
    hasil = a * b
    print(f"Hasil Perkalian: {hasil}")
else:
    print("Kode operasi tidak valid")
