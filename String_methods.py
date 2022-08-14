# PYTHON'DA BAZI STRİNG METOTLARI:


# Capitalize() metodu: Karakter dizisi içindeki ilk harfi büyük harfe dönüştürür. 
'''
website = "fatihakbulut.com"
print(website.capitalize())

->Fatihakbulut.com
'''
# Title metodu: Karakter dizisi içindeki bütün kelimelerin ilk harfini büyük harfe dönüştütür.
'''
website = "fatih akbulut.com "
print(website.title())

->Fatih Akbulut.Com
'''
# Count metodu: Karakter dizisi içinde istenilen karakterden kaç tane olduğunu gösterir.
'''
website = "fatihakbulutt.com"
print(website.count('t'))

->3
'''
# Upper metodu: Karakter dizisi içindeki tüm küçük harfleri büyük harfe dönüştürür.
'''
website = "fatihakbulut.com"
print(website.upper())

->FATİHAKBULUT.COM
''' 
# Lower metodu: Karakter dizisi içindeki tüm büyük harfleri küçük harfe dönüştürür.
'''
website = "FatihAkbulut.COM"
print(website.lower())

->fatihakbulut.com
'''
# Swapcase metodu: Karakter dizisindeki büyük harfi küçük harfe,küçük harfi büyük harfe dönüştürür.
'''
website = "FATİHakbulut.com"
print(website.swapcase())

->fatihAKBULUT.COM
'''
# Center metodu: Bu method içinde belirtilen miktar kadar sağdan ve soldan boşluklarla karakter dizisini ortatalar.
'''
website = "fatihakbulut.com"
print(website.center(8))

->        fatihakbulut.com
'''
# Replace metodu: Bu method karakter dizisi içindeki bir karakteri başka bir karakterle değiştirir.
'''
website fatihakbulut.com
print(website.replace("u","a"))

->fatihakbalat.com
'''

'''
!!!
Not: 
Biz  bu metotlar ile büyük harfe çevirme küçük harfe çevirme karakterleri değiştir gibi işlemler yaptık 
ama burada dikkat etmeniz gereken bir şey var karakter dizileri değiştirilemez veri türü olduğu için aslında 
değiştirmiyor sadece bize işlemin uygulanmış halini  gösteriyor. Orijinal dizi hep aynı kalıyor.
'''

# Startswith metodu: Karakter dizisinin hangi karakter ile başlayıp başlamadığını sorgular.
'''
website = "fatihakbulut.com"
print(website.startswith("f"))

->True
'''
# Endswith metodu: Bu method karakter dizisinin hangi karakter veya karakterler ile bitip bitmediğini kontrol eder.
'''
website = "fatihakbulut.com"
print(website.endswith("com"))

->True
'''
# Isapla metodu: Bu method bir karakter dizisinin alfabetik olup olmadığını kontrol eder.
'''

website = "fatihakbulut"
print(website.isalpha())

->True 

website = "fatihakbulut.com"
print(website.isalpha())

->False
'''
# Isdigit metodu:  Bu method karakter dizisinin sayısal bir değer olup olmadığını kontrol eder.
'''
website = "19216811"
print(website.isdigit())

->True
'''
# Find metodu: Bu method karakter dizisi içinde karakterin kaçıncı indekste olduğunu bulan metottur.
'''
website = "fatihakbulut.com"
print(website.find("i"))

->3
'''
# Rfind metodu: Bu method find ile aynı işlevi görür tek farkı sağdan sola doğru okur.
'''
website = "fatihakbulut.com"
print(website.rfind('u'))

->5
'''
# Index metodu: Find metoduyla aynı işlevi yapar tek fark index metodu aranılan karakter yoksa hata verir.
'''
website = "fatihakbulut.com"
print(website.index('h'))

->4
'''
# Join metodu: Bu method ekleme işlemi yapar.
'''
website = "fatihakbulut.com"
print("*".join(website))

->f*a*t*i*h*a*k*b*u*l*u*t*.*c*o*m

diller = ["Python","java","C","Kotlin"]
print(",".join(diller))

->Python,java,C,Kotlin
'''
# Split metodu: Bu method karakter dizlerini parçalara ayırır.
'''
diller = "Python,Java,Ruby,C#"
print(diller.split(","))

->['Python','Java','Ruby','C#']
'''
# Strip metodu: Bu method karakter dizisinin başındaki ve sonundaki boşluk karakterleri siler. 
'''
website = "   fatihakbulut.com  "
print(website.strip())

->fatihakbulut.com
'''


# ALIŞTIRMALAR

website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-) ' Hello World ' karakter dizisinin baştan ve sondan boşluk karakterlerini siliniz.
result1 = "Hello World".strip()
print(result1)

# 2-) 'www.fatihakbulut.com' karakter dizisinde fatihakbulut dışındaki tüm karakterleri siliniz.
result2 = "www.fatihakbulut.com".strip('w.com')
print(result2)

# 3-) 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result3 = course.lower()
print(result3)

# 4-) 'website ' içinde kaç tane a karakteri vaardır? (count('a'))
result4 = website.count('a')
print(result4)
# 5-) 'website' 'www' ile başlayıp 'com' ile bitiyor mu?
result5 = website.startswith('www')
result6 = website.endswith('com')
print(result5,result6)

# 6-) 'website' içinde '.com '  ifadesi varmı?
result7 = website.find('.com')
print(result7)

# 7-) 'course' içindeki karakterlerin hepsi alfabetik mi?
result8 = course.isalpha()
print(result8)

# 8-) 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result9 = 'Contents'.center(50,'*')
print(result9)

# 9-) 'course' karakter dizisindeki tüm boşluk karakterlerini '- ' ile değiştirin.
result10 = course.replace(' ','-')
print(result10)

# 10-) 'Hello World ' karakter dizisindeki tüm boşluk karakterlerini 'There' ile değiştirin.
result11 = 'Hello World'.replace(' ','There')
print(result11)

# 11-) 'course' karakter dizisini boşluk karakterlerinden ayırın.
result12 = course.split()
print(result12)
