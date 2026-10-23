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
    skor = 100
else:
    print("Belum tepat. Jawabannya adalah Python.")
    skor = 0
print("Skor kamu:", skor)

if skor == 100:
    print("Kerja bagus, Kafka!")
else:
    print("Semangat belajar lagi, Kafka!")
print("Terima kasih sudah mengikuti kuis!")