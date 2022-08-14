# PYTHON'DA KARAKTER DİZiLERİ - STRİNGS


name = 'Fatih'
surname = 'Akbulut'
age = 21

greeting1 = "My name is "+ name + " "+ surname + " and \nI am "+ str(age) + "years old."  #1. gösterim şekli.
print(greeting1)

greeting2 = "My name is {} {} and \nI am {} years old.".format(name,surname,age)          #2. gösterim şekli.
print(greeting2)

greeting3 = f"My name is {name} {surname} and \nI am {age} years old."                    #3. gösterim şekli.
print(greeting3)

print(len(greeting1))                                                                     #Karakter dizisinin uzunluğunu yazdırır.

print(greeting2[0])                                                                       #Karakter dizisinin ilk elemanı -karakterini- yazdırır. 

print(greeting3[0:3])                                                                     #Karakter dizisinin 0'dan 3.elemanına (dahil değil) kadar yazdırır.


#ALIŞTIRMALAR

website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1-) 'course' karakter dizisinde kaç karakter bulunmaktadır.
result1 = len(course)
print(result1)

# 2-) 'website' içinden www karakterlerini alın.
result2 = website[7:10]
print(result2)

# 3-) 'website' içinden com karakterlerini alın. 
print(website.index('c')) #Kaçıncı index ile başladığını bulduk.
result3 = website[22:25]
print(result3)

# 4-) 'course' içinden ilk 15 ve son 15 karakterleri alın
result4 = course[:15]
result5 = course[50:65]
print(result4)
print(result5)

# 5-) 'course'  içindeki karakterleri tersten yazdırın.
result6 = course[-1::-1]
print(result6)


# 6-) Aşağıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Fatih Akbulut, Yaşım 21 ve mesleğim mühendis. '

name1,surname1,age1,job1 = "Fatih","Akbulut",21,"Mühendis"
result7 = f"Benim adım {name1} {surname1}, Yaşım {age1} ve mesleğim {job1}"
print(result7)

# 7-)'Hello world' ifadesindeki 'w' harfini 'W harfi ile değiştirin.'
result8 = "Hello world"
result8 = result8[0:6] + 'W' + result8[-4:]
print(result8)

# 8-) 'abc ifadesiniyan yana 3 defa yazdırın.'
result9 = "abc"*3
print(result9)
