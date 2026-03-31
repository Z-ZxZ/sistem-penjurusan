def input_nilai(mapel):
    while True:
        try:
            n = float(input("Nilai " + mapel + ": "))
            if 0 <= n <= 100:
                return n
            else:
                print("Nilai harus 0 sampai 100")
        except:
            print("Masukkan angka yang benar")


print("Sistem Penjurusan SMA")

print("\nSyarat Nilai Jurusan")
print("Jurusan   Mata Pelajaran     Minimum")

print("\nIPA       Matematika         80")
print("          Biologi            78")
print("          Fisika             78")
print("          Kimia              78")

print("\nIPS       Matematika         80")
print("          Geografi           78")
print("          Ekonomi            80")
print("          Sosiologi          78")

print("\nBAHASA    Matematika         75")
print("          B. Indonesia       80")
print("          B. Inggris         78")
print("          B. Lain            75")


nama = input("\nNama siswa: ")

print("\nPilih minat jurusan")
print("1. IPA")
print("2. IPS")
print("3. BAHASA")

pilihan = input("Masukkan pilihan: ")

if pilihan == "1":
    minat = "IPA"
elif pilihan == "2":
    minat = "IPS"
else:
    minat = "BAHASA"


print("\nMasukkan nilai mata pelajaran")

nilai = {}
nilai["mtk"] = input_nilai("Matematika")
nilai["bio"] = input_nilai("Biologi")
nilai["fis"] = input_nilai("Fisika")
nilai["kim"] = input_nilai("Kimia")

nilai["geo"] = input_nilai("Geografi")
nilai["eko"] = input_nilai("Ekonomi")
nilai["sos"] = input_nilai("Sosiologi")

nilai["indo"] = input_nilai("B. Indonesia")
nilai["ing"] = input_nilai("B. Inggris")
nilai["lain"] = input_nilai("B. Lain")


ipa = False
ips = False
bahasa = False


if nilai["mtk"] >= 80 and nilai["bio"] >= 78 and nilai["fis"] >= 78 and nilai["kim"] >= 78:
    ipa = True

if nilai["mtk"] >= 80 and nilai["geo"] >= 78 and nilai["eko"] >= 80 and nilai["sos"] >= 78:
    ips = True

if nilai["mtk"] >= 75 and nilai["indo"] >= 80 and nilai["ing"] >= 78 and nilai["lain"] >= 75:
    bahasa = True


print("\nHasil Penjurusan")
print("Nama :", nama)
print("Minat:", minat)


if minat == "IPA":
    if ipa:
        print("Diterima di jurusan IPA")
    elif ips:
        print("Disarankan ke jurusan IPS")
    elif bahasa:
        print("Disarankan ke jurusan BAHASA")
    else:
        print("Tidak memenuhi syarat jurusan")

elif minat == "IPS":
    if ips:
        print("Diterima di jurusan IPS")
    elif ipa:
        print("Disarankan ke jurusan IPA")
    elif bahasa:
        print("Disarankan ke jurusan BAHASA")
    else:
        print("Tidak memenuhi syarat jurusan")

else:
    if bahasa:
        print("Diterima di jurusan BAHASA")
    elif ipa:
        print("Disarankan ke jurusan IPA")
    elif ips:
        print("Disarankan ke jurusan IPS")
    else:
        print("Tidak memenuhi syarat jurusan")
