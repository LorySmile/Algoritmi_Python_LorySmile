# definire una Funzione
def saluta():
    print("Ciao")                 # Ciao
saluta()

# con parametri
def somma(a, b):
    return a+b
risultato = somma(3, 5)           # 8
print(risultato)

# con parametri di default
def potenza(base, esponente=2):
    return base ** esponente
print(potenza(5))                # 25
print(potenza(5, 3))             # 125

# controllo Numero Primo
def is_prime(n):
    if n < 2 :
        return False
    for i in range(2, int(n**0.5) + 1):       # un multiplo va da 2 alla sua radice quadra, 
        if n % i == 0 :                       # essendo l'indice che parte da 0, si mette + 1
            return False                      # e si vede poi se n è divisibile per i, allora non è primo
    return True                               # altrimenti uscendo dal ciclo restano i numeri primi

if is_prime(11):
    print("Si, 11 è numero primo!")

# FUNZIONI BUILD-IN o PRODUTTIVE -----------------------------------------------------------------------

# FUNZIONI SUI TIPI ------------------------------------------------------------------------------------

# type() - scoprire il tipo
print(type(5))          # <class 'int'>
print(type("ciao"))     # <class 'str'>
print(type([1,2,3]))    # <class 'list'>

# isinstance() - verificare il tipo
print(isinstance(5, int))           # True
print(isinstance("ciao", str))      # True
print(isinstance([1,2], list))      # True

# Conversioni (casting)
int("42")       # stringa → intero
float("3.14")   # stringa → float
str(123)        # numero → stringa
list("abc")     # ['a', 'b', 'c']
tuple([1,2,3])  # (1, 2, 3)
set([1,2,2,3])  # {1, 2, 3}
dict([("a",1), ("b",2)])  # {'a': 1, 'b': 2}

# FUNZIONI MATEMATICHE BASE ----------------------------------------------------------------------------

# abs() - valore assoluto
print(abs(-5))      # 5
print(abs(-3.7))    # 3.7

# pow() - potenza
print(pow(2, 3))    # 8 (2^3)
print(pow(2, 3, 5)) # 3 (2^3 % 5) - modulo!

# round() - arrotondamento
print(round(3.7))       # 4
print(round(3.14159, 2)) # 3.14 (2 decimali)

# sum() - somma elementi ⭐⭐⭐
print(sum([1, 2, 3, 4, 5]))     # 15
print(sum([1, 2, 3], 10))       # 16 (parte da 10)

# min() e max() ⭐⭐⭐
print(min([3, 1, 4, 1, 5]))     # 1
print(max([3, 1, 4, 1, 5]))     # 5
print(min(3, 1, 4))             # 1 (anche senza lista)

# Con chiave personalizzata
parole = ["python", "è", "fantastico"]
print(min(parole, key=len))     # "è" (più corta)
print(max(parole, key=len))     # "fantastico" (più lunga)

studenti = [("Alice", 28), ("Bob", 30), ("Carol", 25)]
print(max(studenti, key=lambda x: x[1]))  # ('Bob', 30)

# FUNZIONI SU SEQUENZE -------------------------------------------------------------------------------

# len() - lunghezza ⭐⭐⭐
print(len([1, 2, 3]))       # 3
print(len("ciao"))          # 4
print(len({"a": 1, "b": 2})) # 2

# sorted() - ordinare ⭐⭐⭐ in nuova lista
print(sorted([3, 1, 4, 1, 5]))          # [1, 1, 3, 4, 5]
print(sorted([3, 1, 4], reverse=True))  # [4, 3, 1]
print(sorted("python"))                 # ['h', 'n', 'o', 'p', 't', 'y']

# Con chiave
print(sorted(["aa", "b", "ccc"], key=len))  # ['b', 'aa', 'ccc']

# reversed() - rovesciare
print(list(reversed([1, 2, 3])))  # [3, 2, 1]

# enumerate() - indice + elemento ⭐⭐⭐
for i, valore in enumerate(["a", "b", "c"]):
    print(i, valore)  # si può mettere: , start=1 se si vuole iniziare da indice 1
# 0 a
# 1 b
# 2 c

# zip() - accoppiare liste ⭐⭐⭐
nomi = ["Alice", "Bob"]
voti = [28, 30]
for nome, voto in zip(nomi, voti):
    print(nome, voto)
# Alice 28
# Bob 30

# range() - sequenza numeri ⭐⭐⭐
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(2, 8)))        # [2, 3, 4, 5, 6, 7]
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]

# FUNZIONI LOGICHE --------------------------------------------------------------------------------------
# all() - tutti True? ⭐⭐
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False
print(all([1, 2, 3]))            # True (tutti truthy)
print(all([1, 0, 3]))            # False (0 è falsy)

# Esempio: tutti i numeri sono pari?
numeri = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numeri))  # True

# any() - almeno uno True? ⭐⭐
print(any([False, False, True]))  # True
print(any([False, False, False])) # False

# Esempio: c'è almeno un numero pari?
numeri = [1, 3, 5, 8]
print(any(n % 2 == 0 for n in numeri))  # True

# FUNZIONI SU STRINGHE --------------------------------------------------------------------------------

# chr() e ord() - carattere ↔ codice ASCII
print(ord('A'))     # 65
print(chr(65))      # 'A'
print(ord('a'))     # 97
print(chr(122))     # 'z'

# Utile per cifrari!
def cifra_cesare(testo, shift):
    result = ""
    for char in testo:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print(cifra_cesare("ABC", 3))  # "DEF"

# ascii() - rappresentazione ASCII
print(ascii("è"))   # "\\xe8"

# MAP, FILTER, REDUCE ------------------------------------------------------------------------------

# map() - applica funzione a ogni elemento
numeri = [1, 2, 3, 4, 5]
quadrati = list(map(lambda x: x**2, numeri))
print(quadrati)  # [1, 4, 9, 16, 25]

# Esempio: convertire stringhe in interi
stringhe = ["1", "2", "3"]
interi = list(map(int, stringhe))
print(interi)  # [1, 2, 3]

# filter() - filtra elementi
numeri = [1, 2, 3, 4, 5, 6]
pari = list(filter(lambda x: x % 2 == 0, numeri))
print(pari)  # [2, 4, 6]

# reduce() - riduce a un singolo valore (NON built-in, serve import!) ---------------------------------
from functools import reduce
numeri = [1, 2, 3, 4, 5]
somma = reduce(lambda x, y: x + y, numeri)
print(somma)  # 15

prodotto = reduce(lambda x, y: x * y, numeri)
print(prodotto)  # 120 (fattoriale di 5)

