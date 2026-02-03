# Calcolare la somma di tutti i numeri pari 
# nella sequenza di Fibonacci minori di 4 milioni partendo da 1 e 2.

a, b = 1, 2
somma_pari = 0  
while a < 4000000:
    if a % 2 == 0:
        somma_pari += a
    a, b = b, a + b
print(somma_pari)

# la somma è 4613732

# Nella normale sequenza di Fibonacci, i termini pari compaiono con periodicità: 
# ogni 3 numeri uno è pari. Si può sfruttare per ottimizzare ancora 
# (generando direttamente solo i pari), 
# ma qui non è necessario per il limite dato.