# PYTHON'DA COMPREHENSİONS -- FOR - WHİLE DÖNGÜLERİNE ALTERNATİF


from unittest import result


numbers = []         # Boş bir liste tanımladık.  
for x in range(10):
    numbers.append(x)  # Bu listeye sıfırdan 10'a kadar olan sayıları ekledik. 
print(numbers)

numbers1 = [y for y in range(10)] # Yukarıdaki işlemin daha kısa bir şekilde yapılması.
print(numbers1)

for z in range(10):   # elemanları tek tek yazdırmak için for döngüsünü kullandık.
    print(z**2)
    
numbers2 = [z**2 for z in range(10)] # elemanları bir liste haline getirdik.
print(numbers2)

numbers3 = [t*t for t in range(10) if t % 3 == 0]
print(numbers3)


myString = "Hello"
myList = []

for letter in myString:
    myList.append(letter)
print(myList)


myList = [letter for letter in myString]
print(myList)

years = [1983, 1999, 1956, 1986]

ages = [2022-year for year in years ]
print(ages)

results = [x  if x%2 == 0 else 'tek' for x in range(10)]
print(results)

result = []
for a in range(3):
    for b in range(3):
        result.append((a,b))
        
print(result)

numbers4 = [(x,y) for x in range(3) for y in range(3)]
print(numbers4)