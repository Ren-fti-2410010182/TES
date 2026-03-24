# Program Python untuk mengecek apakah tiga bilangan dapat membentuk segitiga
# Menggunakan percabangan if-else

# Input tiga bilangan
a = float(input("Masukkan panjang sisi pertama: "))
b = float(input("Masukkan panjang sisi kedua: "))
c = float(input("Masukkan panjang sisi ketiga: "))

# Cek kondisi segitiga
if a + b > c and a + c > b and b + c > a:
    print("Tiga bilangan ini dapat membentuk segitiga.")
else:
    print("Tiga bilangan ini tidak dapat membentuk segitiga.")
