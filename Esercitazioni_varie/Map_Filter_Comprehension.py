# MAP applica una funzione ad ogni elemento --------------------------------------------------------
n = [1, 2, 3, 4, 5]
raddoppia = map(lambda x : x**2, n) # funzione che prende ogni elemento e lo eleva per 2
print(list(raddoppia))              # map() restituisce un iteratore, quindi va convertito
                                    # con list() se si vuole vedere il risultato

# FILTER tiene solo gli elementi per cui la funzione restituisce True (numeri pari) ----------------
pari = filter(lambda x : x % 2 == 0, n)
print(list(pari))

# Combinazione MAP e FILTER - Pipeline -------------------------------------------------------------
eleva_pari = map(lambda x : x**2, filter(lambda x : x % 2 == 0, n))
print(list(eleva_pari))                     # eleva al quadrato solo i pari

# List Comprehension ------------------------------------------------------------------------------------
ris = [x * 10 for x in n if x % 2 == 0]     # moltiplica per 10 solo i pari
print(ris)

# per calcolare i quadrati di una lista di elementi, invece di scrivere:
quadrati = []
for i in range(10):
    quadrati.append(i**2)                       # 10 elementi al quadrato
print(quadrati)
# con la List Comprehension si può scrivere:
quadrati = [i**2 for i in range(15)]            # 15 elementi al quadrato
print(quadrati)

# con condizione, ad esempio per sapere i numeri pari che vi sono da 1 a 20
pari = [x for x in range(21) if x % 2 == 0 and x != 0]
print(pari)

# annidato (nested) per creare Matrice
matrice = [[i*j for j in range(3)] for i in range(3)]
for i in range(3):
    print(matrice[i])

# i primi 1000 numeri divisibili per 3 e per 5 e la loro somma
multipli = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
print("------------------------------")
print(f"I primi 1000 numeri divisibili per 3 e 5 sono: {multipli}")
print("------------------------------")
print(f"La loro somma è: {sum(multipli)}")
print("------------------------------")
