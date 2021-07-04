#zadanie 4 - algorytm Karpa-Rabina
def kp(text, key, alphabet):
    prime = 19
    text_hash = 0
    key_hash = 0
    m = len(key)

    for i in range(m):
        #making first hashes
        key_hash = (key_hash * len(alphabet) + alphabet[key[i]]) % prime
        text_hash = (text_hash * len(alphabet) + alphabet[text[i]]) % prime
        
    i=0
    while i <= len(text) - len(key):
        if text_hash == key_hash:
            if text[i:i+len(key)] == key:
                return i
        text_hash = ((text_hash - (alphabet[text[i]] * pow(len(alphabet), m-1))) * len(alphabet) + alphabet[text[i+m]] ) % prime
        
        i+=1
    return -1

text = "Ala ma kota"
key = "kot"
alphabet = {}
for y,x in enumerate(text):
    if x not in alphabet.keys() : alphabet[x] = y;
print(kp(text, key, alphabet))



