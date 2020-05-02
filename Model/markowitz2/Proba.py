import csv
import numpy as np
from pandas_wrapper import l1tf
import pandas as pd


def estimate_expected_returns(data):
    max_lambda = 1000
    stock_num = len(data[0])
    days_num = len(data)
    filtered_data = [[0] * max_lambda for _ in range(stock_num)]  # stock_num-1 ako zanemarujemo prvi stupac
    for col in range(1, stock_num+1):  # promijeniti u 0?
        x = pd.Series(np.asarray([float(e[col]) for e in data[1:days_num]]))
        for delta in range(1, max_lambda + 1):
            filtered_stock = l1tf(x, delta)
            slope = filtered_stock[filtered_stock.size - 1] / filtered_stock[filter_stock.size - 2]
            if slope > 1:
                filtered_data[col-1][delta - 1] = 1
            elif slope < 1:
                filtered_data[col-1][delta - 1] = -1
            else:
                filtered_data[col-1][delta - 1] = 0
    returns = []
    for row in filtered_data:
        returns.append(np.mean(row))
    del filtered_data
    return returns


with open('data1.csv') as f:
    podaci = list(csv.reader(f))
f.close()

mean_returns = estimate_expected_returns(podaci)
print("Skalirani povrati")
print(mean_returns)

exit(0)
