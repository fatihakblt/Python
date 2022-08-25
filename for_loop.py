# PYTHON'DA FOR DÖNGÜLERİ



numbers = [1, 2, 3, 4, 5]  # 5 elemanlı numbers listesi tanımladık.


for num in numbers:        # umbers listesinin içindeki tüm elemanları yazdırmak için oluşturulan for döngüsü.
    print(num)

names = ["fatih", 'Göktuğ', 'mehmet']

for name in names:
    print(f"My name is {name}")


isim = "fatih akbulut"      # String bir ifade tanımladık.

for ad in isim:             # Bu for döngüsü ile string ifadenin tüm karakterleri ekrana yazdırılır.
    print(ad)

tuple = [(1,2), (1,3), (3,5),(5,7)] # 4 elemanlı bir tuple listesi oluşturduk.

for a,b in tuple:                   # Her bir tuple'nin elemanlarını yazdırmak için kullanılan for döngüsü.
    print(a,b)

dict = {'k1':1, 'k2':2, 'k3':3}     # dict adında bir dictionary tanımladık. 

for d in dict:                      # Tüm anahtar kelimeleri yazdırmak için kullanılan for döngüsü.
    print(d)

for key,value in dict.items():      # Tüm anahtar - değerleri yazdırmak için kullanılan döngü.
    print(key, value)               # .items() ile tüm eleman gruplarına ulaşırız. ör: ('k1', 1) gibi.


# ALIŞTIRMALAR

sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1-) Sayilar listesindeki hangi sayilar 3'ün katıdır?

for sayi in sayilar:
    if (sayi %3 == 0):
        print(sayi)

# 2-) Sayilar listesindeki sayıların toplamı kaçtır?
toplam = 0
for sayi in sayilar:
    toplam += sayi 
print(toplam)

# 3-) Sayilar listesindeki tek sayıların karesini alınız.

for sayi in sayilar:
    if (sayi %2 != 0):
        print(sayi ** 2)

# 4-) Şehirlerden hangileri en fazla 5 karakterlidir?
sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

for sehir in sehirler:
    if(len(sehir) <= 5):
        print(sehir)



urunler = [
    {'name':  'samsung s6', 'price': '3000'},
    {'name':  'samsung s7', 'price': '4000'},
    {'name':  'samsung s8', 'price': '5000'},
    {'name':  'samsung s9', 'price': '6000'},
    {'name': 'samsung s10', 'price': '7000'}

]

# 5-) Ürünlerin fiyatları toplamı nedir?
toplam = 0
for urun in urunler:
    toplam += int(urun['price'])
print(toplam)


# 6-) Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

for urun in urunler:
    if (int(urun['price']) <= 5000):
        print(urun['name'])
