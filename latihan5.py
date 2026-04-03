x = int(input("Masukkan nilai X: "))
y = int(input("Masukkan nilai Y: "))

p = x + y

if p % 2 == 0:
    q = x * y
else:
    q = x - y

print("Nilai P =", p)
print("Nilai Q =", q)