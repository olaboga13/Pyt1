__author__ = 'Ania'
# Dla danych napisz kod wypisujacy na konsoli wszytskie
# elementy zawierajace dwie identyczne litery obok siebie

list1 = ['berry','orange', 'apple', 'banana']
list2 = ('carrot', 'potato', 'lettuce')
list3 = {'milk', 'sugar', 'butter', 'flour'}
lista = []
"""
Stworz jedna liste
"""
lista += list1
lista += list2
lista += list3

print lista

"""
Dla kazdego elementu listy (slowa)
rozdziel stringa na tablice char'ow
dla kazdej litery w slowie poszukaj, czy obok niej znajduje sie jej duplikat
jesli tak, wyswietl cale slowo
"""
for slowo in lista:
    litera=list(slowo)
    for i in range(len(litera)-1):
        if litera[i] == litera[i+1]:
            print slowo.capitalize()
