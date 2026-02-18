# Liste: ----------------------------------------------------------------------------------------------------
numerica = [1, 2, 3, 4, 5]
nomi = ["Lorenza", "Ludovica", "Paolo", "Fabrizio"]
mista = ["Luna", 3.14, False, 5]
vuota = []

# Indicizzazione e slicing:
lista = [20, 40, 60, 80, 100]
#         0   1   2   3   4      indici
#        -5  -4  -3  -2  -1      inversi (ultimo, penultimo, ecc...)

print(lista[0])        # primo elemento
print(lista[-1])       # ultimo elemento
print(lista[1:3])      # da indice 1 a indice 3 escluso
print(lista[2:])       # da indice 2 fino alla fine
print(lista[:3])       # dall'inizio fino a indice 3 esluso
print(lista[::-1])     # lista al contrario

# Le liste sono mutabili, si possono modificare gli elementi:
lista_corta = [10, 35, 98, 172, 234]
lista_corta[0] = 5
print(lista_corta)                # 5, 35, 98, 172, 234

lista_corta[1:5] = [2, 3, 5, 8]
print(lista_corta)                # 5, 2, 3, 5, 8

# Operazioni sulle liste:
lista1 = [5, 15, 20, 25, 30, 35]

lista1.append(40)       # aggiunge alla fine della lista  [5, 15, 20, 25, 30, 35, 40]
lista1.insert(1, 10)    # inserisce in posizione 1        [5, 10, 15, 20, 25, 30, 35, 40]
lista1.extend([45, 50]) # aggiunge più elementi alla fine [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(lista1)

lista1.remove(20)       # rimuove la prima occorrenza di 20
print(lista1)

x = lista1.pop()        # rimuove l'ultimo elemento della lista
print(lista1)

x = lista1.pop(0)       # rimuove il primo elemento della lista
print(lista1)

del lista1[2]           # elimina l'elemento in posizione/indice 2
print(lista1)

print(lista1.index(40)) # restituisce l'indice della prima occorrenza di 40
print(lista1.count(45)) # restituisce quante volte compare 45 nella lista

lista1.sort()                 # ordina in place, cioè modifica la lista originale
print(lista1)

lista1.sort(reverse = True)     # ordinamento decrescente
print(lista1)

nuova_lista = sorted(lista1)  # restituisce una nuova lista ordinata e l'originale resta intatta
lista_capovolta = sorted(lista1, reverse = True)
print(nuova_lista)
print(lista_capovolta)

lista1.reverse()              # rovescia in place
copia = lista1.copy()         # crea copia
print(len(lista1))            # lunghezza lista
lista1.clear()                # svuota lista
print(lista1)
print(copia)

# Appartenenza:
li = [3, 8, 12, 23, 4, 80]
print(3 in li)              # True: il 3 è nella lista li
print(2 not in li)          # True: il 2 non è nella lista li

# Funzioni Built-in:
print(sum(li))              # Stampa la somma della lista li, cioè 130
print(min(li))              # Stampa a video il minimo della lista li, cioè 3
print(max(li))              # Stampa a video il massimo della lista li, cioè 80

# Concatenazione e Ripetizione:
a = [3, 9] + [30, 12]             # [3, 9, 30, 12]
b = [0] * 5                       # inizializza una lista b di cinque zeri [0, 0, 0, 0, 0]
print(a, b)

c = [1, 2, 3] * 3
print(c)

# Errori e Copia
ab = [1, 2, 3]

# c = ab            NON è una copia! b punta alla stessa lista!
# c[0] = 99
# print(ab)        # [99, 2, 3]  ← anche 'a' è cambiata!

# Modi corretti per copiare
c = ab.copy()
c = ab[:]
c = list(ab)
print(c)

# Liste Annidate:
matrice = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

print(matrice[0])      # prima riga: [0, 1, 2]
print(matrice[1][2])   # elemento all'indice 1 di riga e all'indice 2 di colonna, cioè 5

# Scorrere una matrice:
for riga in matrice:
    for elemento in riga:
        print(elemento,end="")
    print()

# Tuple (non modificabili): ------------------------------------------------------------------------------
coordinate = (10, 20)
colori = "rosso", "verde", "blu"
singola = (42,)                     # virgola obbligatoria per tuple di un elemento
senza_parentesi = 1, 2, 3           # le parentesi sono opzionali
vuota = ()

t = (10, 30, 50, 30, 70)

print(t[0])           # 10
print(t[-1])          # 70
print(t[1:3])         # (30, 50)

print(t.count(30))      # conta le occorrenze di 30
print(t.index(30))      # indice della prima occorrenza di 30

# Unpacking Tuple:
coordinate = (10, 20)
x, y = coordinate
print(x)
print(y)

# Scambiare variabili senza variabile temporanea:
a, b = 5, 10
a, b = b, a
print(a, b)    # stampa 10, 5

# Unpacking con asterisco * :
primo, *altro = (1, 2, 3, 4, 5)
print(primo)                         # 1
print(altro)                         # [2, 3, 4, 5]

*inizio, ultimo = (1, 2, 3, 4, 5)    
print(inizio)                        # [1, 2, 3, 4]
print(ultimo)                        # 5

# Funzioni che restituiscono più valori:
def min_max(lista):
    return(min(lista), max(lista))  # restituisce una tupla
print(min_max(lista))               # (20, 100) di lista = [20, 40, 60, 80, 100]

minimo, massimo = min_max([5, 12, 2, 90])
print(minimo)  # 2
print(massimo) # 90

# Somma di tutti i multipli di 3 o di 5 sotto 1000
multipli = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
print(sum(multipli))   #233168

# Trovare il massimo di una lista senza max
def trova_max(lista):
    maxim = lista[0]
    for elem in lista :
        if elem > maxim :
            maxim = elem
    return maxim

lista_z = [4, 5, 6]
print(trova_max(lista_z))    # 6

# Rimuovi duplicati in lista
def rimuovi_duplicati(lista):
    vista = []
    for x in lista:
        if x not in vista :
            vista.append(x)
    return vista

lista_y = [5, 3, 2, 8, 3]
print(rimuovi_duplicati(lista_y))