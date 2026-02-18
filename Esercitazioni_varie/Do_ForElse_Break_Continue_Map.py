# DO - WHILE in Python si simula --------------------------------------------------

while True :
    numero = int(input("Inserisci un numero positivo: "))
    if numero > 0 :
        break
    print("Deve essere un numero positivo!")
                                              # esegui almeno una volta e poi controlla

# BREAK, CONTINUE, ELSE ----------------------------------------------

# Break esce dal ciclo - Trovare un numero in una lista
numeri = [1, 3, 5, 7, 9, 10, 11]
trovato = False

for num in numeri:
    if num % 2 == 0:              # primo numero pari
        print(f"Trovato: {num}")
        trovato = True
        break                     # ESCE dal for

if not trovato:
    print("Nessun numero pari")

# Continue salta all'iterazione successiva
# Stampare solo i numeri dispari
for i in range(10):
    if i % 2 == 0:
        continue  # salta i numeri pari
    print(i)
# 1, 3, 5, 7, 9

# Saltare elementi vuoti
lista = ["a", "", "b", "", "c"]
for elemento in lista:
    if not elemento:              # se è stringa vuota
        continue
    print(elemento)               # a, b, c

# ELSE nei Cicli - particolarità di Python! ----------------------------------------------------
# Il blocco else dopo un ciclo viene eseguito solo se il ciclo NON è stato interrotto da break.

# Cercare un numero
numeri = [1, 3, 5, 7, 9]
cercato = 4

for num in numeri:
    if num == cercato:
        print("Trovato!")
        break
else:
    print("Non trovato")  # eseguito solo se NON c'è break
                          # Output: "Non trovato"

# Esempio con while
tentativi = 0
while tentativi < 3:
    password = input("Password: ")
    if password == "Python123":
        print("Accesso consentito")
        break
    tentativi += 1
    print("Sbagliato! Hai ancora {tentativi} tentativi!")   # se non c'è break
else:
    print("Troppi tentativi falliti")   # se non c'è break

# PASS - PLACEHOLDER ---------------------------------------------------------------
# pass non fa nulla, è un segnaposto, per dire "continuo dopo a scrivere il codice"

# Quando devi scrivere codice dopo
if voto >= 30:
    pass              # TODO: implementare logica lode
else:
    print("Bene")

# Ciclo vuoto
for i in range(10):
    pass              # nessuna operazione

# MAP applica una funzione ad ogni elemento ------------------------------------------
n = [1, 2, 3, 4, 5]
raddoppia = map(lambda x : x**2, n) # funzione che prende ogni elemento e lo eleva per 2
print(list(raddoppia))              # map() restituisce un iteratore, quindi va convertito
                                    # con list() se si vuole vedere il risultato

# FILTER tiene solo gli elementi per cui la funzione restituisce True ----------------
pari = filter(lambda x : x % 2 == 0, n)
print(list(pari))

# Esempi ---------------------------------------------

# Numeri Primi

