# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:32:31 2020

@author: filip
"""

import csv
from matplotlib import pyplot as plt 
import numpy as np
#from l1tf import l1tf, remove_outliers  - originalno bilo
from __init__ import l1tf, remove_outliers #dovoljno jedanput ucitati
import pandas as pd

first_data_line = 1000
last_data_line = 2001
first_data_column = 248
last_data_column = 249
#uvoz podataka iz datoteke
with open('NYSE_prices_daily.csv') as f:  
    lines = list(csv.reader(f))
f.close()

data = {}
for rbrStupca in range(first_data_column, last_data_column):
   
   #odabir stupca (dionice) i raspona redaka koje proucavamo (velicina uzorka)
   x = pd.Series(np.asarray([float(e[rbrStupca]) for e in lines[first_data_line:last_data_line]]))  
   z = pd.Series(np.asarray([float(e[rbrStupca]) for e in lines[first_data_line:last_data_line+200]])) 
   #y = pd.Series(np.asarray([float(e[rbrStupca]) for e in lines[(last_data_line+20):(last_data_line+30)]])) 
   
   #racunanje prosjecne cijene promatrane dionice u zadnjih 10 dana promatranog razdoblja
   #avgCijenaX = round(np.mean(np.asarray(x[last_data_line-10 : last_data_line])),3)

   #racunanje prosjecne cijene promatrane dionice u iducem razdoblju
   #avgCijenaY = round(np.mean(np.asarray(y)),3)
   
   #avgDayGrowthRate = round(((pow(avgCijenaY/avgCijenaX, 1/30) - 1) * 100),4)
   
   #line = str(avgCijenaX) + ',' + str(avgCijenaY) + ',' + str(avgDayGrowthRate)
   
   #izdvajanje imena dionice iz cijele liste
   dionica = np.asarray(lines[0])[rbrStupca]
  
   #outliers_percentaje = 0.2
   #outliers = np.random.random(len(x)) < outliers_percentaje 
   #x_w_outliers = x.copy()
   #x_w_outliers[outliers] = (np.random.random(outliers.sum()) - 0.5) * 2 + x[outliers]

   #plt.figure()  # vratiti
#plt.suptitle('Different fits by changing the $\delta$ parameter')
# delta ovakvim tipom for petlje poprima iznose 1 i 10
   #for i, delta in enumerate([1, 10]): #maknuti i
    #plt.subplot(2,1,i+1)
   delta_values = [1, 2.5, 4, 6, 8, 10, 25, 100, 250, 1000]
   for delta in delta_values:
  # for delta in range(1, 2000, 200):     
      filtered = l1tf(x, delta)
      plt.figure()
      plt.subplot(1,1,1)
      plt.plot(z, label=dionica)
      plt.plot(z, label='Original data')
      plt.plot(filtered, linewidth=5, label='Filtered, $\delta$ = %s' % delta, alpha=0.5)
      plt.legend(loc='best')     

      #m = []
      #for j in range(989,999):   #ide od 989 do 999 - uzima se zadnjih 10 podataka
       #   a = (filtered[j+1]/filtered[j] - 1) * 100
        #  m.append(a)
         # sr_nagib = round(np.mean(m),4)  #pamtimo vrijednost, zaokruzeno na 4 decimale
          
      #line = line + ',' + str(sr_nagib)
   
   #data.update({dionica : line})   
   #print('obradena dionica' + ' ' + dionica)
#for j in data:
 #  print(j + ',' + data[j])
 
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
#f1 = open('output.csv',"w+")
#f1.write("%s\n" % ('dionica,past,future,stvarnaPromjena,l1,l3,l5,l7,l9,l11,l13,l15,l17,l19'))
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


