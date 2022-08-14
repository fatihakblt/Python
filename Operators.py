# PYTHON OPERATÖRLERİ


# ATAMA OPERATÖRLERİ
# x = 5  
# y = 10
# z = 20  

x, y, z = 5, 10, 20
print(x, y, z)

x += 5  # x = x + 5
x -= 5  # x = x - 5
x *= 5  # x = x * 5
x /= 5  # x = x / 5
y //= 3 # y = y // 3  kalansız bölme işlemi yapar. 10//3 = 3 olur.
x **= 2 # x = x ** 2  x'in karesi ilemi.
x **= z # x = x ** z  x üzeri z işlemi.

values = 1, 2, 3, # values = (1,2,3) ile aynı yani tuple.
print(values)
print(type(values))

x, y, z, = values   # x, y, z, ifadelerine valuesteki değerlerin atanabilmesi için atanacak elemaların sayısı değişken sayısına eşit olmalıdır.
print(x, y,z ) 

values1 = 1, 2, 3, 4, 5
a, b, *c = values1 # ilk iki eleman sırasıyla a ve b'ye atanır c'nin başına yıldız konulduğu için diğer elemanlar liste biçiminde c'ye atanır.
print(a, b, c)    # a = 1 b = 2  c = [3, 4, 5]
print(type(c))
print(a, b, c[1])


# ALIŞTIRMALAR

x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1-) Kullanıcıdan alacağınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
a = int(input("Lütfen 1. sayıyı giriniz: "))
b = int(input("Lütfen 2. sayıyı giriniz: "))
result1 = (a * b) - (x + y + z)
print(result1)
# 2-) y'nin x'e kalansız bölümünü hesaplaynız.
result2 = y//x
print(result2)

# 3-) (x, y, z) toplamının mod 3' ü nedir?
result3 = (x + y + z ) % 3
print(result3)

# 4-) y'nin x. kuvvetini hesaplayınız.
result4 = y ** x
print(result4)


 # 5-) x, *y, z = numbers   işlemine göre z'nin küpü kaçtır?
x, *y, z = numbers
result5 = z ** 3
print(result5)

# 6-)  x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
x, *y, z = numbers
result6 = y[0] + y[1] + y[2]
print(result6)


# KARŞILAŞTIRMA OPERATÖRLERİ

# username, password => database
# 'sadikturan', '123456'

# a, b, c, d = 5, 5, 10, 4

password = '1234'
username = 'fatihakbulut'



result7 = (a == b)  # True
result8 = (a == c)  # False
print(result7)
print(result8)

result9 = ('fthakblt' == username) # False
result10 = ('fatihakbulut' == username) # True 
print(result9)
print(result10)

result11 = (a != b) # False 
result12 = (a != c) # True
print(result11)
print(result12)


result13 = (a > c) # False
result14 = (a < c) # True
print(result13)
print(result14)

result15 = (a >= c) # False
result16 = (a <= c) # True
print(result15)
print(result16)

# ALIŞTIRMALAR

# 1-) Girilen 2 sayıdan hangisi büyüktür?
a = int(input("1.sayı: "))
b = int(input("2.sayı: "))

result17 = (a > b)
result18 = (b > a)
print(f"{a} sayısı {b} sayısından büyüktür: {result17}")
print(f"{b} sayısı {a} sayısından büyüktür: {result18}")

# 2-) Kullanıcıdan  vize(%40) ve final(%60) notunu alıp ortalama hesaplayınız, geçme notu:50 ekrana geçip geçmediğini yazdırınız..
v = int(input("Vize notunuz: "))
f = int(input("Final notunuz: "))

average = (v * 40 + f *60)/100
result19 = (average >= 50)
print(f"Ortalama : {average}, Geçme durumu: {result19}")


# 3-) Girilen bir sayının tek-çift durumunu yazın.
c = int(input("Bir sayı giriniz: "))
result20 = (c % 2 == 0)
print(f"{c} sayısı çift mi: {result20}")

# 4-) Girilen bir sayının negatif-pozitif durumunu yazın.
d = int(input("Bir tam sayı giriniz: "))
result21 = (d > 0)
print(f"{d} sayısı pozitif mi: {result21}")

# 5-) Parola ve email bilgisini isteyip doğruluğunu kontrol edin.
email = "fatihakbulut@gmail.com"
password = 'fatih5354'

