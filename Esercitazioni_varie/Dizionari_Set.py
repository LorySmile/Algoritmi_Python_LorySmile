# Dizionario vuoto:
diz = {}
diz2 = dict()

# Creare un dizionario:
studente = {
    "Nome" : "Lorenza",
    "Cognome" : "Cicero",
    "Età" : 38,
    "Università" : "UniME",
    "Voti" : [30, 28, 27]
}

# Accesso alle componenti del dizionario:
print(studente["Nome"])
print(studente["Cognome"])
print(studente["Voti"])

print(studente.get("Matricola"))                     # restituisce None senza dare errore se non esiste la chiave
print(studente.get("Matricola", "Non Presente"))     # restituisce Non Presente se non esiste la chiave

studente["Matricola"] = 355275    # aggiunge la chiave Matricola con elemento 355275
print(studente)

studente["Età"] = 35              # modifica un valore esistente
print(studente)

studente.update({"Corso" : "Informatica", "Città" : "Messina"})   # Inserire nuove coppie chiave-valore
print(studente)

del studente["Voti"]   # cancella una coppia chiave-valore
print(studente)

eta = studente.pop("Età")    # rimuove e restituisce il valore
print(eta)
print(studente)

chiave, valore = studente.popitem()    # rimuove l'ultima coppia chiave- valore e la restituisce
print(studente)
print(chiave, valore)

studente.clear()  # pulisce il dizionario
print(studente)   # {}

# Metodi principali:
diz_stud = {"Nome" : "Lorenza", "Età" : 35, "Matricola" : 355275}

print("Nome" in diz_stud)   # True
print("Voti" in diz_stud)   # False

print(diz_stud.keys())           # chiavi del dizionario, output: dict_keys(['Nome', 'Età', 'Matricola'])
chiavi = list(diz_stud.keys())   # estrarre le chiavi e inserirle in una lista
print(chiavi)                    # ['Nome', 'Età', 'Matricola']

print(diz_stud.values())           # valori del dizionario, output: dict_values(['Lorenza', 35, 355275])
valori = list(diz_stud.values())   # estrarre i valori e inserirli in una lista
print(valori)                      # ['Lorenza', 35, 355275]

print(diz_stud.items())      # ottenere tutte le coppie chiave-valore

print(len(diz_stud))         # lunghezza del dizionario

# Iterare su un dizionario:
for chiave in diz_stud :
    print(chiave)

for valore in diz_stud.values():
    print(valore)

for chiave, valore in diz_stud.items():
    print(f"{chiave}: {valore}")

# Dizionari Annidati:
studenti = {
    "studente1": {
        "Nome" : "Mario Cuciti",
        "Matricola" : 324564,
        "Voti" : [25, 28, 29]
    },
    "studente2": {
        "Nome" : "Lorenza Cicero",
        "Matricola" : 355275,
        "Voti" : [28, 29, 30]
    }
}

print(studenti["studente1"]["Nome"])     # Mario Cuciti
print(studenti["studente1"]["Voti"][2])  # 29 (indice 2)

studenti["studente3"] = {"Nome" : "Giulia Giannetto", "Matricola" : 273623, "Voti" : [23, 28, 29]}  # aggiunge studente
print(studenti)

# Chiavi Valide (immutabili):
d = {
    "stringa": 1,
    42: "numero",
    (1, 2): "tupla",
    True: "booleano"
}

# Ottenere un valore, se non esiste lo crea:
voto = {}
voto.setdefault("Matematica", []).append(28)
voto.setdefault("Matematica", []).append(30)
voto.setdefault("Fisica 2", []).append(27)
voto.setdefault("Fisica 2", []).append(39)
print(voto)                                    # {'Matematica': [28, 30], 'Fisica 2': [27, 39]}

# Contare Occorrenze:
testo = "io sono brava"
conteggio = {}
for lettera in testo :
    conteggio[lettera] = conteggio.get(lettera, 0) + 1
print(conteggio)

# I SET: un set è una lista non ordinata di elementi unici (non ammette duplicati) ------------------------
numeri = {1, 2, 3, 4, 5}
colori = {"rosso", "verde", "blu"}

vuoto = set()    # set vuoto

# Passare da lista a set per eliminare i duplicati:
lista_num = [1, 3, 6, 2, 3, 9, 5, 9, 3, 6, 3]
set_num = set(lista_num)
print(set_num)

# Operazioni Base sui Set:
s = {5, 10, 20, 50, 80}
print(s)

s.add(4)    # aggiunge elemento al set
print(s)

s.update([8, 10])    # aggiunge più elementi, in questo caso 10 è ripetuto e resta una volta sola nel set
s.update([28, 40, 78])   # aggiunge altri tre elementi (non in ordine nei set)
print(s)

s.remove(10)        # elimina 10, se non ci fosse l'elemento darebbe errore
print(s)
s.discard(9)        # nessun errore se non esiste, resta in output il set uguale
print(s)
s.discard(28)       # elimina 28, nessun errore se non esistesse nel set
print(s)

x = s.pop()         # elimina un elemento del set a caso
print(x)
print(s)

x = s.pop()
print(x)
print(s)

x = s.pop()         # in realtà li sta eliminando a uno a uno da sinistra (al contrario che con le liste, era a destra)
print(x)
print(s)

print(8 in s)       # Controllo: True se esiste nel set l'elemento 8, False altrimenti (è stato tolto quindi l'output è False)

