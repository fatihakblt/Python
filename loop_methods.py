 # PYTHON'DA  DÖNGÜ METOTLARI
 
 # RANGE METODU
 

for item in range(10): # 0'dan başlayarak 10 kadar(10 dahil değil) sayıları ekrana yazdırır.
    print(item)

for deger in range(7,20,2):  # 7'den başlayarak 20'ye kadar 2 sayı artırarak bu sayıları ekrana yazdırır.
    print(deger)

print(list(range(7,20,2)))   # 7'den başlayarak 20'ye kadar 2 sayı artırarak bu sayıları bir sayilarye dönüştürür ve yazdırır.

sayilar = list(range(5,17))  # 5'ten başlayıp 17 'ye kadar olan  sayılardan oluşan sayilar adında bir liste oluşturduk.
print(sayilar)


# ENUMERATE METODU

index = 0
greeting = "Hello"

for letter in greeting:
    print(f"index:  {index}   letter: {greeting[index]}")
    index += 1
    
for item1 in enumerate(greeting):  # Karakterlerin indeks numrasını ve hangi karakteri gösterdiğini liste halinde ekrana yazar.
    print(item1)
        

for index1,letter1 in enumerate(greeting):     # 1.değişken indeks numarasını  temsil eder 2.değişken ise indeksi numarasının karşılık geldiği karakteri temsil eder.
    print(f"İndex: {index1} letter: {letter1}")
    


# ZİP METODU

list_a = [1,2,3,4,5]
list_b = ["a","b","c","d","e"]
list_c = [100,200,300,400,500]

print(list(zip(list_a, list_b, list_c)))  # Bu 3 listeyi indeks numaralarına göre birleştirir.

list_d= list(zip(list_a, list_b, list_c))
print(list_d)


for items in zip(list_a, list_b, list_c):
    print(items)

for a,b,c in zip(list_a, list_b, list_c): 
    print(a,b,c)
