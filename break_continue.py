# PYTHON'DA BREAK VE CONTİNUE KOMUTLARI

name = "fatih akbulut"

for letter in name:
    if letter == 'a':   # letter eğer 'a' karakterine eşit olursa break döngüyü bulunduğu yerde durdurur.
        break
    print(letter)


for letter2 in name:
    if letter2 == 't': # letter2 eğer 't' karakterine eşit olursa  continue 't'karakterini atlayarak döngüyü devam ettirir.
        continue
    print(letter2)

x = 0

while x < 5:
      x += 1
      if x == 2:
        break
      print(x)

y = 0

while y < 5:
    y += 1    # Eğer y'yi artırma işlemini continue'nin alt satırına yazarsak y, 3 sayısında sonsuz döngüye girer.
    if y == 3:
        continue
    print(y)

# ALIŞTIRMA 

# 1-) 1-100' e kadar tek sayıların toplamı.

k = 0
toplam = 0
while k <= 100:
    k += 1
    if (k % 2 == 0):
        continue
    toplam += k
print(toplam)


  
