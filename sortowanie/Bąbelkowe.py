#zadanie 6 - sortowanie bąbelkowe
def bubbleSort(tab):
    for i in range(1, len(tab)):
        if(i%1000 == 0):
            print(f"{i} z {len(tab)}")
        for j in range(len(tab)-1, i-1, -1):
            if tab[j] < tab[j-1]:
                tab[j-1], tab[j] = tab[j], tab[j-1]


if __name__ == "__main__":
    tab = [4, 9, 12, 2, 1, 7, 16, 3]
    print("Przed sortowaniem:")
    print(tab)
    bubbleSort(tab)
    print("Po:")
    print(tab)
