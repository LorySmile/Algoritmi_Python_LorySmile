# definire una Funzione
def saluta():
    print("Ciao")                 # Ciao
saluta()

# con parametri
def somma(a, b):
    return a+b
risultato = somma(3, 5)           # 8
print(risultato)

# con parametri di default
def potenza(base, esponente=2):
    return base ** esponente
print(potenza(5))                # 25
print(potenza(5, 3))             # 125

# controllo Numero Primo
def is_prime(n):
    if n < 2 :
        return False
    for i in range(2, int(n**0.5) + 1):       # un multiplo va da 2 alla sua radice quadra, 
        if n % i == 0 :                       # essendo l'indice che parte da 0, si mette + 1
            return False                      # e si vede poi se n è divisibile per i, allora non è primo
    return True                               # altrimenti uscendo dal ciclo restano i numeri primi

if is_prime(11):
    print("Si, 11 è numero primo!")

# 

