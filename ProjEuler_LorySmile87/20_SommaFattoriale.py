# Calcolare la somma delle cifre del fattoriale di 100 (100!)

import math                           # Importa il modulo math per calcolare il fattoriale
fattoriale_100 = math.factorial(100)  # Calcola 100!
somma_cifre = sum(int(cifra) for cifra in str(fattoriale_100))  # Somma le cifre del numero convertito in stringa
print(somma_cifre)                                              # La somma delle cifre è 648

# Spiegazione:
# 1. Usiamo math.factorial per calcolare 100!. 
# 2. Convertiamo il risultato in una stringa per poter iterare su ogni cifra.
# 3. Usiamo una comprensione di lista per convertire ogni carattere della stringa di nuovo in un intero e sommarli tutti insieme con la funzione sum().
# 4. Infine, stampiamo il risultato della somma delle cifre.
# Il risultato finale è 648.

# La complessità computazionale è O(n^2 log n) a causa del calcolo del fattoriale e della somma delle cifre.