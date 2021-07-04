from random import random
def genetyczny(f, generacja):
    pm = 0.1
    wartosci = []
    for i in range(len(generacja)):
        wartosci.append(f(generacja[i]))
    nowa_generacja = []

    # Dzielenie przedziału 0---1 na podprzedziały by potem zakręcić ruletką
    przedziały = [0]
    suma = sum(wartosci)
    for i in range(len(generacja)-1):
        kraniec = wartosci[i]/suma + przedziały[i]
        przedziały.append(kraniec)
    przedziały.remove(0)
    przedziały.append(1)

    while len(nowa_generacja) < len(generacja):
        # Wybranie dwóch osobników z generacji metodą ruletki
        rodzic1 = generacja[ruletka(przedziały)]
        rodzic2 = generacja[ruletka(przedziały)]
        # Mutacja osobników
        rodzic1 = mutuj(rodzic1[:], pm)
        rodzic2 = mutuj(rodzic2[:], pm)
        # Krzyżowanie
        potomek1 = krzyzuj(rodzic1, rodzic2)
        potomek2 = krzyzuj(rodzic2, rodzic1)
        # Prawo silniejszego. Osobnik z wyższą wartością przechodzi do następnej generacji
        if f(potomek1) > f(rodzic1): 
            nowa_generacja.append(potomek1)
        else:
            nowa_generacja.append(rodzic1)
        # Zabezpieczenie w razie nieparzystej liczby osobników w początkowej generacji
        if len(nowa_generacja) < len(generacja):
            if f(potomek2) > f(rodzic2): 
                nowa_generacja.append(potomek2)
            else:
                nowa_generacja.append(rodzic2)
    print(nowa_generacja)
    return nowa_generacja



def ruletka(przedziały):
    liczba = random()
    zwycięzca = 0
    for i in range(len(przedziały)):
        if liczba < przedziały[i]:
            zwycięzca = i
            break
    return zwycięzca

def mutuj(osobnik, pm):
    for i in range(len(osobnik)):
        losowa = random()
        if losowa <= pm:
            osobnik[i] += random()-0.5
    return osobnik

def krzyzuj(osobnik1, osobnik2):
    eta = random()
    potomek = []
    for i in range(len(osobnik1)):
        potomek.append(osobnik1[i] + eta*(osobnik2[i]-osobnik1[i]))
    return potomek

def testuj(f, generacja, liczba_generacji):
    for i in range(liczba_generacji):
        generacja = genetyczny(f, generacja)

    najlepszy = generacja[0]
    for osobnik in generacja:
        if f(osobnik) > f(najlepszy):
            najlepszy = osobnik
    print("\nNajlepszy osobnik z ostatniej generacji:")
    for i, x in enumerate(najlepszy):
        print(f"x{i+1}: {x}  ", end='')

def sphere(wsp):
    return 75 - sum([x**2 for x in wsp])

def sum_squares(wsp):
    wynik = 0
    for index, x in enumerate(wsp):
        wynik += (index+1) * (x**2)
    return 75 - wynik

generacja = [[-0.25, -0.95, 0.82], [3.69, 0.94, -3.16], [-2.26, 4.93, -1.13], [3.92, -4.29, 1.75], [3.92, -4.29, 1.75]]
testuj(sum_squares, generacja, 2)
testuj(sphere, generacja, 2)