email_in = input("Email: ")
password_in = input("Password: ")
isEmail = (email_in == email)
isPassword = (password == password_in.lower().strip()) # Lower ile büyük-küçük harf duyarlılığını kaldırdk.
print(f"Email: {isEmail}, Password: {isPassword}")     # Strip ile boşluk karakterini silerek parolayı etkilememesini sağladık.



# MANTIKSAL OPERATÖRLER
x = 6 
hak = 5
devam = 'e'
result22 = 5 < x < 10
print(result22)

# AND OPERATÖRÜ
result23 = (x > 5) and (x < 10)   # True and True => True
result24 = (hak > 0) and (devam == 'e')
print(result24)


# OR OPERATÖRÜ
result25 = (x > 0) or (x % 2 == 0)
print(result25)
# True or False => True
# True or True => True
# False or False => False

# NOT OPERATÖRÜ
result26 = not(x > 0)
print(result26)


# ALIŞTIRMALAR


# 1-) Girilen bir sayının 0-100 (100 dahil) arasında olup olmadığını kotrol ediniz.
number = int(input("Bir sayı giriniz: "))
result27 = (0 < number) and (number <= 100)
print(result27)

# 2-) Girilen bir sayının pozitif bir çift sayı olup olmadığını kontrol ediniz.
number1 = int(input("Bir sayı giriniz: "))
result28 = (number1 > 0) and (number1 % 2 == 0)
print(result28)

# 3-) Email ve parola bilgileri ile giriş kontrolü yapınız.
email1 = "fatih@gmail.com"
password1 = '232425'

email1_in = input("Email:")
password1_in = input("Password:")

result29 = (email1 == email1_in) and (password1 == password1_in)
print(result29) 

# 4-) Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
number_a = int(input("1.sayı: "))
number_b = int(input("2.sayı: "))
number_c = int(input("3.sayı: "))

result30 = (number_a > number_b) and (number_a > number_c)
print(f"1.sayı en büyük sayıdır: {result30}")

result30 = (number_b > number_a) and (number_b > number_c)
print(f"2.sayı en büyük sayıdır: {result30}")

result30 = (number_c > number_a) and (number_c > number_b)
print(f"3.sayı en büyük sayıdır: {result30}")

# 5-) Kullanıcıdan 2 vize (%60) ve 1 final (%40) notunu alıp ortalama hesaplayınız.
#     Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#     a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#     b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = int(input("1.vize: "))
vize2 = int(input("2.vize: "))
final1 = int(input("Final: "))

ortalama1 = (((vize1 + vize2) / 2) * 0.6) + (final1 * 0.4)
gecti_mi = ((ortalama1 >= 50) and (final1 >=50)) or (final1 >= 70)
print(f"Öğrencinin ortalaması: {ortalama1}, geçme durumu: {gecti_mi}")


# 6-) Kişinin ad, kilo ve boy bilgilerini alıp kilo indeksini hesaplayınız.
#     Formül: (Kilo / boy uzunluğunun karesi)
'''
Aşağıdaki tabloya göre  kişi kilo indeksine göre hangi gruba girmektedir:

0-18.4       => Zayıf
18.5-24.9    => Normal
25.0-29.9    => Fazla Kilolu
30.0-34.9    => Şişman(Obez)
'''

isim = input("İsminiz: ")
kilo = float(input("Kilonuz: "))
boy = float(input("Boyunuz: "))

indeks = (kilo) / (boy ** 2)
Zayif = (indeks >= 0) and (indeks <= 18.4)
Normal = (indeks >= 18.5) and (indeks <= 24.9)
Kilolu = (indeks >= 25.0) and (indeks <= 29.9)
Obez = (indeks >= 30.0) and (indeks <= 34.9)

print(f"{isim} zayıf mı:  {Zayif}")
print(f"{isim} normal mi: {Normal}")
print(f"{isim} kilolu mu: {Kilolu}")
print(f"{isim} obez mi:   {Obez}")

# PYTOHN'DA DİĞER OPERATÖRLER

# IDENTITY OPERATOR: is

l = n = [1, 2, 3]
m = [1, 2, 3]
print(l == n)
print(l == m)

print(l is n ) # l ile n'nin aynı adresi gösterip göstermediğini tespit etmek için is operatörünü kullandık.
print(l is m)

k = [1, 2, 3]
t = [2, 4]

print( k is t) # k ile t farklı bellek adresine sahiptir.Referansları aynı değildir.

# MEMBERSHİP OPERATOR: in

meyveler = ['apple', 'banana']
print('banana' in meyveler)   # banana öğesi meyveler listesinde var mıdır.

ad = "Fatih"
print("a" in ad) 