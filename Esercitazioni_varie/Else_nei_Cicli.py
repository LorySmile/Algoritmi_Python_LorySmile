# ELSE nei Cicli - particolarità di Python! ----------------------------------------------------
# Il blocco else dopo un ciclo viene eseguito solo se il ciclo NON è stato interrotto da break.

# Cercare un numero
numeri = [1, 3, 5, 7, 9]
cercato = 4

for num in numeri:
    if num == cercato:
        print("Trovato!")
        break
else:
    print("Non trovato")  # eseguito solo se NON c'è break
                          # Output: "Non trovato"

# Esempio con while
tentativi = 0
while tentativi < 3:
    password = input("Password: ")
    if password == "Python123":
        print("Accesso consentito")
        break
    tentativi += 1
    print("Sbagliato! Hai ancora {tentativi} tentativi!")   # se non c'è break
else:
    print("Troppi tentativi falliti")   # se non c'è break