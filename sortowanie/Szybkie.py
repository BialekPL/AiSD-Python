#zadanie 6 - sortowanie szybkie
from random import randint
def quickSort(tab, left, right):
    # First element ( tab[left] ) is a pivot
    if left < right:
        m = left
        for i in range (left+1, right+1):
            if tab[i] < tab[left]:
                m += 1
                tab[m], tab[i] = tab[i], tab[m]
        tab[left], tab [m] = tab[m], tab[left]
        quickSort(tab, left, m-1)
        quickSort(tab, m+1, right)

if __name__ == "__main__":
    # tab = [4, 9, 12, 2, 1, 7, 16, 3]
    tab = [randint(1, 10000) for  i in range(10000)]
    print("Przed sortowaniem:")
    #print(tab)
    quickSort(tab, 0, len(tab)-1)
    #print("Po:")
    print(tab)
