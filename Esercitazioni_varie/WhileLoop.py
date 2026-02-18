# WHILE - LOOP - Cicli Condizionali : --------------------------------------------------------------

# While base (attenzione ai loop infiniti, usare break se serve) ---------------------
count = 0
while count < 5 :
    print(count, end=" ")         # 0 1 2 3 4
    count += 1           
print("")

# While con input ----------------------------------------------------------------------
print("Se inserisci un numero positivo ti lascio stare, se no ti invio un messaggio!")
while True:
    risp = input("Inserisci un numero: ")
    if risp.isdigit():
        num = int(risp)
        break
    else:
        print("Non valido, riprova.")

# Password -----------------------------------------------------
print("Se sai la password accedi, altrimenti non accedi!")
tentativi = 3
while tentativi > 0 :
    password = input("Password: ")
    if password == "Python123" :
        print("Accesso Consentito!")
        break
    else:
        tentativi -= 1
        if tentativi == 0 :
            print(f"Sbagliato! Hai finito i tentativi!")
        else:    
            print(f"Sbagliato! Ritenta!")
        
