# Funzione normale (return)
def numeri_return(n):
    result = []
    for i in range(n):
        result.append(i)
    return result         # restituisce TUTTA la lista

lista = numeri_return(5)  # [0, 1, 2, 3, 4] ← tutto in memoria

# Generatore (yield)
def numeri_yield(n):
    for i in range(n):
        yield i           # restituisce UN valore alla volta

gen = numeri_yield(5)     # <generator object>
for num in gen:
    print(num)            # 0, 1, 2, 3, 4 ← un valore alla volta

# Generatore di numeri primi (infinito!)
def primi_infiniti():
    n = 2
    while True:  # INFINITO!
        if is_prime(n):
            yield n
        n += 1

# Prendi solo i primi 5
gen = primi_infiniti()
for _ in range(5):
    print(next(gen))  # 2, 3, 5, 7, 11

# Funzione is_prime necessaria
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generator Expression (come List Comprehension ma con parentesi tonde)
# List comprehension (crea TUTTA la lista)
quadrati_lista = [x**2 for x in range(1000000)]  # consuma troppa memoria!

# Generator expression (lazy, uno alla volta)
quadrati_gen = (x**2 for x in range(1000000))    # è efficiente!

# Esempio pratico
somma = sum(x**2 for x in range(1000))  # calcola la somma senza creare lista
print(somma)

# next() e StopIteration -----
def conta_tre():
    yield 1
    yield 2
    yield 3

gen = conta_tre()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # StopIteration! (finito)

# Generatore di numeri pari
def pari(limit):
    n = 0
    while n < limit:
        yield n
        n += 2

# Multipli di 3 o 5 sotto 1000 (Problema 1 Euler)
def multipli_3_5(limit):
    for n in range(limit):
        if n % 3 == 0 or n % 5 == 0:
            yield n

somma = sum(multipli_3_5(1000))  # efficiente!
print(somma)  # 233168

# Generatore di fattori
def fattori(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

print(list(fattori(12)))  # [1, 2, 3, 4, 6, 12]


## ** VANTAGGI DEI GENERATORI **
"""
┌──────────────────┬─────────────────┬─────────────────┐
│                  │     LISTA       │   GENERATORE    │
├──────────────────┼─────────────────┼─────────────────┤
│ Memoria          │ Tutto in RAM    │ Uno alla volta  │
│ Velocità inizio  │ Lenta (calcola  │ Immediata       │
│                  │ tutto subito)   │                 │
│ Riutilizzabile   │ Sì              │ No (esauribile) │
|                  |                 |                 |
│ Indicizzabile    │ Sì lista[5]     │ No              │
│ Uso              │ Dati piccoli    │ Dati grandi o   │
│                  │                 │ infiniti        │
└──────────────────┴─────────────────┴─────────────────┘
"""