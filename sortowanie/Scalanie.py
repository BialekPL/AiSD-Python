#zadanie 6 - sortowanie przez scalanie
from random import randint

def mergeSort(tab):
    if len(tab) > 1:
        mid = len(tab)//2
        L = tab[:mid]
        R = tab[mid:]
        mergeSort(L)
        mergeSort(R)
        merge(tab, L, R)

def merge(tab, L, R): 
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            tab[k] = L[i]
            i += 1
        else:
            tab[k] = R[j]
            j += 1
        k += 1
 
        # At this point we ran out of one of the tables, so we add the rest from the other one
    while i < len(L):
        tab[k] = L[i]
        i += 1
        k += 1
 
    while j < len(R):
        tab[k] = R[j]
        j += 1
        k += 1
 
if __name__ == "__main__":
    tab = [4, 9, 12, 2, 1, 7, 16, 3]
    print("Przed sortowaniem:")
    print(tab)
    mergeSort(tab)
    print("Po:")
    print(tab)