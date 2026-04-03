nuts = int(input("Nilai UTS: "))
nuas = int(input("Nilai UAS: "))
ntgs = int(input("Nilai Tugas: "))
nsiswa = input("Nama siswa: ")

na = (nuts + nuas + ntgs) / 3

print("Nama:", nsiswa)
print("Nilai akhir:", na)

if na >= 60:
    print("Status: Lulus")
else:
    print("Status: Tidak Lulus")

if na < 45:
    grade = "E"
elif na < 60:
    grade = "D"
elif na < 70:
    grade = "C"
elif na < 85:
    grade = "B"
else:
    grade = "A"

print("Grade:", grade)