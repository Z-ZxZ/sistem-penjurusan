x=int(input("Uang Dari Ayah : "))
k=int(input("Jumlah Aanak : "))

sekolah=0.3*x
saku=k*200000

sisa1=x-sekolah-saku
dapur=0.3*sisa1

sisa2=sisa1-dapur
listrik=300000
sisa3=sisa2-listrik

tabungan=0.2*sisa3
sisa_akhir=sisa3-tabungan

print("Biaya Sekolah", sekolah)
print("Uang Saku Anak", saku)
print("Biaya Listrik", listrik)
print("BIaya Dapur", dapur)
print("Tabungan", tabungan)
print("Sisa Uang Ibu", sisa_akhir)
