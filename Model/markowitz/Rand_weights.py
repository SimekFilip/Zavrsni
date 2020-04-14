import numpy as np


def rand_weights(n):
    # Produces n random weights that sum to 1 '''
    k = np.random.rand(n)
    return k / sum(k)


#n_assets = 5
#print(rand_weights(n_assets))
#print(rand_weights(n_assets))

