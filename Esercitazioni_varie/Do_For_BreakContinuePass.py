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
    print(i, end=" ")
print("")
# 1, 3, 5, 7, 9

# Saltare elementi vuoti
lista = ["a", "", "b", "", "c"]
for elemento in lista:
    if not elemento:              # se è stringa vuota
        continue
    print(elemento, end=" ")               # a, b, c

