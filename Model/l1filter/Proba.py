import csv
import numpy as np
from pandas_wrapper import l1tf
import pandas as pd

# 761 - broj trgovanih dana u prve tri godine
# za ubuduce plan traziti datume


# 2D array, prvi broj - stupci (max_lambda), drugi - retci (broj_dionica = 571)
zeros = [[0] * 1000 for _ in range(70)]


def l1(pocetak, kraj):
    # uvoz podataka iz datoteke
    with open('NYSE_prices_daily.csv') as f:
        lines = list(csv.reader(f))
    f.close()
    # broj_dionica = len(lines[0]) - 1
    max_lambda = 1000
    br = 1
    firstCol = 501
    for stupac in range(firstCol, 571):  # drugi broj mora biti broj_dionica+1
        x = pd.Series(np.asarray([float(e[stupac]) for e in lines[pocetak:kraj]]))
        for delta in range(1, max_lambda+1):  # drugi broj mora biti konacna_delta+1
            filter_data = l1tf(x, delta)
            nagib = filter_data[filter_data.size-1] / filter_data[filter_data.size-2]
            if nagib > 1:
                zeros[stupac-firstCol][delta - 1] = 1
                # zeros[stupac-1][delta-1] = 1
            elif nagib < 1:
                zeros[stupac-firstCol][delta - 1] = -1
                # zeros[stupac - 1][delta - 1] = -1
            else:
                zeros[stupac-firstCol][delta - 1] = 0
                # zeros[stupac - 1][delta - 1] = 0
        print(lines[0][stupac] + " obraden " + str(br))
        br += 1
    return zeros


zeros = l1(1, 761)

# ispis rezultata u datoteku
f1 = open('c:/filip/fer/3.godina/6.semestar/završni rad/Model/data/100_stocks_lambda1-1000e.txt', "w+")
for key in zeros:
    f1.write("%s\n" % key)
f1.close()

del zeros

exit(0)
