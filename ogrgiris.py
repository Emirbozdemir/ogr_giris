import os

kayıt_dosyası = "Kayıt dosyası.txt"


# Kayıt dosyasının varlığını kontrol et
def kayit_sorgu():
    return os.path.exists(kayıt_dosyası)


# Öğrenci kaydını dosyaya yaz
def ögrenci_kaydi(ogr_ad_soyad, ogr_tc):
    with open(kayıt_dosyası, "a") as f:
        f.write(f"{ogr_ad_soyad},{ogr_tc}\n")


# Öğrencinin girişini kontrol et
def ogr_giris(ogr_ad_soyad, ogr_tc):
    if not kayit_sorgu():
        print("Kayıtlı öğrenci bulunamadı!")
        return False

    with open(kayıt_dosyası, "r") as f:
        for satir in f:
            kayıt_ogr_ad_soyad, kayıt_ogr_tc = satir.strip().split(",")
            if ogr_ad_soyad == kayıt_ogr_ad_soyad and ogr_tc == kayıt_ogr_tc:
                return True
    return False


# Uygulamanın ana işlevi
def uygulama():
    print("1. Giriş yap")
    print("2. Kayıt ol")
    secim = input("Bir seçenek giriniz (1/2): ")

    if secim == "2":
        ogr_ad_soyad = input("Öğrenci adını soyadını giriniz = ")
        ogr_tc = input("Öğrencinin Tc kimlik numarasını giriniz = ")

        # Eğer TC sayısal değilse hata ver
        if not ogr_tc.isdigit():
            print("Geçersiz TC numarası.")
            return

        ogr_tc = int(ogr_tc)

        # Öğrenci zaten kayıtlı mı diye kontrol et
        if ogr_giris(ogr_ad_soyad, ogr_tc):
            print("Kayıt zaten sistemde mevcut.")
        else:
            ögrenci_kaydi(ogr_ad_soyad, ogr_tc)
            print("Kayıt başarılı.")

    elif secim == "1":
        ogr_ad_soyad = input("Öğrencinin adını giriniz = ")
        ogr_tc = input("Öğrencinin TC kimlik numarasını giriniz = ")

        # Eğer TC sayısal değilse hata ver
        if not ogr_tc.isdigit():
            print("Geçersiz TC numarası.")
            return

        ogr_tc = int(ogr_tc)

        # Öğrenciyi sisteme giriş yapmaya çalış
        if ogr_giris(ogr_ad_soyad, ogr_tc):
            print("Giriş başarılı.")
        else:
            print("Hatalı öğrenci adı ya da TC.")
    else:
        print("Geçersiz seçenek.")


# Uygulamayı çalıştır
if __name__ == "__main__":
    uygulama()
