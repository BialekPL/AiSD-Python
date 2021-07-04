from random import random, sample
def roznicowy(f, generacja):
    k = 0.5
    p = 0.3
    nowa_generacja = []

    for rodzic in generacja:
        pozostali = generacja[:]
        pozostali.remove(rodzic)
        # Wylosowanie 3 spośród pozostałcyh osobników do stworzenia wektora mutacji
        wybrani = sample(pozostali, 3) 
        # Stworzenie wektora mutacji u
        u = mutacja(wybrani, k)
        # Krzyżowanie
        potomek = krzyzuj(rodzic, u, p)
        # Prawo silniejszego. Osobnik z wyższą wartością przechodzi do następnej generacji
        if f(potomek) < f(rodzic): 
            nowa_generacja.append(potomek)
        else:
            nowa_generacja.append(rodzic)

    return nowa_generacja


def mutacja(wybrani, k):
    wektor_mutacji = []
    for i in range(len(wybrani)):
        wsp = wybrani[0][i] + k * (wybrani[1][i] - wybrani[2][i])
        wektor_mutacji.append(wsp)
    return wektor_mutacji

def krzyzuj(rodzic, u, p):
    potomek = []
    for i in range(len(rodzic)):
        r = random()
        if r <= p: potomek.append(u[i])
        else: potomek.append(rodzic[i])
    return potomek

def testuj(f, generacja, liczba_generacji):
    for i in range(liczba_generacji):
        generacja = roznicowy(f, generacja)

    najlepszy = generacja[0]
    for osobnik in generacja:
        if f(osobnik) < f(najlepszy):
            najlepszy = osobnik
    print("Najlepszy osobnik z ostatniej generacji:")
    for i, x in enumerate(najlepszy):
        print(f"x{i+1}: {x}  ", end='')
    print()

def sphere(wsp):
    return sum([x**2 for x in wsp])

def sum_squares(wsp):
    wynik = 0
    for index, x in enumerate(wsp):
        wynik += (index+1) * (x**2)
    return wynik

generacja = [[-0.25, -0.95, 0.82], [3.69, 0.94, -3.16],[-2.26, 4.93, -1.13],[3.92, -4.29, 1.75],[3.92, -4.29, 1.75]]
liczba_epok = 50
print(f"Test na funkcji 'sum_squares' (liczba epok: {liczba_epok}): ")
testuj(sum_squares, generacja, liczba_epok)
print(f"Test na funkcji 'sphere' (liczba epok: {liczba_epok}): ")
testuj(sphere, generacja, liczba_epok)
