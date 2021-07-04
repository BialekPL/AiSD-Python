#zadanie 5 - kodowanie Huffmana
kod = {"A":"", "B":"", "C":"", "D":"", "E":"", "F":""}
# Tworzę listę krotek, w każdej znajdują się litery i odpowiadające im prawdopodobieństwo,
# Prawdopodobieństwa sumują się do 100. Zrobiłem tak zamiast sumowania do 1, ponieważ
# komputery mają problem z działaniami na ułamkach
symbole = [(30, "A"), (10, "B"), (20, "C"), (10, "D"), (20, "E"), (10, "F")]
symbole = sorted(symbole, reverse=True)
# Tworzenie kodu
while len(symbole) > 1:
    # Pobieram dwa symbole o najmniejszych prawdopodobieństwach, 
    # Prawdopodobieństwo s1 jest mniejsze lub równe prawdopodobieństwu s2
    s1 = symbole.pop()
    s2 = symbole.pop()
    # Dla każdej litery znajdującej się w symbolu, dodaję Z LEWEJ STRONY jej kodu
    # 0 lub 1, w zależności która została kiedy pobrana
    for litera in s1[1]:
        kod[litera] = "0" + kod[litera]
    for litera in s2[1]:
        kod[litera] = "1" + kod[litera]
    # Tworzę nowy symbol będący sumą liter i prawdopodobieństw pobranych symboli,
    # np. (B, 10), (D, 10) daje (BD, 20) 
    s1s2 = (s1[0]+s2[0], s1[1]+s2[1])
    symbole.append(s1s2)
    symbole = sorted(symbole, reverse=True)
    
print(kod)
tekst = "BACA"
print("Tekst: ", tekst)
print("Zakodowany tekst: ", end="")
for litera in tekst:
    print(kod[litera], end="")
