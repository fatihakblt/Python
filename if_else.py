# PYTHON'DA KOŞUL BLOKLARI

# if - else koşulu

username = "fatih"
password = "12345"

isloggedin = (username == "fatih") and (password == "12345")

if isloggedin:                       # Eğer isloggedin içindeki karşılaştırmaların sonucu  doğru ise if bloğundaki ifade ekrana yazdırılır ve else bloğu kullanılmaz.
    print("Hoşgeldiniz")
else:                                # Eğer isloggedin içindeki karşılaştırmaların sonucu yanlış ise if bloğuna girilmeden else bloğunun içindeki ifade  ekrana yazdırılır.
    print("Yanlış bilgi girdiniz!")


if (username == "fatih"):
    if(password == "12345"):
        print("Hoşgeldiniz.")
    else:
        print("Yanlış parola!")
else:
    print("Yanlış kullanıcı adı!")

# if -elif -else koşulu

x = 20
y = 20

if x > y:
    print("x, y'den büyüktür.")
elif x == y:
    print("x, y'ye eşittir.")
else:
    print("x, y'den büyük değildir. ")


num = int(input("Sayı: "))

if num > 0:
    print("Sayı pozitif.")
elif num <0:
    print("Sayı negatif.")
else:
    print("Sayı sıfır.")


# ALIŞTIRMALAR



# 1-) Kullanıcıdan isim, yaş ve eğtim bilgilerini isteyip ehliyet alabilme durumunu kontrol
#     ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

kullanıcı_isim = input("İsminizi giriniz: ")
kullanıcı_yas = int(input("Yaşınızı giriniz: "))
kullanıcı_egitim = input("Eğitim düzeyinizi  giriniz: ")

if kullanıcı_yas >= 18:
    if (kullanıcı_egitim == "lise") or (kullanıcı_egitim == "üniversite" ):
        print(f"{kullanıcı_isim} ehliyet alabilirsin.")
    else:
        print(f"{kullanıcı_isim} eğitim düzeyin yetersiz!")
else:
    print(f"{kullanıcı_isim} en az 18 yaşında olmalısın!")

# 2-) Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre not 
#     aralığına karşılık gelen not bilgisini yazdırınız.
#     0 -24  => 0
#     25-44  => 1
#     45-54  => 2
#     55-69  => 3
#     70-84  => 4
#     85-100 => 5

exam1 = int(input("1.yazılı: "))
exam2 = int(input("2.yazılı: "))
quiz = int(input("Sözlü: "))
average = (exam1 + exam2 + quiz)/3

if (average >= 0 ) and (average <= 24):
    print(f"Ortalamanız: {average} Notunuz: 0")
elif (average >= 25) and (average <= 44):
    print(f"Ortalamanız: {average} Notunuz: 1")
elif (average >= 45) and (average <= 54):
    print(f"Ortalamanız: {average} Notunuz: 2")
elif (average >= 55) and (average <= 69):
    print(f"Ortalamanız: {average} Notunuz: 3")
elif (average >= 70) and (average <= 84):
    print(f"Ortalamanız: {average} Notunuz: 4")
elif (average >= 85) and (average <= 100):
    print(f"Ortalamanız: {average} Notunuz: 5")
else:
    print("Hatalı notlar girdiniz!")


# 3-) Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#     1.Bakım => 1. yıl
#     2.Bakım => 2. yıl
#     3.Bakım => 3. yıl
#     ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
#     *** datatime modülünü kullanmanız gerekiyor.
import datetime   # Mevcut tarihi tespit etmek için kullandığımız modül.

tarih = input("Aracınız hangi tarihte trafiğe çıktı(Gün/Ay/Yıl): ")
tarih = tarih.split('/')

trafigeCikis = datetime.datetime(int(tarih[2]),int(tarih[1]),int(tarih[0]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis

gun = (fark.days)       # Gün olarak hesaplamak için .days kullandık.
if gun <= 365:
    print("1. servis aralığı.")
elif (gun > 365) and (gun <= 365*2):
    print("2. servis aralığı.")
elif (gun > 365*2) and (gun <= 365*3):
    print("3. servis aralığı.")
else:
    print("Hatalı süre.")

# 4-) Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
number = int(input("Bir sayı giriniz: "))

if (number >= 0 and number <= 100):
    print(f"{number} sayısı 0-100 aralığındadır.")
else:
    print(f"{number} sayısı 0-100 aralığında değildir. ")

# 5-) Girilen bir sayının pozitif-çift olup olmadığını kontrol ediniz.
number1 = int(input("Bir sayı giriniz: "))

if number1 > 0:
    print("Sayı pozitiftir.")
else:
    print("Sayı negatiftir.")
if number1 % 2 == 0:
    print("Sayı çifttir.")
else:
    print("Sayı tektir.")

# 6-) Email ve parola bilgileri ile giriş kontrolü yapınız.

email = "fatihakbulut@gmail.com"
password1 = "123456"

girilen_email = input("Email: ")
girilen_password = input("Password:")

if (girilen_email == email):
    if(girilen_password == password1):
        print("Giriş başarılı.")
    else:
        print("Parolanız yanlış.")
else:
    print("Email bilginiz yanlış.")
