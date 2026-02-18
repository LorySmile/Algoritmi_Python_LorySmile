# Fattoriale di 10 + fattoriale di un numero inserito ----------------------
# n = 10
n = int(input("Inserisci il numero di cui calcolare il fattoriale: "))
fattoriale = 1
for i in range(1, n+1):
    fattoriale *= i
print(fattoriale)         # il fattoriale di 10 è 3628800

# Fattoriale in Funzione con ricorsione --------------------------------------------------------
def fattoriale(n):
    if n <= 1 :
        return 1
    return n * fattoriale(n-1)    # ricorsione

print(f"Il fattoriale di 3 (che si scrive 3!) è {fattoriale(3)}")
