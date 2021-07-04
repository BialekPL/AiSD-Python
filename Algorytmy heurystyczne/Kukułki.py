from random import random, normalvariate, uniform
from math import cos, sqrt, exp, pi
def kukulki(f, jaja):
    delta = gamma = 1
    pa = 0.6
    mi = 0.5
    minimum = -10
    maksimum = 10
    moze_wypasc = 2
    nastepne_jaja = lot_wirtualny(jaja, gamma, delta, mi, f)
    nastepne_jaja = wykrycie_jaj(nastepne_jaja, pa, moze_wypasc, minimum, maksimum)
    nastepne_jaja = sorted(nastepne_jaja, key=f, reverse=True)
    return nastepne_jaja

def lot_wirtualny(jaja, gamma, delta, mi, f):
    nastepne_jaja = []
    jaja_temp = []
    for jajko in jaja:
        beta = abs(normalvariate(gamma/len(jaja), 1))
        L = lot_levy(beta, gamma, delta)
        jaja_temp.append([x+mi*L for x in jajko])
    for jajo, jajo_temp in zip(jaja, jaja_temp):
        if f(jajo) < f(jajo_temp): nastepne_jaja.append(jajo)
        else: nastepne_jaja.append(jajo_temp)
    nastepne_jaja = sorted(nastepne_jaja, key=f)
    return nastepne_jaja

def lot_levy(beta, gamma, delta):
    if beta > delta:
        mnoznik = sqrt(gamma/(2*pi))
        licznik = exp((-1*delta)/(2*(beta-delta)))
        mianownik = pow((beta - delta),3/2)
        wynik = mnoznik * licznik / mianownik
    else: 
        wynik = 0
    return wynik

def wykrycie_jaj(jaja, pa, moze_wypasc, minimum, maksimum):
    # Przeprowadzanie losowania dla 2 najgorszych jaj (oryginalnie moze_wypasc = 2)
    for jajo in jaja[-moze_wypasc:]:
        r = random()
        # wyrzuć jajko z prawdopoodbienstwem pa, w jego miejsce umieść losowe współrzędne nowego gniazda.
        if r <= pa:
            nowe_jajo = []
            for _ in jajo:
                nowe_jajo.append(uniform(minimum, maksimum))
            jaja.remove(jajo)
            jaja.append(nowe_jajo)
    return jaja

def testuj(f, generacja, liczba_testow):
    for i in range(liczba_testow):
        generacja = kukulki(f, generacja)
    print("Najlepszy: ", generacja[0])

def sum_squares(wsp):
    wynik = 0
    for index, x in enumerate(wsp):
        wynik += (index+1) * (x**2)
    return wynik

sphere = lambda wsp: sum([x**2 for x in wsp])

jaja = [[-3, 2], [-2, 1], [-3, 0], [2, -3], [1, 1]]
testuj(sum_squares, jaja, 20)
testuj(sphere, jaja, 20)

