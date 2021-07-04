#zadanie 6 - sortowanie przez wstawianie
def insertSort(tab):
    for i in range(1, len(tab)):
        if(i%1000 == 0):
            print(f"{i} z {len(tab)}")
        j = i
        karta = tab[j]
        while(j>0 and tab[j-1] > karta):
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = karta

if __name__ == "__main__":
    tab = [4, 9, 12, 2, 1, 7, 16, 3]
    print("Przed sortowaniem:")
    print(tab)
    insertSort(tab)
    print("Po:")
    print(tab)

