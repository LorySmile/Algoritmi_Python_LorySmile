# Calcola il numero inferiore a un milione che genera la sequenza di Collatz più lunga.

# La sequenza di Collatz si ottiene seguendo queste regole:
# - Inizia con un numero intero positivo n. 
# - Se n è pari, il successivo numero è n/2.
# - Se n è dispari, il successivo numero è 3n + 1.
# - La sequenza termina quando si raggiunge 1.

def lunghezza_collatz(n):
    lunghezza = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        lunghezza += 1
    return lunghezza

lunghezza_massima = 0
numero_massimo = 0

for i in range(1, 1000000):
    lunghezza = lunghezza_collatz(i)
    if lunghezza > lunghezza_massima:
        lunghezza_massima = lunghezza
        numero_massimo = i

print("Il numero che genera la sequenza di Collatz più lunga è", numero_massimo) # il numero che genera la sequenza di Collatz più lunga è 837799

# Extra: stampare la lunghezza della sequenza
print("La lunghezza della sequenza è",lunghezza_massima) # la lunghezza della sequenza è 525