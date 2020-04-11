import numpy as np
import matplotlib.pyplot as plt
a = np.array([[5, 4], [3, 2]])
print(a.T)

data = [[0] * 5 for _ in range(2)]
data[0] = [0, 1, 2, 3, 4]
data[1] = [2, 3, 4, 5, 6]

for i in data:
    print(i)

plt.plot(np.transpose(data), alpha=.4)
plt.show()


# print(data[0].T)
# np.transpose(data)
exit(0)