s.clear()     # pulisce/svuota il set

# Operazioni Insiemistiche:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)         # unisce gli elementi di a e b, a OR b, e li stampa
print(a.union(b))    # {1, 2, 3, 4, 5, 6, 7, 8}

print(a & b)                # interseca a e b, a AND b, e li stampa
print(a.intersection(b))    # {4, 5}

print(a - b)              # elementi che sono in a ma non sono in b, differenza tra a e b
print(a.difference(b))    # {1, 2, 3}

print(a ^ b)                         # elementi che sono in a o in b ma non in entrambi, a XOR b
print(a.symmetric_difference(b))     # {1, 2, 3, 6, 7, 8}

print({1, 2} <= a)                # è sottoinsieme di a ? True
print({1, 2, 7, 8} <= a)          # False

print({4, 5, 6, 7, 8, 9} >= b)    # è sovrainsieme di b ? True
print({4, 5, 6, 7} >= b)          # False

print({1, 2, 3} <= {1, 2, 3, 4})  # True (l'ordine nei set non conta)
print({2, 1, 3} <= {3, 1, 4, 2})  # True

# Set immutabili con frozenset possono essere usati come chiavi di dizionario:
fs = frozenset([1, 2, 3])
print(fs)                   # stampa frozenset({1, 2, 3})

d = {fs : "valore"}    # usato come chiave del dizionario d

# ------------------------------------------------------------------------
""" **3. CONFRONTO: LISTA vs TUPLA vs DIZIONARIO vs SET**
```
┌─────────────┬───────────┬──────────┬──────────┬──────────┐
│             │   LISTA   │  TUPLA   │   DICT   │   SET    │
├─────────────┼───────────┼──────────┼──────────┼──────────┤
│ Ordinata    │    si     │    si    │ si(3.7+) │    no    │
│ Mutabile    │    si     │    si    │    si    │    si    │
│ Duplicati   │    si     │    si    │ no chiavi│    no    │
│ Indicizzata │    si     │    si    │ per key  │    no    │
│ Sintassi    │  [1,2,3]  │ (1,2,3)  │  {k:v}   │  {1,2,3} │
│ Lookup O(1) │    no     │    no    │    si    │    si    │
└─────────────┴───────────┴──────────┴──────────┴──────────┘
"""


# Contare quante volte appare uno stesso numero
numeri = [1, 2, 3, 1, 1, 4, 1, 5, 1, 5, 3, 2, 4, 4, 3, 3, 3]
frequenza = {}
for num in numeri :
    frequenza[num] = frequenza.get(num, 0) + 1
print(frequenza)                                        # {1: 5, 2: 2, 3: 5, 4: 3, 5: 2}

# esempio extra:
numeri = [3, 5, 6, 9, 10, 3, 10, 5, 5, 9, 6, 3, 6, 3]
conta = {}
for numerini in numeri :
    conta[numerini] = conta.get(numerini, 0) + 1
print(conta)                                            # {3: 4, 5: 3, 6: 3, 9: 2, 10: 2}

# esempio con una stringa:
stringa_corta = "supercalifragilistichespiralidoso"
conteggio_lettere = {}
for letterina in stringa_corta :
    conteggio_lettere[letterina] = conteggio_lettere.get(letterina, 0) + 1
print(conteggio_lettere)                               
# {'s': 4, 'u': 1, 'p': 2, 'e': 2, 'r': 3, 'c': 2, 'a': 3, 'l': 3, 'i': 6, 'f': 1, 'g': 1, 't': 1, 'h': 1, 'd': 1, 'o': 2}

# Trovare elementi unici senza ripetizioni:
list_1 = [1, 5, 6, 3, 2, 8, 1, 3, 6, 8]
print(list(set(list_1)))
# altrimenti scrivo:
unica = list(set(list_1))
print(unica)                                    # [1, 2, 3, 5, 6, 8]

# Trovare l'intersezione di due liste:
list_2 = [1, 2, 3, 4, 5]
list_3 = [2, 4, 6, 8, 10]
comuni = list(set(list_2) & set(list_3))
print(comuni)                                   # [2, 4]

# Invertire dei valori in un dizionario:
voti_dati = {
    "Mario Vitale" : 28,
    "Pamela Prati" : 22,
    "Giucas Casella" : 30,
    "Fabrizio Conte" : 24
}

studente_con_miglior_voto = max(voti_dati, key=voti_dati.get)    # prende il nome dello studente con il miglior voto
print(studente_con_miglior_voto)                                 # Giucas Casella

inverto = {v : k for k, v in voti_dati.items()}                  # funziona solo se ogni valore è diverso dall'altro
print(inverto)
# {28: 'Mario Vitale', 22: 'Pamela Prati', 30: 'Giucas Casella', 24: 'Fabrizio Conte'}

# le chiavi devono sempre essere diverse le une dalle altre, quindi se dei voti fossero uguali
# si sovrascriverebbe qualche nome... funziona bene solo nel caso in cui ciascun voto è diverso

# Raggruppare Elementi:
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
raggruppa = {"pari" : [], "dispari" : []}
for num1 in numeri :
    if num1 % 2 == 0 :
        raggruppa["pari"].append(num1)
    else:
        raggruppa["dispari"].append(num1)
print(raggruppa)                               # {'pari': [2, 4, 6, 8, 10], 'dispari': [1, 3, 5, 7, 9]}






