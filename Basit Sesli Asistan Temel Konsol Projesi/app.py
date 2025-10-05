import aab
import speech_recognition as sr
from os import system

cikis_komut = ['6','altı','çıkış','kapat','programı kapat','program kapat','çık']
sil_komut = ['2','iki','dosya sil','rehber sil','dosya kaldır','rehber kaldır','kaldır']
kisi_sil_komut = ['4','dört','kişi sil','rehberden kişi sil','kişiyi sil','rehberden sil']
rehber_goruntule_komut = ['5','beş','rehberi görüntüle','rehberi göster','rehberi aç','rehber aç','görüntüle','göster']
olustur_komut = ['1','bir','oluştur','dosya oluştur','dosya yap']  # 'rehber' çıkarıldı
kisi_ekle_komut = ['3','üç','kişi ekle','rehbere kişi ekle','kişiyi ekle','rehbere ekle']

while True:
    system('cls')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        system
        print("╔═════════════════════╗")
        print("║  REHBER UYGULAMASI  ║")
        print("║═════════════════════║")
        print("║  1-Rehber Oluştur   ║")
        print("║  2-Rehber Kaldır    ║")
        print("║  3-Kişi Ekle        ║")
        print("║  4-Kişi Sil         ║")
        print("║  5-Rehber Görüntüle ║")
        print("║  6-Çıkış            ║")
        print("║═════════════════════║")
        print("║  Seçimiz nedir?     ║")
        print("╚═════════════════════╝")

        print("Lütfen Komutunuzu Söyleyin...")
        audio = r.listen(source)
        try:
            yazi = r.recognize_google(audio, language="tr-TR")
            print("Komut'unuz: ", yazi)
        except sr.UnknownValueError:
            print("Sizi Anlıyamadım")
            continue
        except sr.RequestError:
            print("Sistem Çalışmıyor")
            continue
        yazi_kucult = yazi.lower()

        if any(word in yazi_kucult for word in cikis_komut):
            print("Program Kapatılıyor...")
            break

        elif any(word in yazi_kucult for word in sil_komut):
            with sr.Microphone() as source:
                print("Silinecek Dosyanın Adını Söyleyin. [örnek: rehber]")
                audio = r.listen(source)
                try:
                    dosya_adim = r.recognize_google(audio, language="tr-TR")
                    print("Silinecek Dosyanın Adı: ", dosya_adim)
                    aab.sil(dosya_adim)
                    print(f"{dosya_adim} dosyası silindi.")
                    continue
                except sr.UnknownValueError:
                    print("Sizi Anlıyamadım")
                    continue
                except sr.RequestError:
                    print("Sistem Çalışmıyor")
                    continue

        elif any(word in yazi_kucult for word in kisi_sil_komut):
            with sr.Microphone() as source:
                print("Kişi Silinecek Dosyanın Adını Söyleyin. [örnek: rehber]")
                audio = r.listen(source)
                try:
                    dosya_adim = r.recognize_google(audio, language="tr-TR")
                    print("Kişi Silinecek Dosyanın Adı: ", dosya_adim)
                except sr.UnknownValueError:
                    print("Sizi Anlıyamadım")
                    continue
                except sr.RequestError:
                    print("Sistem Çalışmıyor")
                    continue
            with sr.Microphone() as source:
                print("Silinecek Kişinin Adını Ve Soyadını Söyleyin. [örnek: Ahmet Yılmaz]")
                audio = r.listen(source)
                try:
                    kisi_adim = r.recognize_google(audio, language="tr-TR")
                    print("Silinecek Kişinin Adı: ", kisi_adim)
                    aab.kisi_sil(dosya_adim, kisi_adim)
                    print(f"{kisi_adim} rehberden silindi.")
                    continue
                except sr.UnknownValueError:
                    print("Sizi Anlıyamadım")
                    continue
                except sr.RequestError:
                    print("Sistem Çalışmıyor")
                    continue

        elif any(word in yazi_kucult for word in rehber_goruntule_komut):
            with sr.Microphone() as source:
                print("Görüntülenecek Dosyanın Adını Söyleyin. [örnek: rehber]")
                audio = r.listen(source)
                try:
                    dosya_adim = r.recognize_google(audio, language="tr-TR")
                    print("Görüntülenecek Dosyanın Adı: ", dosya_adim)
                    aab.rehber_goruntule(dosya_adim)
                    continue
                except sr.UnknownValueError:
                    print("Sizi Anlıyamadım")
                    continue
                except sr.RequestError:
                    print("Sistem Çalışmıyor")
                    continue

        elif any(word in yazi_kucult for word in olustur_komut):
            with sr.Microphone() as source:
                print("Oluşturalacak Dosyanın Adını Söyleyin. [örnek: rehber]")
                audio = r.listen(source)
                try:
                    dosya_adim = r.recognize_google(audio, language="tr-TR")
                    print("Oluşturulacak Dosyanın Adı: ", dosya_adim)
                    aab.olustur(dosya_adim)
                    print(f"{dosya_adim} dosyası oluşturuldu.")
                    continue
                except sr.UnknownValueError:
                    print("Sizi Anlıyamadım")
                    continue
                except sr.RequestError:
                    print("Sistem Çalışmıyor")
                    continue

        elif any(word in yazi_kucult for word in kisi_ekle_komut):
            with sr.Microphone() as source:
                print("Kişi Eklenecek Dosyanın Adını Söyleyin. [örnek: rehber]")
                audio = r.listen(source)
                try:
                    dosya_adim = r.recognize_google(audio, language="tr-TR")
                    print("Kişi Eklenecek Dosyanın Adı: ", dosya_adim)
                except sr.UnknownValueError:
                    print("Sizi Anlıyamadım")
                    continue
                except sr.RequestError:
                    print("Sistem Çalışmıyor")
                    continue
            with sr.Microphone() as source:
                print("Eklenecek Kişinin Adını Ve Soyadını Söyleyin. [örnek: Ahmet Yılmaz]")
                audio = r.listen(source)
                try:
                    kisi_adim = r.recognize_google(audio, language="tr-TR")
                except sr.UnknownValueError:
                    print("Sizi Anlıyamadım")
                    continue
                except sr.RequestError:
                    print("Sistem Çalışmıyor")
                    continue
            with sr.Microphone() as source:
                print("Eklenecek Kişinin Telefon Numarasını Söyleyin. [örnek: 05551234567]")
                audio = r.listen(source)
                try:
                    kisi_numaram = r.recognize_google(audio, language="tr-TR")
                    print("Eklenecek Kişinin Numarası: ", kisi_numaram)
                    aab.kisi_ekle(dosya_adim, kisi_adim, kisi_numaram)
                    print(f"{kisi_adim} rehbere eklendi.")
                    continue
                except sr.UnknownValueError:
                    print("Sizi Anlıyamadım")
                    continue
                except sr.RequestError:
                    print("Sistem Çalışmıyor")
                    continue
