from time import sleep
from os import system

while True:
    system("cls")
    print("╔═════════════════════╗")
    print("║    Hesap Makinesi   ║")
    print("║═════════════════════║")
    print("║                     ║")
    print("║  1-Toplama          ║")
    print("║  2-Çıkarma          ║")
    print("║  3-çarpma           ║")
    print("║  4-Bölme            ║")
    print("║  5-Çıkış            ║")
    print("║                     ║")
    print("╚═════════════════════╝")
    op = input("Seçimiz nedir?: ")
    if op == "1":
        a = int(input("1. Sayıyı Giriniz: "))
        b = int(input("2. Sayıyı Giriniz: "))
        print(f"{a} + {b} = {a + b}")
        sleep(10)
        continue
    elif op == "2":
        a = int(input("1. Sayıyı Giriniz: "))
        b = int(input("2. Sayıyı Giriniz: "))
        print(f"{a} - {b} = {a - b}")
        sleep(10)
        continue
    elif op == "3":
        a = int(input("1. Sayıyı Giriniz: "))
        b = int(input("2. Sayıyı Giriniz: "))
        print(f"{a} x {b} = {a * b}")
        sleep(10)
        continue
    elif op == "4":
        a = int(input("1. Sayıyı Giriniz: "))
        b = int(input("2. Sayıyı Giriniz: "))
        if b == 0:
            print("Bir sayı 0'a bölünemez!")
            sleep(10)
            continue
        print(f"{a} / {b} = {a / b}")
        sleep(10)
        continue
    elif op == "5":
        print("Çıkılıyor...")
        sleep(2)
        break
    else:
        print("Geçersiz Giriş!")
        sleep(10)
        continue

