# import csv
import matplotlib.pyplot as plt
# import numpy as np
# import cvxopt as opt
# from cvxopt import blas, solvers
# import pandas as pd

#data = [[0] * 50 for _ in range(5)]
data = []
with open('c:/filip/fer/3.godina/6.semestar/završni rad/output.txt', "r+") as f:
    line = f.readline()
    while line:
        line = line.replace("[", "").replace("]", "").replace(" ", "").replace("\n", "")
        ints_list = [int(i) for i in line.split(",")]
        data.append(ints_list)
        line = f.readline()
f.close()

for i in data:
    print(i)

plt.plot(data[0], 'ro', markersize=2)
plt.xlabel('lambda')
plt.ylabel('sign')
plt.title('ABX stock')
plt.show()

exit(0)
