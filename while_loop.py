# PYTHON'DA WHİLE DÖNGÜLERİ

# 1-100 'e kadar sayıların ekrana  yazılması.


x = 1 
while x <= 100:
    print(x)
    x += 1
print("Döngü bitti.")

# 1-100 aralığındaki tek sayıların ekrana yazılması.

y = 1 
while y <= 100:
    if (y % 2 != 0):
        print(f"Sayı tektir: {y}")
    else:
        print(f"Sayı çifttir: {y}")
    y += 1
print("Döngü bitti.")


name = '' # False

while not name.strip():   # name'de boşluk değer False olarak algılanır döngünün başlaması için not operatörünü kullandık.
    name = input("İsminizi giriniz: ") # bir karakter girmediğimiz müddetçe döngü devam eder, boşluk karakteri girersek döngü sonlanır.
print(f"Merhaba {name}")

# ALIŞTIRMALAR

sayilar = [1,3,5,7,9,12,19,21]

# 1-) Sayılar listesini while ile ekrana yazdırın.

s = 0

while s < len(sayilar):
    print(sayilar[s])
    s += 1

# 2-) Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları yazdırın.

baslangıc = int(input("Başlangıç değerini giriniz: "))
bitis = int(input("Bitiş değerini giriniz: "))

while baslangıc <= bitis:
    if baslangıc % 2 != 0:
        print(baslangıc)
    baslangıc += 1


# 3-) 1-100 arasındaki sayıları azalan şekilde yazdırın.

i = 100
while i >= 1:
    print(i)
    i -= 1

# 4-) Kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın.

k = 0
sayilar = []
while k < 5:
    sayi = int(input("Lütfen 5 adet sayı giriniz: "))
    sayilar.append(sayi)
    k += 1
sayilar.sort()
print(sayilar)


# 5-) Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#     ** ürün sayısını kullanıcıya sorun.
#     ** dictionary listesi yapısı (name, prace) şeklinde olsun.
#     ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin. 


urunler = []
urun_sayisi = int(input("Ürün sayısını giriniz: "))
while urun_sayisi > 0:
    urun_ismi = input("Name: ")
    urun_fiyatı = input("Price: ")

    urunler.append({
        'name' : urun_ismi,
        'price': urun_fiyatı
        })
    urun_sayisi -= 1

for urun in urunler:
    print(f"Ürün adı: {urun['name']} Ürün fiyatı: {urun['price']}")
