# Qual è il multiplo più piccolo divisibile per tutti i numeri da 1 a 20?
# cioè l'LCM (Least Common Multiple) di questi numeri.

from math import gcd                   # Importa gcd per calcolare il massimo comune divisore
from functools import reduce           # Importa reduce per applicare una funzione cumulativamente a una lista
def lcm(a: int, b: int) -> int:        # Funzione che prende in input due numeri e restituisce il loro LCM
    return abs(a * b) // gcd(a, b)     # Calcola l'LCM di due numeri usando il GCD, abs per sicurezza con numeri negativi
result = reduce(lcm, range(1, 21))     # Calcola l'LCM di tutti i numeri da 1 a 20, reduce serve ad applicare lcm in cascata

print(result)  # il multiplo più piccolo è 232792560