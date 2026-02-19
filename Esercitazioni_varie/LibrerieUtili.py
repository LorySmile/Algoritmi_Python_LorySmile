# LIBRERIE -------------------------------------------------------------------------------------
# Math ----------------------------------------------------------
import math

# Costanti
print(math.pi)        # 3.141592653589793
print(math.e)         # 2.718281828459045
print(math.inf)       # infinito
print(math.nan)       # Not a Number

# Potenze e radici
print(math.sqrt(16))      # 4.0 (radice quadrata)
print(math.pow(2, 3))     # 8.0 (2^3)
print(math.exp(2))        # e^2 = 7.389...

# Arrotondamenti
print(math.floor(3.7))    # 3 (arrotonda per difetto)
print(math.ceil(3.2))     # 4 (arrotonda per eccesso)
print(math.trunc(3.7))    # 3 (tronca)

# Valore assoluto
print(math.fabs(-5))      # 5.0

# Logaritmi
print(math.log(10))       # ln(10) = 2.302...
print(math.log10(100))    # log₁₀(100) = 2.0
print(math.log2(8))       # log₂(8) = 3.0

# Trigonometria (radianti!)
print(math.sin(math.pi/2))   # 1.0
print(math.cos(0))           # 1.0
print(math.tan(math.pi/4))   # 1.0

# Conversioni
print(math.degrees(math.pi))  # 180.0 (radianti → gradi)
print(math.radians(180))      # π (gradi → radianti)

# Fattoriale
print(math.factorial(5))   # 120

# GCD (massimo comun divisore)
print(math.gcd(48, 18))    # 6

# Combinatoria (Python 3.8+)
print(math.comb(5, 2))     # C(5,2) = 10 (combinazioni)
print(math.perm(5, 2))     # P(5,2) = 20 (permutazioni)

# Esempi utili per Project Euler -----------------------------
import math

# Verificare se un numero è perfetto quadrato
def is_perfect_square(n):
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n

print(is_perfect_square(16))  # True
print(is_perfect_square(15))  # False

# Somma dei divisori
def sum_divisors(n):
    total = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i and i != 1:
                total += n // i
    return total

# ITERTOOLS - ITERATORI POTENTI --------------------------------------------------------------------
import itertools

# count() - contatore infinito
for i in itertools.count(10, 2):  # parte da 10, step 2
    if i > 20:
        break
    print(i)  # 10, 12, 14, 16, 18, 20

# cycle() - ripete una sequenza all'infinito
counter = 0
for item in itertools.cycle(['A', 'B', 'C']):
    if counter > 5:
        break
    print(item)  # A, B, C, A, B, C
    counter += 1

# repeat() - ripete un valore
for x in itertools.repeat(5, 3):
    print(x)  # 5, 5, 5

# chain() - concatena iterabili
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
for x in itertools.chain(lista1, lista2):
    print(x)  # 1, 2, 3, 4, 5, 6

# combinations() - IMPORTANTISSIMO per Euler!
for combo in itertools.combinations([1, 2, 3, 4], 2):
    print(combo)
# (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)

# permutations() - IMPORTANTISSIMO!
for perm in itertools.permutations([1, 2, 3], 2):
    print(perm)
# (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)

# product() - prodotto cartesiano
for p in itertools.product([1, 2], ['A', 'B']):
    print(p)
# (1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')

# combinations_with_replacement()
for c in itertools.combinations_with_replacement([1, 2], 2):
    print(c)
# (1, 1), (1, 2), (2, 2)

# groupby() - raggruppa elementi consecutivi
dati = [1, 1, 2, 2, 2, 3, 3, 1, 1]
for chiave, gruppo in itertools.groupby(dati):
    print(chiave, list(gruppo))
# 1 [1, 1]
# 2 [2, 2, 2]
# 3 [3, 3]
# 1 [1, 1]

# islice() - slicing di iteratori
for x in itertools.islice(range(100), 5, 10):
    print(x)  # 5, 6, 7, 8, 9

# takewhile() - prende finché la condizione è vera
for x in itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 1]):
    print(x)  # 1, 2, 3, 4

# dropwhile() - salta finché la condizione è vera
for x in itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 1]):
    print(x)  # 5, 6, 1

# Esempio utile a Project Euler ------------------------------------------------
import itertools

# Problema: trova tutti i modi di formare 200 con monete [1,2,5,10,20,50,100,200]
monete = [1, 2, 5, 10, 20, 50, 100, 200]

