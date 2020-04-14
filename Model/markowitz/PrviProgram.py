import matplotlib.pyplot as plt
import numpy as np
# from l1filter import Proba
from plotly.graph_objs import *
# import cvxopt as opt
# from cvxopt import blas, solvers
# import pandas as pd


def insert_data():
    # prvi broj - lambda_range, drugi broj - broj_dionica
    data = [[0] * 250 for _ in range(6)]
    with open('c:/filip/fer/3.godina/6.semestar/završni rad/Model/data/Six_stocks_lambda1-250.txt', "r+") as f:
        line = f.readline()
        cnt = 0
        while line:
            line = line.replace("[", "").replace("]", "").replace(" ", "").replace("\n", "")
            ints_list = [int(i) for i in line.split(",")]
            data[cnt] = ints_list
            line = f.readline()
            cnt += 1
        f.close()
    return data


def plot_graph():
    plt.plot(np.transpose(data), markersize=1)  # alpha=.4
    plt.title('AEM, AEP, AET, AFG')
    plt.xlabel('lambda')
    plt.ylabel('sign')
    plt.show()


'''
data = insert_data()
print(type(data))
print(len(data))
for i in data:
    print(i)
del data

exit(0)
# '''