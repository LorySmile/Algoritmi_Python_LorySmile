# Contare il numero di domeniche che ricadono il primo giorno del mese tra il 1° gennaio 1901 e il 31 dicembre 2000

import datetime
domenica_count = 0
for anno in range(1901, 2001):
    for mese in range(1, 13):
        if datetime.date(anno, mese, 1).weekday() == 6:  # 6 rappresenta la domenica
            domenica_count += 1
print(domenica_count)  # Il numero di domeniche è 171