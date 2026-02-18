# Somma Cifre in breve
numero = 12345
somma_cifre = sum(int(c) for c in str(numero))
print(f"La somma delle cifre del numero {numero} è {somma_cifre}.")

# Somma Cifre algoritmicamente
nume = 98765
somma = 0
while nume > 0 :
    cifra = nume % 10
    somma += cifra
    nume //= 10
print(f"La somma delle cifre del numero 98765 è {somma}.")

# Somma Cifre con definizione di Funzione
def somma_cifre(n):
    print(sum(int(cifra) for cifra in n))

print(f"La somma delle cifre del numero è:", end=" ")
somma_cifre("123")

