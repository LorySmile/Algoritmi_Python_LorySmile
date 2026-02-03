# Trovare il prodotto dei coefficienti a e b per il quale il polinomio n^2 + an + b genera il massimo numero di numeri primi consecutivi per n = 0, 1, 2, ...

def is_prime(num: int) -> bool:               # se il numero è primo
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):     # controlla i divisori fino alla radice quadrata di num
        if num % i == 0:
            return False
    return True

max_count = 0
result = 0

for a in range(-999, 1000):                       # coefficiente a tra -999 e 999
    for b in range(-1000, 1001):                  # coefficiente b tra -1000 e 1000
        n = 0
        while True:
            quadratic_value = n**2 + a*n + b      # calcola il valore del polinomio
            if is_prime(quadratic_value):
                n += 1
            else:
                break

        if n > max_count:                         # se il conteggio è il massimo trovato finora
            max_count = n
            result = a * b
            
print(result)  # Il prodotto dei coefficienti a e b è -59231