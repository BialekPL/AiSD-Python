#zadanie 4 - algorytm Boyera - Moore'a
def bm(text, key):
    m = len(key)
    i = m-1
    j = m-1
    while i < len(text):
        while text[i] == key[j]:
            i-=1
            j-=1
        if j == -1:
            return i+1
        else:
            i += m - min(j, 1+in_p(text[i]))
            j = m-1
    return -1

def in_p(letter):
    for l in p.keys():
        if l == letter:
            return p[letter]
    return -1

text = "Ala ma kota"
key = "kot"
# "pomocnicza tablica przesunięć"
p = {letter:index for index, letter in enumerate(key)}
# printing on what position there's first appearance of a key
# -1 means that key wasn't found
print(bm(text, key))


