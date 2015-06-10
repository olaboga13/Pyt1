__author__ = 'Ania'
# A non-empty zero-indexed array A consisting of N numbers is given.
# The absolute distinct count of this array is the number of distinct
# absolute values among the elements of the array


A=[-10,-5,-8,0,3,-2,8,12] # tablica do obliczen

"""
Dla kazdego elementu tablicy A
jesli wartosc bezwzgl tego elem nie znajduje sie w tablicy pomocniczej array
dodaj te wartosc
wyswietl ilosc elementow tablicy array
"""
def absDistinct(A):
    array=[]
    for i in A:
        if abs(i) not in array:
            array.append(abs(i))
    # print sorted(array)
    return len(array)

y=absDistinct(A)
print y