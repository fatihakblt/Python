# # PYTHON'DA  TUPLE

# # Tuple: listelerin aynısı fakat üzerinde ekeleme çıkarma gibi değişikliklere izin vermez ve  yay ayrac ile -()- oluşturulur .

# from email.headerregistry import Address
# from operator import index


# list = [1,2,3]
# tuple = (1,'iki',3)
# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

# # Listeye ve Tuple'a tamamen farklı liste elemanı ataması yapılabilir.
# list = ['Ali','Veli']      
# tuple = ('Damla','Ayşe','Ayşe') 

# #list[0] = 'Ahmet'      listelerde tek eleman değiştirilebilir. 
# #tuple[0] = 'Mehmet'    tuplelarda tek eleman değiştirilemez.
# print(list)
# print(tuple)

# # Metot olarak sayma metotları dışındaki metotlar tuplelarda kullanılamaz.
# print(tuple.count('Damla'))
# print(tuple.index('Ayşe'))

# names = tuple + ('fatih','mehmet','Yıldız','Ayşe')
# print(names)



# #PYTHON'DA DICTIONARY


# # Key - Value bilgisi kullanılır yani anahtar ve kilit sistemi gibi...

# # 41 -> Kocaeli   34 -> İstanbul ,vesaire.

# sehirler = ['kocaeli','istanbul']
# plakalar = [41,34]

# print(plakalar[sehirler.index('kocaeli')]) # Liste metodu ile yapım şekli.
# print(plakalar[sehirler.index('istanbul')])


# plakalar = {'İstanbul': 34, 'kocaeli': 41} # Dictionary ile yapım şekli.
# print(plakalar['İstanbul'])
# print(plakalar['kocaeli'])

# plakalar['ankara'] = 6        # Yeni değer atama işlemi.
# print(plakalar['ankara'])

# plakalar['kocaeli'] = 0       # Varolan bir değeri değiştirme işlemi.
# print(plakalar['kocaeli'])


# users = {
#     'fatih akbulut': {
#         'age' : 21,
#         'roles' : ['user'],
#         'email' : 'fatih@gmail.com',
#         'address' : 'Erzurum',
#         'phone' : '123456' 
#     },
#     'mehmet akbulut': {
#         'age' : 17,
#         'roles' : ['admin','user'],
#         'email' : 'mehmet.gmail.com',
#         'address' : 'Erzurum',
#         'phone' : '1234567'
#     }
# }

# print(users['fatih akbulut'])
# print(users['mehmet akbulut']['address'])
# print(users['fatih akbulut']['age'])

# print(users['mehmet akbulut']['roles'][0])


# # ALIŞTIRMALAR


# '''
# ogrenciler = {
#     '120' : {
#         'ad': 'fatih',
#         'soyad' : 'akbulut',
#         'telefon' : '532 000 00 01'
#     },
#     '125' : {
#         'ad' : 'can',
#         'soyad' : 'korkmaz',
#         'telefon' : '532 000 00 02'
#     },
#     '128' : {
#         'ad' : 'volkan',
#         'soyad' : 'yükselen',
#         'telefon' : '532 000 00 03'
#     }

# }
# '''

# # 1-) Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içnde saklayınız.

# ogrenciler = {}
# numara = input("Öğrenci numarasını giriniz: ")
# ad = input("Oğrenci adını giriniz: ")
# soyad = input("Öğrenci soyadını giriniz: ")
# telefon = input("Öğrenci telefon numarasını giriniz: ")

# # ogrenciler[numara] ={
# #     'ad' : ad,
# #     'soyad' : soyad,
# #     'telefon' : telefon 
# # }
# # print(ogrenciler)

# ogrenciler.update({
#     numara:{
#         'ad' :ad,
#         'soyad':soyad,
#         'telefon': telefon
#     }
# })
# ogrenci = ogrenciler[numara]
# print(f"Bilgisi girilen öğrencinin  adı: {ogrenci['ad']}, soyadı: {ogrenci['soyad']}, telefon nosu: {ogrenci['telefon']}")

# tip = {'fatih','kader'}
# print(type(tip))

# PYTHON'DA SETS

fruits = {'orange', 'apple', 'banana'}

print(fruits)      # Setlerin  tüm elemanları yazdırılabir.
#print(fruits[0])    ama setler indekslenemez, yani tek elemanına indeks numarasıyla ulaşılamaz.

for x  in fruits:
    print(x)        # for döngüsü ile de elemanlar yazdırılabilir.

fruits.add('cherry')
print(fruits)
fruits.update(['mango', 'grape', 'apple']) # Bir eleman ikinci kez yazılmaz  ve apple listeye tekrar yazılmaz.
print(fruits)

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList))   # Lİsteyi sete çevirirsek tekrarlanan elemanlar yalnızca bir kere  listelenir.

fruits.remove('mango')
fruits.discard('apple') # Bu iki komut setten eleman silmek için kullanılır.

#fruits.pop() ifadesi kullanılırsa  set içindeki elemanlar belli bir sıralamada olmadığı için rastgele bir öğe silinebilir!.

fruits.clear() # Tüm elemanlar silinir.



# PYTHON'DA VALUE VE REFERENCE VERİ TİPLERİ

# VALUE TYPES => String, Number
 
x = 5
y = 25

x = y
y = 10
print(x,y)

# REFERENCE TYPES => List, class

x = ['apple', 'banana']
y = ['apple', 'banana']

x = y
y[0] = 'grape'
print(x,y)

