# PYTHON'DA LİSTELER


message = "Hello There. My name is Fatih Akbulut".split() #Split() ile listeye çevirdik.

myList1 = [1,2,3]
myList2 = ['bir',2,True,5.6]
print(myList1)
print(myList2)

list1 = ['one','two','theree']
list2 = ['four','five','six']

numbers = list1 + list2          #İki listeyi birleşrme işlemi.
print(numbers)
print(len(numbers))              #Liste uzunluğunun tespit etme.
print(message[0])

userA = ['Fatih',21]
userB = ['Faruk',28]

users = [userA,userB]           #İki listeyi ayrı ayrı dizi içine alma işlemi.
print(users)
print(users[0][1])              #Listenin ilk kümesinin içindeki ikinci elemanı bulma işlemi.




#ALIŞTIRMALAR

# 1-) "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
myList3 = ["Bmw","Mercedes","Opel","Mazda"]
print(myList3)

# 2-) Liste kaç elemanlıdır?
print(len(myList3))

# 3-) Listenin ilk ve son elemanı nedir?
print(myList3[0]) 
print(myList3[-1])

# 4-) Mazda değerini Toyota ile değiştiriniz.
myList3[3] = "Toyota"
print(myList3)

# 5-) Mercedes listenin bir elemanı mıdır?
elemaniMi = 'Mercedes' in myList3
print(elemaniMi)

# 6-) Listenin -2 indeksindeki değer nedir?
print(myList3[-2])

# 7-) Listenin ilk 3 elemanını alın.
myList4 = myList3[:3]
print(myList4)

# 8-) Listenin son iki elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin.
myList3[2:] = "Toyota","Renault"
print(myList3)

# 9-) Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin.
myList5 = myList4 + ["Audi","Nissan"]
print(myList5)

# 10-) Listenin son elemanını silin.
del myList5[-1]
print(myList5)

# 11-) Liste elemanlarını tersten yazdırın.
myList6 = myList5[-1::-1]
print(myList6)

# 12-) Aşağıdaki verileri bir liste içinde sakayınız.
 #studentA = Yiğit  Bilgi 2010, (70,60,70)
 #studentB = Sena   Turan 1999, (80,80,70)
 #studentC = Ahmet  Turan 1998, (80,70,90)

ogrenciA = ['Yiğit','Bilgi',2010,[70,60,70]]
ogrenciB = ['Sena','Turan',1999,[80,80,90]]
ogrenciC = ['Ahmet','Turan',1998,[80,70,90]]

# 13-) Liste elemanlarını ekrana yazdırınız.
ogrenciBilgisi = f"{ogrenciA[0]} {ogrenciA[1]} {2019-ogrenciA[2]} yaşında ve not ortalaması: {(ogrenciA[3][0] + ogrenciA[3][1] + ogrenciA[3][2])/3}"
print(ogrenciBilgisi)