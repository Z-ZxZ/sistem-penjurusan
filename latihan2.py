import math

def hitung_segitiga_siku(a, b):
    c = math.hypot(a, b)       
    luas = (a * b) / 2
    keliling = a + b + c
    return luas, keliling

print("\n Hitung Segitiga Siku-siku ")
a = float(input("Masukkan panjang sisi a (alas): "))
b = float(input("Masukkan panjang sisi b (tinggi): "))

luas, keliling = hitung_segitiga_siku(a, b)
print(f"Luas segitiga = {luas:.2f}")
print(f"Keliling segitiga = {keliling:.2f}")
