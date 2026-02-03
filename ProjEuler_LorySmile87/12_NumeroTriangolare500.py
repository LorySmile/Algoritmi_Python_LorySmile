# Qual è il primo numero triangolare ad avere più di 500 divisori?

def numero_triangolare(n: int) -> int:
    return n * (n + 1) // 2

def conta_divisori(num: int) -> int:
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 2              # i e num // i sono entrambi divisori
    if int(num**0.5) ** 2 == num:
        count -= 1                  # se num è un quadrato perfetto, togliamo uno
    return count

n = 1

while True: 
    tri_num = numero_triangolare(n)
    div_count = conta_divisori(tri_num)
    if div_count > 500:
        print(tri_num)  # il primo numero triangolare con più di 500 divisori è 76576500
        break
    n += 1  

# Spiegazione:
# La funzione numero_triangolare calcola il n-esimo numero triangolare.
# La funzione conta_divisori conta il numero di divisori di un dato numero.
# Il ciclo while continua a calcolare numeri triangolari e i loro divisori finché non trova uno con più di 500 divisori.
# Quando trova tale numero, lo stampa e termina.    

