# Condizioni, Control Flow, Loop ------------------------------------

# if base:
età = 20
if età >= 18 :
    print("puoi guidare")
    print("perchè sei maggiorenne")

# if else:
voto = 28
if voto >= 30 :
    print("Lode!")
else:
    print(f"{voto}, bene, ma si può migliorare!")

# if, elif, else:
voto = 25
if voto >= 30 :
    print("Eccellente! 30 e Lode!")
elif voto >= 27 :
    print("Ottimo!")
elif voto >= 24 :
    print("Buono!")
elif voto >= 18 :
    print("Sufficiente!")
else:                              # else è opzionale
    print("Insufficiente!")

# if annidati:
ha_patente = True
età = 18
if età >= 18 :
    if ha_patente :
        print("Puoi guidare, sei maggiorenne!")
    else:
        print("Non hai la patente, non puoi guidare!")
else:
    print("Non sei maggiorenne! Non puoi guidare!")

# con operatori logici si scrive meno codice:
if età >= 18 & ha_patente :
    print("Puoi guidare, sei maggiorenne ed hai la patente!")

# Operatore Ternario (if in una riga) -----------------------------

# se scrivo per esteso:
if età >= 18 :
    status = "maggiorenne"
else:
    status = "minorenne"

# in forma compatta (ternario):
status = "Maggiorenne" if età >= 18 else "Minorenne"
print(status)

# altro esempio:
votino = 30
risultato = "Ottimo!" if votino == 30 else "Potevi fare di meglio, va bene lo stesso!"
print(risultato)

# Condizioni Multiple:

# AND: tutte le condizioni devono essere vere
ha_assicurazione = True
if età >=18 and ha_patente and ha_assicurazione :
    print("Puoi guidare tranquillamente!")

# OR: almeno una condizione deve essere vera
giorno = "sabato"
if giorno == "sabato" or giorno == "domenica" :
    print("Week-end!")

# NOT: negazione
piovoso = False
if not piovoso :
    print("Andiamo al mare!")

# Combinazione:
if (giorno == "sabato" and piovoso == False) or status == "Maggiorenne" :
    print("Si esce!")

"""

Valori FALSY (considerati False)

if 0:           pass  # NON viene eseguito
if "":          pass  # NON viene eseguito (stringa vuota)
if []:          pass  # NON viene eseguito (lista vuota)
if {}:          pass  # NON viene eseguito (dict vuoto)
if None:        pass  # NON viene eseguito
if False:       pass  # NON viene eseguito

Tutto il resto è TRUTHY (considerato True)

if 1:           pass  # viene eseguito
if "ciao":      pass  # viene eseguito
if [1, 2]:      pass  # viene eseguito
if {"a": 1}:    pass  # viene eseguito

"""

# Esempio pratico
nome = input("Nome: ")
if nome:                     # se la stringa NON è vuota
    print(f"Ciao {nome}")
else:
    print("Non hai inserito un nome!")

# For Loop - Cicli iterativi ------------------------------------------------

# For su Liste:
numeri = [1, 2, 3, 4, 5]
for numero in numeri :
    print(numero)         # stampa 1 2 3 4 5 tutti uno sotto l'altro

totale = 0
for numero in numeri :
    totale += numero
print(totale)             #15

# For su Stringhe:
parola = "Python"
for lettera in parola :
    print(lettera)        # scrive una sotto l'altra le lettere P y t h o n

testo = "Mississippi"
vocali = 0
for lettera in testo.lower():
    if lettera in "aeiou":
        vocali += 1
print(vocali)                   # 4

# RANGE ---------------------------------------------------------------------

# Range (stop)
for i in range(5):
    print(i)

# Range (start - stop)
for i in range(2, 7):             # dal primo all'ultimo escluso
    print(i)

# Range (start - stop -step)
for i in range(0, 10, 2):         # a due a due dal primo all'ultimo escluso
    print(i)
    
# Range decrescente
for i in range(0, 10, -1):
    print(i)                      # 10 9 8 7 6 5 4 3 2 1

# Convertire da Range a Lista
lista_r = list(range(5))
print(lista_r)                    # [0, 1, 2, 3, 4]

# Enumerate --------------------------------------------------------------------
lista_o = [23, 56, 78, 76, 98]
for valore, elem in enumerate(lista_o):
    print(f"Indice {valore}: {elem}")

# Senza Enumerate e con Range avrei scritto:
for i in range(len(lista_o)):
    print(f"Indice {i}: {lista_o[i]}")

# Partendo da 1 invece che da 0
nomi = ["Bob", "Giucas", "Valery"]
for indice, nome in enumerate(nomi, start=1):
    print(f"Indice {indice}: {nome}")

# ZIP - Iterare su più liste insieme: ----------------------------------------------

nomi1 = ["Marlena", "Verdiana", "Margherita"]
età1 = [25, 30, 45]

for nome, età, in zip(nomi1, età1):
    print(f"{nome}: {età} anni.")

# Enumerate + Zip :
nomi = ["Miriam", "Paola", "Viviana"]
voti = [30, 28, 26]
for i, (nome, voto) in enumerate(zip(nomi, voti), start=1):
    print(i, nome, voto)

# Creare un dizionario da due liste con dict() e zip():
studenti = dict(zip(nomi, voti))
print(studenti)

# FOR su Dizionari: -------------------------------------------------------------
studente = {"Nome" : "Lorenza", "Età" : 30, "Voto" : 30}

for chiave in studente :                   # iterare sulle chiavi (default)
    print(chiave)

for valore in studente.values():           # iterare sui valori
    print(valore)

for chiave, valore in studente.items():    # iterare su chiavi e valori
    print(f"{chiave}: {valore}")

# FOR annidati, Matrici e Tabelle: -------------------------------------------

# Tabella di moltiplicazione
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# Matrice
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for riga in matrice :
    for elemento in riga:
        print(elemento, end=" ")
    print()

# Con Indici
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        print(f"Matrice[{i}][{j}]: {matrice[i][j]}")


# WHILE - LOOP - Cicli Condizionali : -----------------------------------------

# While base (attenzione ai loop infiniti, usare break se serve)
count = 0
while count < 5 :
    print(count)
    count += 1        # 0 1 2 3 4

# While con input
while True:
    risp = input("Inserisci un numero: ")
    if risp.isdigit():
        num = int(risp)
        break
    else:
        print("Non valido, riprova.")

# Password
tentativi = 3
while tentativi > 0 :
    password = input("Password: ")
    if password == "Python123" :
        print("Accesso Consentito!")
        break
    else:
        tentativi -= 1
        if tentativi == 0 :
            print(f"Sbagliato! Hai finito i tentativi!")
        else:    
            print(f"Sbagliato! Hai ancora {tentativi} tentativi.")
        
