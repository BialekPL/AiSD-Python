kod = {"A": "", "B": "", "C": "", "D": "", "E": "", }
symbole = [(30, "A"), (10, "B"), (10, "C"), (20, "D"), (30, "E")]
def shannon_fano(symbole):
    if len(symbole) > 1:
        symbole = sorted(symbole, reverse=True)
        lewo = []
        suma_lewo = 0
        prawo = symbole
        suma_prawo = 0
        for symbol in prawo:
            suma_prawo += symbol[0]
        i=0
        while i < len(symbole):
            # Przerzucaj elementy z prawej tablicy do lewej do momentu, aż różnica częstości będzie najmniejsza
            if abs((suma_lewo+prawo[0][0]) - (suma_prawo-prawo[0][0])) < abs(suma_lewo - suma_prawo):
                s = prawo.pop(0)
                lewo.append(s)
                suma_lewo += s[0]
                suma_prawo -= s[0]
                i+=1
            else: break
        # Do kodu każdej litery, znajdującej się w lewej gałęzi dopisz 0, do tych w prawej 1; 
        for symbol in lewo:
            kod[symbol[1]] += "0"
        for symbol in prawo:
            kod[symbol[1]] += "1"
        shannon_fano(lewo)
        shannon_fano(prawo)
        
shannon_fano(symbole)
print("Wyznaczony kod: ", kod)
tekst = "BACA"
print(f"Tekst: {tekst}\nZakodowany tekst: ", end="")
for litera in tekst:
    print(kod[litera], end="")