# Generare tutte le combinazioni di 3 numeri che sommano a 10
for combo in itertools.combinations(range(1, 11), 3):
    if sum(combo) == 10:
        print(combo)

# COLLECTIONS - STRUTTURE DATI SPECIALI ----------------------------------------+++++++++++
from collections import Counter, defaultdict, deque, namedtuple

# Counter - contare elementi (UTILISSIMO!)
testo = "abbcccddddeeeee"
conteggio = Counter(testo)
print(conteggio)  # Counter({'e': 5, 'd': 4, 'c': 3, 'b': 2, 'a': 1})
print(conteggio['e'])  # 5
print(conteggio.most_common(2))  # [('e', 5), ('d', 4)]

# esempio
from collections import Counter
testo = "aabbcc"
c = Counter(testo)
print(c)  # Counter({'a': 2, 'b': 2, 'c': 2})

# Esempio pratico
numeri = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq = Counter(numeri)
print(freq[3])  # 3
print(freq.most_common(1))  # [(4, 4)] - elemento più frequente

# esempio
c.most_common(1)  # restituisce i primi 1 elementi più comuni

# defaultdict - dizionario con valori di default
d = defaultdict(int)  # default = 0
d['a'] += 1
d['b'] += 2
print(d)  # {'a': 1, 'b': 2}

# Utile per raggruppare
raggruppati = defaultdict(list)
for nome, voto in [("Alice", 28), ("Bob", 30), ("Alice", 27)]:
    raggruppati[nome].append(voto)
print(raggruppati)  # {'Alice': [28, 27], 'Bob': [30]}

# deque - coda doppia (double-ended queue)
coda = deque([1, 2, 3])
coda.append(4)        # aggiungi a destra
coda.appendleft(0)    # aggiungi a sinistra
print(coda)           # deque([0, 1, 2, 3, 4])
coda.pop()            # rimuovi da destra → 4
coda.popleft()        # rimuovi da sinistra → 0
print(coda)           # deque([1, 2, 3])

# rotate
coda.rotate(1)        # ruota a destra
print(coda)           # deque([3, 1, 2])
coda.rotate(-1)       # ruota a sinistra
print(coda)           # deque([1, 2, 3])

# namedtuple - tuple con nomi (come struct)
Punto = namedtuple('Punto', ['x', 'y'])
p = Punto(10, 20)
print(p.x, p.y)       # 10 20
print(p[0], p[1])     # 10 20 (funziona anche come tupla normale)

Studente = namedtuple('Studente', ['nome', 'voto'])
s = Studente('Lorenza', 30)
print(s.nome)         # Lorenza

# chainmap - unire più dizionari
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print(chain['a'])  # 1 (da dict1)
print(chain['b'])  # 2 (da dict1, ha precedenza)
print(chain['c'])  # 4 (da dict2)

# Esempio in Project Euler -------------------------------------------
# Problema: trovare la cifra più frequente in 2^1000
from collections import Counter
numero = 2 ** 1000
cifre = Counter(str(numero))
print(cifre.most_common(1))  # cifra più frequente

# RIASSUNTO ---------------------------------------------------------------------------------------

# Math - per calcoli matematici
import math
print(math.sqrt(16), math.factorial(5), math.gcd(12, 8))

# Itertools - per combinazioni, permutazioni, iteratori
import itertools
list(itertools.combinations([1,2,3], 2))  # [(1,2), (1,3), (2,3)]

# Collections - per contare, dizionari speciali, code
from collections import Counter, defaultdict, deque
Counter("aabbcc").most_common(1)  # [('a', 2)] o [('b', 2)]...

# --------------------------------------------------------------------------------------------------

# HEAPQ - Code con priorità ------------------------------------------------------------------------
import heapq

# Creare un heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 9)
print(heap)  # [1, 5, 3, 9] - NON è ordinato, ma il minimo è sempre in heap[0]

# Estrarre il minimo
minimo = heapq.heappop(heap)
print(minimo)  # 1
print(heap)    # [3, 5, 9]

# Trasformare una lista in heap
lista = [5, 7, 9, 1, 3]
heapq.heapify(lista)
print(lista)  # [1, 3, 9, 7, 5] - ora è un heap

# I 3 elementi più piccoli
numeri = [5, 1, 9, 3, 7, 2, 8]
print(heapq.nsmallest(3, numeri))  # [1, 2, 3]

