#Ege-School
import sqlite3

# Veritabanını oluştur ve bağlantı kur
def veritabani_olustur():
    conn = sqlite3.connect('ege-school.db')
    c = conn.cursor()

    # Öğrenciler tablosunu oluştur
    c.execute('''CREATE TABLE IF NOT EXISTS Öğrenciler (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 isim TEXT NOT NULL,
                 soyisim TEXT NOT NULL,
                 sınıf TEXT NOT NULL,
                 numara INTEGER NOT NULL UNIQUE)''')

    # Notlar tablosunu oluştur
    c.execute('''CREATE TABLE IF NOT EXISTS Notlar (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 öğrenci_id INTEGER,
                 ders TEXT NOT NULL,
                 not_degeri INTEGER NOT NULL,
                 FOREIGN KEY (öğrenci_id) REFERENCES Öğrenciler(id))''')

    # Devamsızlık tablosunu oluştur
    c.execute('''CREATE TABLE IF NOT EXISTS Devamsızlık (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 öğrenci_id INTEGER,
                 tarih TEXT NOT NULL,
                 FOREIGN KEY (öğrenci_id) REFERENCES Öğrenciler(id))''')

    # Değişiklikleri kaydet ve bağlantıyı kapat
    conn.commit()
    conn.close()

# Öğrenci ekleme
def ogrenci_ekle(isim, soyisim, sınıf, numara):
    conn = sqlite3.connect('ege-school.db')
    c = conn.cursor()
    c.execute('INSERT INTO Öğrenciler (isim, soyisim, sınıf, numara) VALUES (?, ?, ?, ?)', (isim, soyisim, sınıf, numara))
    conn.commit()
    conn.close()

# Öğrenci notu ekleme
def not_ekle(ogrenci_id, ders, not_degeri):
    conn = sqlite3.connect('ege-school.db')
    c = conn.cursor()
    c.execute('INSERT INTO Notlar (öğrenci_id, ders, not_degeri) VALUES (?, ?, ?)', (ogrenci_id, ders, not_degeri))
    conn.commit()
    conn.close()

# Öğrenci devamsızlık ekleme
def devamsizlik_ekle(ogrenci_id, tarih):
    conn = sqlite3.connect('ege-school.db')
    c = conn.cursor()
    c.execute('INSERT INTO Devamsızlık (öğrenci_id, tarih) VALUES (?, ?)', (ogrenci_id, tarih))
    conn.commit()
    conn.close()

# Öğrencileri listeleme
def ogrencileri_listele():
    conn = sqlite3.connect('ege-school.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Öğrenciler')
    öğrenciler = c.fetchall()
    conn.close()
    return öğrenciler

# Öğrenci notlarını listeleme
def notlari_listele(ogrenci_id):
    conn = sqlite3.connect('ege-school.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Notlar WHERE öğrenci_id=?', (ogrenci_id,))
    notlar = c.fetchall()
    conn.close()
    return notlar

# Öğrenci devamsızlıklarını listeleme
def devamsizliklari_listele(ogrenci_id):
    conn = sqlite3.connect('ege-school.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Devamsızlık WHERE öğrenci_id=?', (ogrenci_id,))
    devamsizliklar = c.fetchall()
    conn.close()
    return devamsizliklar

# Ana menü
def menu():
    veritabani_olustur()  # Veritabanını ve tabloları oluştur

    while True:
        print("\nEge-School Yönetim Sistemi")
        print("1. Öğrenci Ekle")
        print("2. Öğrencileri Listele")
        print("3. Not Ekle")
        print("4. Notları Görüntüle")
        print("5. Devamsızlık Ekle")
        print("6. Devamsızlıkları Görüntüle")
        print("7. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            isim = input("Öğrencinin İsmi: ")
            soyisim = input("Öğrencinin Soyismi: ")
            sınıf = input("Öğrencinin Sınıfı: ")
            numara = int(input("Öğrenci Numarası: "))
            ogrenci_ekle(isim, soyisim, sınıf, numara)
            print("Öğrenci eklendi!")

        elif secim == "2":
            öğrenciler = ogrencileri_listele()
            for öğrenci in öğrenciler:
                print(f"ID: {öğrenci[0]}, İsim: {öğrenci[1]}, Soyisim: {öğrenci[2]}, Sınıf: {öğrenci[3]}, Numara: {öğrenci[4]}")

        elif secim == "3":
            öğrenci_id = int(input("Öğrenci ID: "))
            ders = input("Ders: ")
            not_degeri = int(input("Not: "))
            not_ekle(öğrenci_id, ders, not_degeri)
            print("Not eklendi!")

        elif secim == "4":
            öğrenci_id = int(input("Öğrenci ID: "))
            notlar = notlari_listele(öğrenci_id)
            for not_ in notlar:
                print(f"Ders: {not_[2]}, Not: {not_[3]}")

        elif secim == "5":
            öğrenci_id = int(input("Öğrenci ID: "))
            tarih = input("Tarih (YYYY-MM-DD): ")
            devamsizlik_ekle(öğrenci_id, tarih)
            print("Devamsızlık eklendi!")

        elif secim == "6":
            öğrenci_id = int(input("Öğrenci ID: "))
            devamsizliklar = devamsizliklari_listele(öğrenci_id)
            for devamsizlik in devamsizliklar:
                print(f"Tarih: {devamsizlik[2]}")

        elif secim == "7":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Menü arayüzünü başlat
menu()
