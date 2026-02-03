# Calcolare la somma dei punteggi di tutti i nomi nel file names.txt
# importo la libreria necessaria

import os
with open("names.txt", "r") as f:
    nomi = sorted(f.read().replace('"', '').split(','))  # Leggi e ordina i nomi
    punteggio_totale = 0
    for i, nome in enumerate(nomi):
        punteggio = sum(ord(c) - ord('A') + 1 for c in nome)  # Calcola il punteggio del nome
        punteggio_totale += punteggio * (i + 1)               # Moltiplica per la posizione e aggiungi al totale
    print(punteggio_totale)                                   # Stampa il punteggio totale

# La somma dei punteggi dei nomi è 871198282
