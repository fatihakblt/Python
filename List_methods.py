# PYTHON'DA BAZI LİSTE METOTLARI



numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

# 1-) Min() metodu: sayılar listesinde en küçük sayıyı verir.
#     ''         '' karakter listesinde alfabetik sıra olarak en küçük harfi verir.
result1 = min(numbers)
result2 = min(letters)
print(result1)
print(result2)

# 2-) Max() metodu: sayılar listesinde en büyük sayıyı verir.
#     ''         '' karakter listesinde alfabetik sıra olarak en büyük harfi verir.
result3 = max(numbers)
result4 = max(letters)
print(result3)
print(result4)

# 3-) Append() metodu: içinde verilen değeri listenin sonuna ekler.
numbers.append(35)
print(numbers)
numbers.append('fatih')
print(numbers)

# 4-) Insert(x,y) metodu:  ilk parametrede verilen eklenecek öğenin indeks numarasına göre ikinci parametreyi listeye ekler.
numbers.insert(4,90)
print(numbers)

# 5-) Pop() metodu: parametre alırsa aldığı parametrenin indeks numarasındaki elemanı siler.
#      ''        ''parametre almazsa listenin son elemanını siler.
numbers.pop()
print(numbers)
numbers.pop(4)
print(numbers)

# 6-) Remove() metodu: bu metot içine girilen değeri listeden siler.
numbers.remove(10)
print(numbers) 

# 7-) Sort metodu: Bu metot sayıları ve karakterleri küçükten büyüğe sıralar (karakterleri alfabetik sıraya göre).
numbers.sort()
print(numbers)
letters.sort()
print(letters)

# 8-) Reverse() metodu: Bu metot  listenin sıralamasını tam tersine çevirir.
numbers.reverse()
print(numbers)

# 9-) Count() metodu: Bu metot verilen değerlerin liste içindeki sayısını belirler.
print(numbers.count(5))

# 10-) Clear() metodu : Bu metot listenin elemalarını temizler.
numbers.clear()
print(numbers)



#ALIŞTIRMALAR


names = ['Ali','Yağmur','Hakan','Deniz']
years = [1999, 2000, 1998, 1987]

# 1-) "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)

# 2-) "Sena" ismini listenin başına ekleyiniz.
names.insert(0,"Sena")
print(names)

# 3-) "Deniz" ismini listeden siliniz.
names.remove("Deniz")
print(names)

# 4-) "Yağmur" isminin indeksi nedir?
print(names.index("Yağmur"))

# 5-) "Ali" listenin bir elemanı mıdır?
print("Ali" in names)

# 6-) Liste elemanlarını ters çevirin.
names.reverse()
print(names)

# 7-) Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 8-) 'years' listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)

# 9-) str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia".split()
print(str)

# 10-) 'years' dizisinin en büyük ve en küçük elemanı nedir?
print(max(years))
print(min(years))

# 11-) 'years' dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))

# 12-) 'years' dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

# 13-) Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
x = input("Lutfen marka giriniz:")
y = input("Lutfen marka giriniz:")
z = input("Lutfen marka giriniz:")
arabalar = [x,y,z]
print(arabalar)