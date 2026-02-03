# Calcolare la somma di tutti i numeri amichevoli minori di 10000

def somma_divisori(n: int) -> int:
    total = 1                              # 1 è un divisore di tutti i numeri
    for i in range(2, int(n**0.5) + 1):    # int(n**0.5) significa radice quadrata di n
        if n % i == 0:                     # Se i è un divisore di n
            total += i
            if i != n // i:                # Aggiungi anche il divisore complementare
                total += n // i
    return total                           # Restituisce la somma dei divisori propri di n
amicabili = set()                          # Insieme per memorizzare i numeri amichevoli trovati
for numero in range(2, 10000):             # Itera attraverso tutti i numeri da 2 a 9999
    partner = somma_divisori(numero)       # Trova il "partner" del numero
    if partner != numero and somma_divisori(partner) == numero:
        amicabili.add(numero)              # Aggiungi il numero amichevole all'insieme
        amicabili.add(partner)             # Aggiungi anche il suo partner
print(sum(amicabili))                      # Stampa la somma di tutti i numeri amichevoli trovati

# La somma dei numeri amichevoli minori di 10000 è 31626