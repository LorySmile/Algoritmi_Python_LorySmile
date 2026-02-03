# Calcolare la somma di tutti i numeri interi positivi che non possono essere scritti come somma di due numeri abbondanti.

def is_abundant(n: int) -> bool:
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total > n
abundant_numbers = [i for i in range(1, 28124) if is_abundant(i)]
can_be_written_as_abundant_sum = [False] * 28124
for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        abundant_sum = abundant_numbers[i] + abundant_numbers[j]
        if abundant_sum < 28124:
            can_be_written_as_abundant_sum[abundant_sum] = True
        else:
            break
result = sum(i for i in range(1, 28124) if not can_be_written_as_abundant_sum[i])
print(result)  
# La somma dei numeri che non possono essere scritti come somma di due numeri abbondanti è 4179871