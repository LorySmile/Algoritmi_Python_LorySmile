nome = "Lorenza"
print(type(nome))     # <class 'str'>

print(ord("A"))          # ord() scrive il codice unicode di un carattere o simbolo (65)
print(chr(65))           # chr() prende un numero unicode e lo trasforma nel carattere corrispondente (A)
print(nome.isalpha())    # isalpha() controlla se tutti i caratteri sono lettere alfabetiche (True)
print(nome.islower())    # islower() controlla se sono tutte lettere minuscole (False)

aggiunta = "Lorenza" + " " + "Cicero"
print(aggiunta)
print(len(aggiunta))    # la lunghezza della stringa comprende lo spazio
print(nome[0:4])        # output: Lore (perchè posizione zero compresa e quarta esclusa)
print(aggiunta[::-1])   # stringa capovolta dalla fine all'inizio
print(nome[2:])         # dalla seconda posizione fino a fine stringa: renza
print(aggiunta[:5])     # dall'inizio alla quinta posizione esclusa: Loren

voto = 30
print(f"Ciao {aggiunta}, il tuo voto è {voto} !")
print("Ciao", aggiunta, "il tuo voto è", voto, "!")

print(f"Il Pi-greco è circa {3.14159:.2f}")    # :.2f si mette per approssimare a due cifre dopo la virgola

vero = True
falso = False
print(type(vero))    # <class: 'bool'>
# i Bool sono int in Python!
print(True + True)   # stampa 2
print(True * 5)      # stampa 5
# Python considera False: False, 0, 0.0, "", [], {}, None
# Tutto il resto è considerato True

risultato = None    # nessun valore
x = None
if x is None : 
    print("x non ha un valore")
# per confrontare con None bisogna usare: is None

# Conversione tra tipi: Casting

# da stringa a intero:
a = int("42")     # non funziona con numeri decimali

# da stringa a float:
b = float("3.14")
c = float("20")   # 20.0

# da numero a stringa:
d = str(23)
e = str(4.10)

# da float a intero:
f = int(4.9)     # 4
g = int(-4.9)    # -4 (tronca non arrotonda!)

# da stringa a bool:
h = bool("")        # False
i = bool("aeiou")   # True

# Operazioni aritmetiche

z, y = 10, 5

print(z + y)      # addizione
print(z * y)      # moltiplicazione
print(z / y)      # divisione con risultato float
print(z // y)     # divisione con risultato int
print(z % y)      # modulo o resto
print(z ** y)     # elevazione a potenza

# capire se un numero è pari

n = 7
if n % 2 == 0 :
    print("pari")
else:
    print("dispari")

# estrarre cifre da numeri
r = 1234
print(r % 10)   # estrae e stampa 4
print(r // 10)  # stampa 123

# Operatori di Confronto (restituiscono Bool)
print(5 == 5)      # True (uguale)
print(5 != 3)      # True (diverso)
print(5 > 2)       # True (maggiore)
print(5 >= 5)      # True (maggiore o uguale)
print(5 < 2)       # False (minore)
print(5 <= 4)      # False (minore o uguale)

# Operatori Logici
print(True and False)    # False perchè è vera solo se entrambe sono vere
print(True or False)     # True perchè è vera se almeno una delle due è vera
print(not(True))         # False (negazione)

# Esempio pratico:
età = 20
ha_patente = True
if età >= 18 and ha_patente :
    print("Può guidare!")

# Operatori di assegnazione:
x = 10
x += 3      # sarebbe x = x + 3
x -= 3
x *= 3
x //= 3     # x = x // 3
x %= 5

# Output:
print("Ciao.")                          # stampa con new line a capo
print("Ciao", "io", "sono", "Lory")     # Ciao io sono Lory (con spazio di default)
print("Make", "up", sep="-")            # Make-up (mette il separatore - tra le parole)
print("Ciao ciao.", end="")             # stampa e non va a capo

# Input:
nome = input("Come ti chiami? ")         # restituisce sempre una stringa
eta = int(input("Quanti anni hai? "))    # converte l'input subito in int





