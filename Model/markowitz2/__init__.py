import numpy as np

table1 = [1, 2, 3]
table2 = [1, 2, 3]
table = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(np.cov(table1, table2))
print("-----------")
print(np.cov(table))
