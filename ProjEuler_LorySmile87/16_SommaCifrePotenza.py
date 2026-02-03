# Qual è la somma delle cifre del numero 2^1000?

numero = str(2**1000)               # Calcola 2^1000 e convertilo in stringa
somma_cifre = sum(int(cifra) for cifra in numero)  # Somma le cifre convertendole di nuovo in interi
print(somma_cifre)                  # la somma delle cifre è 1366

# Spiegazione:
# 1. Calcoliamo 2 elevato alla potenza di 1000 usando l'operatore **.
# 2. Convertiamo il risultato in una stringa per poter iterare su ogni cifra.
# 3. Usiamo una comprensione di lista per convertire ogni carattere della stringa di nuovo in un intero e sommarli tutti insieme con la funzione sum().
# 4. Infine, stampiamo il risultato della somma delle cifre.
# Il risultato finale è 1366.