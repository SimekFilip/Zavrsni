import csv
import numpy as np
from pandas_wrapper import l1tf
import pandas as pd

# uvoz podataka iz datoteke
with open('NYSE_prices_daily.csv') as f:
    lines = list(csv.reader(f))
f.close()

broj_dionica = len(lines[0])-1
# 761 - broj trgovanih dana u prve tri godine
# za ubuduce plan traziti datume

# 2D array, prvi broj - stupci (broj_lambdi), drugi - retci (broj_dionica)
zeros = [[0] * 1000 for _ in range(1)]


def l1(pocetak, kraj):
    for stupac in range(5, 6):  # drugi broj mora biti broj_dionica+1
        x = pd.Series(np.asarray([float(e[stupac]) for e in lines[pocetak:kraj]]))
        for delta in range(1, 1001):  # drugi broj mora biti konacna_delta+1
            filter_data = l1tf(x, delta)
            nagib = filter_data[filter_data.size-1] / filter_data[filter_data.size-2]
            if nagib > 1:
                zeros[0][delta - 1] = 1
                # zeros[stupac-1][delta-1] = 1
            elif nagib < 1:
                zeros[0][delta - 1] = -1
                # zeros[stupac - 1][delta - 1] = -1
            else:
                zeros[0][delta - 1] = 0
                # zeros[stupac - 1][delta - 1] = 0
        print(lines[0][stupac] + " obraden")
    return zeros


zeros = l1(1, 761)

# SLJEDECI CILJ - GRAFICKI PRIKAZATI PODATKE JEDNE LINIJE 2D POLJA

# ispis rezultata u datoteku
f1 = open('c:/filip/fer/3.godina/6.semestar/završni rad/output.txt', "w+")
for key in zeros:
    f1.write("%s\n" % key)
f1.close()

del zeros

exit(0)
