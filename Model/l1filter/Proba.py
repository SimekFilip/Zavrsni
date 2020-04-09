import csv
import numpy as np
from pandas_wrapper import l1tf
import pandas as pd

# uvoz podataka iz datoteke
with open('NYSE_prices_daily.csv') as f:
    lines = list(csv.reader(f))
f.close()

broj_dionica = len(lines[0])-1
print(broj_dionica)
# 761 - broj trgovanih dana u prve tri godine
# za ubuduce plan traziti datume

# IDEJA - STAVITI CIJELI RACUN U FUNKCIJU KOJA CE IMATI DVA PARAMETRA
#       - POCETNU VREMENSKU TOCKU I KONACNU

zeros = [[0] * 20 for _ in range(10)]  # 2D array, prvi broj - stupci, drugi - retci
'''
for i in zeros:
    print(i)
'''
for stupac in range(1, 10):  # drugi broj mora biti broj_dionica+1
    x = pd.Series(np.asarray([float(e[stupac]) for e in lines[1:761]]))
    for delta in range(1, 21): # drugi broj mora biti konacna_delta+1
        filter_data = l1tf(x, delta)
        nagib = filter_data[filter_data.size-1] / filter_data[filter_data.size-2]
        if nagib > 1:
            zeros[stupac-1][delta-1] = 1
        elif nagib < 1:
            zeros[stupac - 1][delta - 1] = -1
        else:
            zeros[stupac - 1][delta - 1] = 0
        # print(lines[0][stupac] + ", delta: " + str(delta) + " - nagib: " + str(nagib))
    print(lines[0][stupac] + " obraden")

# for i in zeros:
#    print(i)

# ispis rezultata u datoteku
f1 = open('c:/filip/fer/3.godina/6.semestar/završni rad/output.csv', "w+")
for key in zeros:
    f1.write("%s\n" % key)
f1.close()

del zeros


exit(0)
