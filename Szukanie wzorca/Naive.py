#zadanie 4 - algorytm naiwny
def naive(text, key):
    i = 0;
    j = 0;
    n = len(text)
    m = len(key)
    while(j<m and i<n):
        if text[i] == key[j]:
            i+=1
            j+=1
        else:
            i -= (j-1)
            j = 0
    if j==m:
        print(f"Found key on position {i-m}")
    else:
        print("Key not found")

naive("Ala ma kota", "kot")