# I 3 elementi più grandi
print(heapq.nlargest(3, numeri))   # [9, 8, 7]

# ARRAY tipizzati ----------------------------------------------------------------------------------
import array

# Creare array di interi
arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' = signed int
print(arr)  # array('i', [1, 2, 3, 4, 5])

# Codici tipo:
# 'b' = signed char (1 byte)
# 'i' = signed int (2 bytes)
# 'l' = signed long (4 bytes)
# 'f' = float
# 'd' = double

arr.append(6)
print(arr[0])  # 1

# Più efficiente di lista per numeri, ma meno flessibile

#   QUEUE - Code Thread-safe --------------------------------------------------------------------------
from queue import Queue, LifoQueue, PriorityQueue

# FIFO Queue (First In First Out)
q = Queue()
q.put(1)
q.put(2)
q.put(3)
print(q.get())  # 1 (primo inserito)
print(q.get())  # 2

# LIFO Queue (Last In First Out) - come uno Stack
stack = LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)
print(stack.get())  # 3 (ultimo inserito)
print(stack.get())  # 2

# Priority Queue (elemento con priorità minore esce per primo)
pq = PriorityQueue()
pq.put((2, "task2"))  # (priorità, valore)
pq.put((1, "task1"))
pq.put((3, "task3"))
print(pq.get())  # (1, 'task1')
print(pq.get())  # (2, 'task2')

# BISECT - Ricerca Binaria ----------------------------------------------------------------------------
import bisect

# Lista ordinata
numeri = [1, 3, 5, 7, 9]

# Trovare posizione dove inserire mantenendo ordine
pos = bisect.bisect_left(numeri, 6)
print(pos)  # 3 (tra 5 e 7)

# Inserire mantenendo ordine
bisect.insort(numeri, 6)
print(numeri)  # [1, 3, 5, 6, 7, 9]

# bisect_left vs bisect_right (con duplicati)
numeri = [1, 2, 2, 2, 3]
print(bisect.bisect_left(numeri, 2))   # 1 (prima del 2)
print(bisect.bisect_right(numeri, 2))  # 4 (dopo l'ultimo 2)

# ENUM - Enumerazioni ----------------------------------------------------------------------------------
from enum import Enum

class Colore(Enum):
    ROSSO = 1
    VERDE = 2
    BLU = 3

print(Colore.ROSSO)        # Colore.ROSSO
print(Colore.ROSSO.value)  # 1
print(Colore.ROSSO.name)   # 'ROSSO'

# Iterare
for colore in Colore:
    print(colore)

# DATACLASSES ----------------------------------------------------------------------------------------
from dataclasses import dataclass

@dataclass
class Studente:
    nome: str
    età: int
    voto: float = 0.0  # valore di default

s = Studente("Lorenza", 21, 30)
print(s)  # Studente(nome='Lorenza', età=21, voto=30)
print(s.nome)  # Lorenza

# Confronti automatici
s2 = Studente("Marco", 22, 28)
print(s == s2)  # False

# TYPING - Type Hints ---------------------------------------------------------------------------
from typing import List, Dict, Tuple, Optional, Union

def somma_lista(numeri: List[int]) -> int:
    return sum(numeri)

def trova_studente(nome: str) -> Optional[Dict[str, int]]:
    # Optional = può restituire None
    if nome in database:
        return {"età": 21, "voto": 30}
    return None

def processa(valore: Union[int, str]) -> str:
    # Union = può essere int O str
    return str(valore)


## **RIEPILOGO: QUANDO USARE COSA?**
"""
┌─────────────────────┬──────────────────────────────────┐
│   STRUTTURA         │   QUANDO USARLA                  │
├─────────────────────┼──────────────────────────────────┤
│ list                │ Collezione generale mutabile     │
│ tuple               │ Dati immutabili, coordinate      │
│ set                 │ Elementi unici, operazioni O(1)  │
│ dict                │ Mappature chiave-valore          │
│ deque               │ Code, stack, inserimenti veloci  │
│ Counter             │ Contare frequenze                │
│ defaultdict         │ Dict con valori di default       │
│ heapq               │ Min/max heap, priorità           │
│ namedtuple          │ Tuple con nomi (struct-like)     │
│ array               │ Array numerici compatti          │
│ Queue               │ Code thread-safe                 │
│ bisect              │ Ricerca binaria su liste         │
└─────────────────────┴──────────────────────────────────┘
"""