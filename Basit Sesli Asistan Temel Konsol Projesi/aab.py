import os
from time import sleep

def olustur(dosya_adi):
    yol = f"{dosya_adi}.txt"
    if os.path.exists(yol):
        print(f"{yol} zaten mevcut.")
        sleep(2)
        return
    try:
        with open(yol, "x", encoding="utf-8"):
            pass
        print(f"{yol} oluşturuldu.")
    except FileExistsError:
        print(f"{yol} zaten mevcut.")
    except OSError as e:
        print(f"{yol} oluşturulurken hata: {e}")
    sleep(2)

def sil(dosya_adi):
    import os
    from time import sleep
    yol = f"{dosya_adi}.txt"
    if os.path.exists(yol):
        try:
            os.remove(yol)
            print(f"{yol} silindi.")
        except OSError as e:
            print(f"{yol} silinirken hata: {e}")
    else:
        print(f"{yol} bulunamadı.")
    sleep(2)


def kisi_ekle(dosya_adi, kisi_adi, kisi_numarasi):
    yol = f"{dosya_adi}.txt"
    if os.path.exists(yol):
        try:
            with open(yol, "a", encoding="utf-8") as file:
                file.write(f"{kisi_adi}: {kisi_numarasi}\n")
            print(f"{kisi_adi} rehbere eklendi.")
        except OSError as e:
            print(f"Yazma hatası: {e}")
    else:
        print(f"{yol} bulunamadı. Önce dosyayı oluşturun.")
    sleep(2)

def kisi_sil(dosya_adi, kisi_adi):
    import os
    from time import sleep
    yol = f"{dosya_adi}.txt"
    if not os.path.exists(yol):
        print(f"{yol} bulunamadı.")
        sleep(2)
        return
    with open(yol, "r", encoding="utf-8") as f:
        satirlar = f.readlines()
    yeni = []
    silinen = 0
    for s in satirlar:
        ad = s.split(":", 1)[0].strip()
        if ad == kisi_adi:
            silinen += 1
        else:
            yeni.append(s)
    if silinen:
        with open(yol, "w", encoding="utf-8") as f:
            f.writelines(yeni)
        print(f"{kisi_adi} kaydı silindi. ({silinen})")
    else:
        print(f"{kisi_adi} kaydı bulunamadı.")
    sleep(2)


def rehber_goruntule(dosya_adi):
    import os
    from time import sleep
    yol = f"{dosya_adi}.txt"
    if not os.path.exists(yol):
        print(f"{yol} bulunamadı.")
        sleep(2)
        return
    try:
        with open(yol, "r", encoding="utf-8") as file:
            icerik = file.read().strip()
            if icerik:
                print(f"{yol} içeriği:\n{icerik}")
            else:
                print(f"{yol} boş.")
    except OSError as e:
        print(f"Okuma hatası: {e}")
    sleep(2)

