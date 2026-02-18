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

# Comprehension ------------------------------------------------------------------------------------
ris = [x * 10 for x in n if x % 2 == 0]     # moltiplica per 10 solo i pari
print(ris)