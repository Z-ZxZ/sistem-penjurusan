karakter = input("Masukkan karakter : ")

if karakter.lower() in "aiueo" or karakter.upper() in "AIUEO":
    print("karakter", karakter, "adalah huruf hidup")
else:
    print("karakter", karakter, "bukan huruf hidup")