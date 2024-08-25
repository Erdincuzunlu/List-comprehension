### Soru 1: 0’dan 9’a kadar olan sayıları içeren bir liste oluşturun.

list(range(10))

###Liste Comprehension ile Aynı Listeyi Oluşturma

[n for n in range(10)]

##soru 2 :Verilen bir listeyi kullanarak, bu listedeki her öğeyi iki katına çıkaran bir liste oluşturun.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_numbers = [i * 2 for i in numbers]
## for dongüsüyle önce numbersda gezdik bunları i indexinde tuttuk ve 2 ile çarpıp print ile yazdırdık.

print(new_numbers)

##Soru 3 : Verilen bir listeyi kullanarak, bu listedeki her öğenin karesini alan bir liste oluşturun

list(range(10)) #yeni bir liste oluşturduk range fonk. ile 0 dan 9 a kadar
#daha sonra bunların karesi alarak yeni listeyi yazdırdık.

new_list = [a ** 2 for a in list(range(10))]
print(new_list)

##Soru 4 Aşağıdaki listeyi kullanarak, listenin içinde “e” harfi bulunan kelimeleri seçin
# ve büyük harfle yazın. List comprehension kullanarak bu işlemi nasıl yaparsınız?

words = ["apple", "banana", "cherry", "date", "fig", "grape"]

new_words = [i.upper() for i in words if "e" in i]
print(new_words)

##Soru 5: Elinizde bir liste olsun ve bu listedeki tüm negatif sayıların yer aldığı yeni bir liste oluşturun.
##Negatif olmayan sayılar ise listede yer almasın.

numbers = [5, -1, 8, -3, 9, -7, 2]

new_negatif_numbers_list = [a for a in numbers if a < 0]
print(new_negatif_numbers_list)


##soru 6:Verilen iki listeyi kullanarak, iki listedeki öğeleri sırasıyla birleştiren bir liste oluşturun.
## Örneğin, list1 = ["a", "b", "c"] ve list2 = [1, 2, 3] için sonuç [('a', 1), ('b', 2), ('c', 3)] olmalıdır.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

new_list = list(zip(list1,list2))
print(new_list)


##soru 7 :Verilen bir listeyi kullanarak, listedeki yalnızca çift sayıların karesini alan bir liste oluşturun.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers= [i ** 2  for i in numbers if i % 2 == 0]
print(new_numbers)

## soru 8 : Verilen bir liste içinde her öğe bir cümle olarak kabul edilsin.
# Bu cümlelerdeki kelimeleri ters çeviren bir liste oluşturun.

#   1.	Cümleleri kelimelere ayırın.
#	2.	Her kelimeyi ters çevirin.
#	3.	Ters çevrilen kelimeleri tekrar birleştirin.
sentences = ["hello world", "python is fun", "list comprehension"]

new_sentences = ["".join(word[::-1] for word in s.split()) for s in sentences]
print(new_sentences)

##Açıklama

	#•	s.split() cümleyi kelimelere böler.
	#	word[::-1] her kelimeyi ters çevirir.
    #	' '.join(...) ters çevrilen kelimeleri tekrar birleştirir.

# soru 9 : Verilen bir listeyi kullanarak, bu listedeki her öğenin sadece
# tek haneli (yani 0-9 arası) olanlarını seçip bir liste oluşturun.

numbers = [5, 15, 3, 24, 9, 7, 19, 1]

new_list = [number for number in numbers if 0 < number <= 9]
print(new_list)

## Verilen bir liste içerisindeki her bir string’in uzunluğunu hesaplayan
# ve sadece uzunluğu 5’ten büyük olanları içeren yeni bir liste oluşturun.

words = ["apple", "banana", "cherry", "kiwi", "mango", "blueberry"]

long_words = [word for word in words if len(word) > 5]
print(long_words)

## soru 11 : Verilen bir liste içerisindeki her sayının, kendisi ile bölünmesi
# sonucu tam sayı olanları seçerek yeni bir liste oluşturun.
# Yani, sayıların kendisine bölündüğünde kalan sıfır olanları seçin.

numbers = [12, 15, 18, 22, 24, 30]

new_list = [i for i in numbers if i / i == 1]
print(new_list)

# soru 12: Verilen bir listeyi kullanarak, listedeki her öğeyi, string olup olmadığını kontrol edip,
#sadece string olanları içeren yeni bir liste oluşturun.

mixed_list = [1, 'apple', 3.5, 'banana', True, 'cherry', 7]


new_list = [i for i in mixed_list if isinstance(i, str) and i != ""]
print(new_list)

# Beklenen çıktı:
# ['apple', 'banana', 'cherry']

## soru 13 Aşağıdaki listeyi kullanarak, her bir öğenin türünü belirten bir sözlük oluşturun.
# Sözlükte anahtarlar öğelerin kendileri, değerler ise öğelerin türleri olacak.

mixed_list = [1, 'apple', 3.5, 'banana', True, 'cherry', 7]

type_dict = {item: type(item) for item in mixed_list}
print(type_dict)

## açıklama : 	•	{item: type(item) for item in mixed_list} ifadesi, mixed_list içindeki
# her item için item’in türünü belirten bir sözlük oluşturur.
	#type(item) fonksiyonu, her bir öğenin veri tipini döndürür.


# soru 14 Verilen bir liste içinde sadece
# çift sayıları ve 5’ten büyük olanları seçip yeni bir liste oluşturun.
# Listeyi numbers olarak tanımlayın ve sonucunu yazdırın.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = [i for i in numbers if i % 2 == 0 and i > 5 ]
print(new_list)

#soru 15: Verilen bir liste içindeki sayıları kontrol edin. Eğer sayı çift ise o sayıyı iki katına çıkarın,
# tek ise o sayıyı üç katına çıkarın. Sonuçları içeren yeni bir liste oluşturun.

numbers = list(range(15))

new_numbers = [i * 2 if i % 2 == 0 else i * 3 for i in numbers]
print(new_numbers)


## Soru 16 Verilen numbers listesindeki pozitif sayıları ve negatif sayıları ayrı listelere ayırarak iki liste oluşturun.
# Bu işlemi list comprehension kullanarak yapın.

numbers = [10, -1, 4, -8, 0, 15, -3]

pozitif_sayilar = [i for i in numbers if i > 0]
negatif_sayilar = [i for i in numbers if i < 0]

print(pozitif_sayilar)
print( negatif_sayilar)

