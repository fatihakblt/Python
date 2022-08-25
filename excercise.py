'''
    Soru: 1-100 arasında rastgele  üretilecek bir sayıyı aşağı yukarı ifadeleriyle buldurmaya çalışın.

    **"random modülü için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.

'''
import random
sayi = random.randint(1,100)
hak = int(input("Kaç hak istiyorsunuz: "))
sayac = 0
print(sayi)
puanlama = 100 / hak
while hak > 0:
    tahmin = int(input("Sayıyı tahmin edin:"))
    hak -= 1 
    sayac += 1
    if tahmin < sayi:
        print("Daha büyük bir sayı tahmin edin!")
    elif tahmin > sayi:
        print("Daha küçük bir sayı tahmin edin!")
        
    elif tahmin == sayi:
        print(f"Tebrikler, {sayac}. denemede doğru tahmin, puanınız: {100 -(puanlama) * (sayac-1)}")
        break
    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")





'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir. 
'''

sayi = int(input("Sayı:"))
asalMi = True
if sayi == 1:
    print("1 sayısı asal değildir.")

for i in range(2,sayi):
    if sayi % i == 0:
        asalMi = False
        break
if asalMi:
    print(f"{sayi} sayısı asaldır.")
else:
    print(f"{sayi} sayısı asal değildir.")
