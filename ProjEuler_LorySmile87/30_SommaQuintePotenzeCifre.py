# Trovare la somma di tutti i numeri che possono essere scritti 
# come somma delle quinte potenze delle loro cifre.

def sum_of_fifth_powers(n: int) -> int:
    return sum(int(digit) ** 5 for digit in str(n))
result = sum(n for n in range(10, 6 * (9 ** 5)) if n == sum_of_fifth_powers(n))

print(result)  # La somma è 443839