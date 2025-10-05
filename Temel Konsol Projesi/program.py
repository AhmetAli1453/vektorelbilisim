from time import sleep
from os import system
from datetime import datetime
def sil():
    system("cls")

def sure():
    print("5 saniye bekleniyor...")
    sleep(1)
    print("4 saniye bekleniyor...")
    sleep(1)
    print("3 saniye bekleniyor...")
    sleep(1)
    print("2 saniye bekleniyor...")
    sleep(1)
    print("1 saniye bekleniyor...")
    sleep(1)
    print("Süre Bitti :)")


def animasyon(hiz=0.5, dongu_sayisi=5):
    for _ in range(dongu_sayisi):
        for i in range(4):
            system("cls")  # Windows için ekranı temizle
            print("╔═════════════════════╗")
            # Noktaları sola yaslayacak şekilde kutu satırını yaz
            print(f"║ Yükleniyor{'.'*i:<8}  ║")
            print("╚═════════════════════╝")
            sleep(hiz)
    # Döngü bittiğinde ekranı temizle ve kutuyu sabit göster
    system("cls")
    print("╔═════════════════════╗")
    print("║ Yükleniyor...       ║")
    print("╚═════════════════════╝")

while True:
    system("cls")
    print("╔═════════════════════╗")
    print("║Vektörel Bilişim Ödev║")
    print("║═════════════════════║")
    print("║1-Mrhb Diyen Uyg.    ║")
    print("║2-Ad Soyad snf - no  ║")
    print("║3-istiklal marşı uyg.║")
    print("║4-ekran yazdırma     ║")
    print("║5-ekrana ad yazdırma ║")
    print("║6-döviz uyg.         ║")
    print("║7-Hesap Makinesi     ║")
    print("║8-Yaş Hesaplama      ║")
    print("║9-Not Hesaplama      ║")
    print("║10.Kilo Ölçer - test ║")
    print("║11.Çıkış             ║")
    print("╚═════════════════════╝")
    op = input("Seçimiz nedir?: ")
    
    if op == "1":
        system("cls")
        a = input("Sizinle Tanışmak İstiyorum. Lütfen İsminizin Tamamını Giriniz:  ").split()
        ad = " ".join(a[:-1]) if len(a) > 1 else a[0]
        soyad = a[-1] if len(a) > 1 else ""
        system("cls")
        # 3 karakter veya daha fazlası için animasyonu çalıştır
        if len(a) >= 3:
            animasyon(hiz=0.3, dongu_sayisi=3)
            print("╔═══════════════════════╗")
            print("║   Sohbet Balonu :)    ║")
            print("║═══════════════════════║")
            print("║       Merhaba         ║")
            print(f"║       {ad}           ║")
            print("║     Soyadın İse :>    ║")
            print(f"║      {soyad}            ║")
            print("║      Olmalı :)        ║")
            print("║    Benim adım AAB     ║")
            print("║Tanıştığıma Memnn Oldum║")
            print("╚═══════════════════════╝")
            sleep(5)
        else:
            print("Merhaba, isminiz çok kısa görünüyor. Lütfen daha uzun bir isim girin: ")
        sure()
        continue
    elif op == "2":
        system("cls")
        # İsim ve numara al
        a = input("Lütfen İsminizin Tamamını Giriniz: ").split()
        numara = input("Lütfen Numaranızı(no) Giriniz: ")
        ad = " ".join(a[:-1]) if len(a) > 1 else a[0]
        soyad = a[-1] if len(a) > 1 else ""
        # Sınıf bilgisini al ve doğrula
        s = input("Sınıfınızı giriniz (9/a - 12/a): ").split("/")[0]
        try:
            g = int(s)
        except ValueError:
            print("Hatalı Sınıf Girdiniz!")
            sure()
            continue

        if 1 <= g <= 12:
            yas = g + 5.5
            system("cls")
            sinif = f"{g}. Sınıf"

            # Kutunun genişliğini dinamik tutmak için en uzun satırı ölçüyoruz
            satirlar = [
                f" Adınız: {ad}",
                f" Soyadınız: {soyad}",
                f" Sınıfınız: {sinif}",
                f" Numaranız: {numara}",
                f" Ortalama Yaşınız: {yas}"
            ]
            max_len = max(len(x) for x in satirlar) + 2  # yan boşluklar için +2

            print("╔" + "═" * max_len + "╗")
            for satir in satirlar:
                print("║" + satir.ljust(max_len) + "║")
            print("╚" + "═" * max_len + "╝")

            sleep(10)
            continue
        else:
            print("1 ile 12 arasında bir sınıf girin!")
            sure()
            continue

    elif op == "3":
        system("cls")
        secim = input("istiklal marşını görmek ister misiniz? (e/h): ")
        if secim.lower() == "e":
            system("cls")
            animasyon(hiz=0.2, dongu_sayisi=10)
            print("╔══════════════════════════════╗")
            print("║    İstiklal Marsı 1.kıta :)  ║")
            print("║══════════════════════════════║")
            print("║ Korkma Sönmez Bu Şafaklarda  ║")
            print("║ Yüzen Al Sancak; Sönmeden    ║")
            print("║ yurdumun üstünde tüten en son║")
            print("║ ocak. O benim milletimin     ║")
            print("║ yıldızıdır, parlayacak;      ║")
            print("║ O benimdir, o benim          ║")
            print("║ milletimindir ancak.         ║")    
            print("╚══════════════════════════════╝")
            sleep(15)
            continue
        
        else:
            print("Öyle Bir Seçeneğin Yok :)")
            sleep(3)
            system("cls")
            animasyon(hiz=0.2, dongu_sayisi=10)
            print("╔══════════════════════════════╗")
            print("║    İstiklal Marsı 1.kıta :)  ║")
            print("║══════════════════════════════║")
            print("║ Korkma Sönmez Bu Şafaklarda  ║")
            print("║ Yüzen Al Sancak; Sönmeden    ║")
            print("║ yurdumun üstünde tüten en son║")
            print("║ ocak. O benim milletimin     ║")
            print("║ yıldızıdır, parlayacak;      ║")
            print("║ O benimdir, o benim          ║")
            print("║ milletimindir ancak.         ║")    
            print("╚══════════════════════════════╝")
            sleep(15)
            continue
    elif op == "4":
        system("cls")
        print("╔═════════════════════╗")
        print("║ Ekran Yazdırma Uyg. ║")
        print("║═════════════════════║")
        print("║Ltf isminn Tammın yaz║")
        print("╚═════════════════════╝")
        a = input("isminizin tamamını giriniz: ").split()
        ad = " ".join(a[:-1]) if len(a) > 1 else a[0]
        system("cls")
        print("╔═══════════════════════════╗")
        print("║ Ekran Yazdırma Uyg.       ║")
        print("║═══════════════════════════║")
        print(f"║ {ad}'nin Annesi Gel Dedi ║")
        print("╚═══════════════════════════╝")
        sleep(7)
        continue
    
    elif op == "5":
        system("cls")  
        print("╔═════════════════════╗")
        print("║ Ekrana Ad Yazdırma  ║")  
        print("║═════════════════════║")
        print("║Ltf isminn Tammın yaz║")
        print("╚═════════════════════╝")
        a = input("isminizin tamamını giriniz: ").split()
        ad = " ".join(a[:-1]) if len(a) > 1 else a[0]
        system("cls")
        # ad değişkeni önceden tanımlı olsun
        for i in range(1, 101):
            print(f"{i}. {ad}")
        sleep(7)
        continue

    elif op == "6":
        usd_kur = 39.87
        eur_kur = 46.83
        
        system("cls")
        print("╔═════════════════════╗")
        print("║ Döviz Uygulaması    ║")
        print("║═════════════════════║")
        print("║1-Döviz Kurları      ║")
        print("║2-Döviz Hesaplama    ║")
        print("╚═════════════════════╝")
        secim = input("Seçiminizi yapınız (1/2): ")
        
        if secim == "1":
            system("cls")
            print("╔═════════════════════╗")
            print("║    Döviz Kurları    ║")
            print("║      6.07.2025      ║")
            print("║═════════════════════║")
            print("║    USD: 39.87 TL    ║")
            print("║    EUR: 46.83 TL    ║")
            print("╚═════════════════════╝")
            sleep(7)
            continue
        elif secim == "2":
            system("cls")
            secim = input("Hangi döviz? (1: USD, 2: EUR): ").strip()
            if secim == "1":
                miktar = float(input("Kaç USD?(örn:100): "))
                tl = miktar * usd_kur
                system("cls")
                print("╔═══════════════════════════╗")
                print("║      Döviz Hesaplama      ║")
                print("║═══════════════════════════║")
                print(f"║{miktar} USD = {tl:.2f} TL       ")
                print("╚═══════════════════════════╝")
                sleep(15)
                continue
            elif secim == "2":
                miktar = float(input("Kaç EUR?(örn:100): "))
                tl = miktar * eur_kur
                system("cls")
                print("╔═══════════════════════════╗")
                print("║      Döviz Hesaplama      ║")
                print("║═══════════════════════════║")
                print(f"║{miktar} EUR = {tl:.2f} TL     ")
                print("╚═══════════════════════════╝")
                sleep(15)
                continue
        
        else:
            print("Geçersiz seçim!")
            sleep(3)
            continue
    
    elif op == "7":
        
            system("cls")
            print("╔═════════════════════╗")
            print("║    Hesap Makinesi   ║")
            print("║═════════════════════║")
            print("║  1-Toplama          ║")
            print("║  2-Çıkarma          ║")
            print("║  3-çarpma           ║")
            print("║  4-Bölme            ║")
            print("║  5-Karenin Çevresi  ║")
            print("║  6-Sayı Farkları    ║")
            print("╚═════════════════════╝")
            op = input("Seçimiz nedir?: ")
            if op == "1":
                system("cls")
                a = int(input("1. Sayıyı Giriniz: "))
                b = int(input("2. Sayıyı Giriniz: "))
                system("cls")
                print("╔═════════════════════╗")
                print("║    Hesap Makinesi   ║")                
                print("║═════════════════════║")
                print("║    Toplama İşlemi   ║")
                print("║        Sonucu       ║")
                print("║        Nedir?       ║")
                print("║═════════════════════║")
                print("║  İşlemin Sonucu:    ║")
                print(f"║{a} + {b} = {a + b}          ")
                print("╚═════════════════════╝")
                sleep(10)
                continue
            elif op == "2":
                system("cls")
                a = int(input("1. Sayıyı Giriniz: "))
                b = int(input("2. Sayıyı Giriniz: "))
                system("cls")
                print("╔═════════════════════╗")
                print("║    Hesap Makinesi   ║")                
                print("║═════════════════════║")
                print("║    Çıkarma İşlemi   ║")
                print("║        Sonucu       ║")
                print("║        Nedir?       ║")
                print("║═════════════════════║")
                print("║  İşlemin Sonucu:    ║")
                print(f"║{a} - {b} = {a - b}          ")
                print("╚═════════════════════╝")
                sleep(10)
                continue
            elif op == "3":
                system("cls")
                a = int(input("1. Sayıyı Giriniz: "))
                b = int(input("2. Sayıyı Giriniz: "))
                system("cls")
                print("╔═════════════════════╗")
                print("║    Hesap Makinesi   ║")                
                print("║═════════════════════║")
                print("║     Çarpma İşlemi   ║")
                print("║        Sonucu       ║")
                print("║        Nedir?       ║")
                print("║═════════════════════║")
                print("║  İşlemin Sonucu:    ║")
                print(f"║{a} x {b} = {a * b}          ")
                print("╚═════════════════════╝")
                sleep(10)
                continue
            elif op == "4":
                a = int(input("1. Sayıyı Giriniz: "))
                b = int(input("2. Sayıyı Giriniz: "))
                if b == 0:
                    system("cls")
                    print("╔═════════════════════╗")
                    print("║    Hesap Makinesi   ║")
                    print("║═════════════════════║")
                    print("║      Bir Sayı 0'a   ║")
                    print("║       Bölünemez!    ║")
                    print("║          :(         ║")
                    print("╚═════════════════════╝")
                    sleep(10)
                    continue
                system("cls")
                print("╔═════════════════════╗")
                print("║    Hesap Makinesi   ║")                
                print("║═════════════════════║")
                print("║      Bölme İşlemi   ║")
                print("║        Sonucu       ║")
                print("║        Nedir?       ║")
                print("║═════════════════════║")
                print("║  İşlemin Sonucu:    ║")
                print(f"║{a} / {b} = {a / b}          ")
                print("╚═════════════════════╝")
                sleep(10)
                continue
            
            elif op == "5":
                a = int(input("Karenin Bir Kenarını Giriniz: "))
                alan = a ** 2
                system("cls")
                print("╔═════════════════════╗")
                print("║    Hesap Makinesi   ║")                
                print("║═════════════════════║")
                print("║    Karenin Çevresi  ║")
                print("║        Sonucu       ║")
                print("║        Nedir?       ║")
                print("║═════════════════════║")
                print("║  İşlemin Sonucu:    ║")
                print(f"║ {a} x 4 = {alan}    ")
                print("╚═════════════════════╝")
                sleep(10)
                continue
            
            elif op == "6":
                s1 = float(input("Birinci sayıyı giriniz: "))
                s2 = float(input("İkinci sayıyı giriniz: "))
                s = s1 - s2
                system("cls")
                print("╔═════════════════════╗")
                print("║    Hesap Makinesi   ║")                
                print("║═════════════════════║")
                print("║       Sayıların     ║")
                print("║        Farkı        ║")
                print("║        Nedir?       ║")
                print("║═════════════════════║")
                print("║  İşlemin Sonucu:    ║")
                print(f"║{s1} - {s2} = {s}  ")
                print("╚═════════════════════╝")
                sleep(10)
                continue
            
            else:
                print("Hatalı Veya Geçersiz Bir Seçim Yaptınız! Tekrar Deneyiniz. :/")
                sleep(7)
                continue
    
    elif op == "8":
        dogum_yili = int(input("Lütfen Doğum Yılınızı Giriniz(örn: 2000)"))
        simdiki_yil = datetime.now().year
        yas = simdiki_yil - dogum_yili
        if dogum_yili > simdiki_yil:
            print("╔═════════════════════╗")
            print("║   Sen Ciddi Misin?  ║")                
            print("║═════════════════════║")
            print("║    Daha Doğmadınız  ║")
            print("║          :(         ║")
            print("║═════════════════════║")
            print("║      ERROR :/       ║")
            print("╚═════════════════════╝")
            sleep(10)
        
        
        system("cls")
        print("╔═════════════════════╗")
        print("║   Yaş Tahmin edici  ║")                
        print("║═════════════════════║")
        print("║     Bence Sizim     ║")
        print("║       Yaşınız       ║")
        print("║═════════════════════║")
        print(f"║*       {yas}      ║")
        print("╚═════════════════════╝")
        sleep(10)
        continue
        
    elif op == "9":
        not_sayisi = int(input("Kaç tane not gireceksiniz? "))
        system("cls")
        toplam = 0
           
        for i in range(not_sayisi):
            notu = float(input(f"{i+1}. notu giriniz: "))
            toplam += notu
        durum = "Geçti" if ortalama >= 50 else "Kaldı"    

        ortalama = toplam / not_sayisi
        print("╔═════════════════════╗")
        print("║   Not Ortalamanız   ║")                
        print("║═════════════════════║")
        print("║ Geçtinmi Kaldın mı? ║")
        print(f"║   durum: {durum}   ║")
        print("║═════════════════════║")
        print(f"║Ortalaman:{ortalama}║")
        print("╚═════════════════════╝")
        sleep(10) 
    
    elif op == "10":
        boy = float(input("Boyunuzu metre cinsinden girin (örn: 1.71): "))
        ideal_kilo = boy * boy * 22
        system("cls")
        print("╔═════════════════════╗")
        print("║     İdeal Kilomuz   ║")                
        print("║═════════════════════║")
        print("║ Sizin İdeal Kilonuz ║")
        print(f"║{ideal_kilo:.1f} kg ║")
        print("╚═════════════════════╝")
        sleep(10)
        continue
    
    
    elif op == "11":
        system("cls")
        for _ in range(3):  
            for i in range(4):  
                system("cls")
                print("╔═════════════════════╗")
                print(f"║  Çıkış Yapılıyor{'.'*i:<3} ║")
                print("╚═════════════════════╝")
                sleep(0.3) 
        break
    else: 
        system("cls")
        print("Geçersiz Seçim! veya Hatalı Bir Seçim Yaptınız! Tekrar Deneyiniz. :/")
        sure()
        continue