nama = input("kafka lazuardi : ")

print("\n=== KUIS INTERAKTIF ===")
print("Halo,", nama)
print("1. Bahasa pemrograman yang sedang kita gunakan?")
print("a. Python")
print("b. HTML")
print("c. CSS")

jawaban = input("Jawaban kamu (a/b/c): ").lower()

if jawaban == "a":
    print("Benar! ")
else:
    print("Belum tepat. Jawabannya adalah Python.")