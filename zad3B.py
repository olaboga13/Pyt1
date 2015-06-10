__author__ = 'Ania'

# Dla danych napisz kod wypisujacy na konsoli elementy
# list pogrupowane wg dlugosci elementow

list1 = ['orange', 'apple', 'banana']
list2 = ('carrot', 'potato', 'lettuce')
list3 = {'milk', 'sugar', 'butter', 'flour'}

slownik = {}
lista=[]
"""
Stworz jedna liste
"""
lista += list1
lista += list2
lista += list3
"""
Jesli dlugosc aktualnego slowa jest juz w slowniku, dodaj tylko nazwe,
w przeciwnym razie stworz nowy element: dlugosc + nazwa
"""

for i in lista:
    if len(i)in slownik:
        slownik[len(i)]+=(i,)
    else:
        slownik[len(i)] = (i,)

print slownik

