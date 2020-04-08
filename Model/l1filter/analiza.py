import csv
# from matplotlib import pyplot as plt
import numpy as np
# from l1tf import l1tf, remove_outliers  - originalno bilo
from init import l1tf, remove_outliers
# dovoljno jedanput ucitati
import pandas as pd

first_data_line = 6100
last_data_line = 7101
last_data_column = 251
rbrDionice=1
delta_values = [1, 2.5, 4, 6, 8, 10, 25, 100, 250, 1000]

# uvoz podataka iz datoteke
with open('NYSE_prices_daily.csv') as f:  
    lines = list(csv.reader(f))
f.close()

data = {}
for rbrStupca in range(1, last_data_column):
   
    # odabir stupca (dionice) i raspona redaka koje proucavamo (velicina uzorka)
    x = pd.Series(np.asarray([float(e[rbrStupca]) for e in lines[first_data_line:last_data_line]]))
    # print(x[x.size-3], x[x.size-2], x[x.size-1])
    y = pd.Series(np.asarray([float(e[rbrStupca]) for e in lines[(last_data_line):(last_data_line+3)]]))
    #print(y[0], y[1])
    #racunanje prosjecne cijene promatrane dionice u zadnjih 5 dana promatranog razdoblja
    avgCijenaX = round(np.mean(np.asarray(x[(x.size-3) : x.size])),3)

    # racunanje prosjecne cijene promatrane dionice u iducem razdoblju
    avgCijenaY = round(np.mean(np.asarray(y)),3)
   
    # avgDayGrowthRate = round(((pow(avgCijenaY/avgCijenaX, 1/30) - 1) * 100),4)
    change = round((avgCijenaY/avgCijenaX -1), 3)
   
    line = str(avgCijenaX) + ',' + str(avgCijenaY) + ',' + str(change)
   
    # izdvajanje imena dionice iz cijele liste
    dionica = np.asarray(lines[0])[rbrStupca]
  
    # delta_values = [1, 2.5, 4, 6, 8, 10, 25, 100, 250, 1000]
    for delta in delta_values:
       filtered = l1tf(x, delta)
       m = []
       for j in range(x.size-4,x.size-1):   #ide od 996 do 999 - uzima se zadnja 3 podataka
           a = (filtered[j+1]/filtered[j] - 1) * 100
           m.append(a)
           sr_nagib = round(np.mean(m),4)  #pamtimo vrijednost, zaokruzeno na 4 decimale
       line = line + ',' + str(sr_nagib)
       del m
   
    data.update({dionica : line})
    print('obradena dionica br ' + ' ' + str(rbrDionice) + '. ' + dionica)
    rbrDionice+=1
    # print(line)
   
    del x
    del y
    del avgCijenaX
    del avgCijenaY
    del change
    del line
    del dionica

   
#for k in data:
 #  print(k + ',' + data[k])
 
#sorted_nagibi = sorted(nagibi.items(), key=lambda kv: kv[1], reverse = True)  #sortira dictionary
#print(sorted_nagibi) #problem formata ispisa 

#for i in cijene:
    #value = str(cijene[i]) + ',' + str(future[i])
    #cijene.update({i : value})
    #stock = str(i).replace('(', '').replace(')', '').replace('\'', '')
    #stock = stock.split(',')
    #indStock, stock_growth_rate = stock[0],stock[1]
    #price = cijene.get(indStock)
    #value = str(price) + ',' + stock_growth_rate.strip()
    #data.update({indStock : value})

#ispis rezultata u datoteku - potrebno jos ljepse formatirati linije
#f1 = open('c:/filip/fer/3.godina/projekt iz programske potpore/py-l1tf-master/l1tf/mojiPodaci/output_raspon_lambda4.csv',"w+")
#f1.write("%s\n" % ('dionica,past,future,stvarnaPromjena,l1,l2.5,l4,l5,l8,l10,l25,l100,l250,l1000'))
#for key in data:
 #    f1.write("%s\n" % (key + ',' + data[key]))
#f1.close()

#del m
del data

print('Izveden program!')
#plt.figure()
#plt.suptitle('Outlier detection algorithm changing the mad_factor parameter')

#for i, mad_factor in enumerate([1, 3]):
 #  plt.subplot(2,1,i+1)
 #  x_wo_outliers = remove_outliers(x_w_outliers, delta=1, mad_factor=mad_factor)
 #  plt.plot(x_w_outliers, label='Original data')
 #  plt.plot(x_wo_outliers, linewidth=5, label='Without outliers, mad_factor = %s' % mad_factor, alpha=0.5)
 #  plt.legend(loc='best')

#plt.show()


