# Calcolare la somma di tutti i numeri naturali minori di 1000 che sono multipli di 3 o 5. 

somma = sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0)
print(somma) 

# la somma è 233168