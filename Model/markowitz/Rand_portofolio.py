import numpy as np
import matplotlib.pyplot as plt
# import chart_studio.plotly as py
import cvxopt as opt
from cvxopt import blas, solvers
from markowitz import Rand_weights
from markowitz import PrviProgram
from numpy.polynomial import Polynomial as P


def random_portfolio(returns1):
    # Returns the mean and standard deviation of returns for a random portfolio
    p = np.asmatrix(np.mean(returns1, axis=1))
    w = np.asmatrix(Rand_weights.rand_weights(len(returns1)))  # treba mi broj redaka - len
    C = np.asmatrix(np.cov(returns1))

    mu = w * p.T
    sigma = np.sqrt(w * C * w.T)
    # This recursion reduces outliers to keep plots pretty
    if sigma > 2:
        return random_portfolio(returns1)
    return mu, sigma


data = PrviProgram.insert_data()
## NUMBER OF ASSETS
n_assets = 4
## NUMBER OF OBSERVATIONS
n_obs = 1000
# data = np.random.randn(n_assets, n_obs)

n_portfolios = 500
means, stds = np.column_stack([
    random_portfolio(data)  # return_vec je data
    for i in range(n_portfolios)
])


def optimal_portfolio(returns1):
    n = len(returns1)
    returns1 = np.asmatrix(returns1)

    N = 100
    mus = [10**(5.0 * t/N - 1.0) for t in range(N)]

    # Convert to cvxopt matrices
    S = opt.matrix(np.cov(returns1))
    pbar = opt.matrix(np.mean(returns1, axis=1))

    # Create constraint matrices
    G = -opt.matrix(np.eye(n))  # negative n x n identity matrix
    h = opt.matrix(0.0, (n, 1))
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)

    # Calculate efficient frontier weights using quadratic programming
    portfolios = [solvers.qp(mu * S, -pbar, G, h, A, b)['x']
                  for mu in mus]
    # CALCULATE RISKS AND RETURNS FOR FRONTIER
    returns1 = [blas.dot(pbar, x) for x in portfolios]
    risks1 = [np.sqrt(blas.dot(x, S * x)) for x in portfolios]
    # CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
    m1 = np.polyfit(returns1, risks1, 2)
    p = P.fit(returns1, risks1, 2)
    #x1 = np.sqrt(m1[2] / m1[0])
    # CALCULATE THE OPTIMAL PORTFOLIO
    #wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']
    #return np.asarray(wt), returns1, risks1
    return returns1, risks1


# weights, returns, risks = optimal_portfolio(data)  # return_vec
# optimal_portfolio(data)
returns, risks = optimal_portfolio(data)
del data
# fig = plt.figure()
plt.plot(stds, means, 'o')
plt.ylabel('mean')
plt.xlabel('std')
# plt.plot(risks, returns, 'y-o')
plt.title("Efficient Frontier - my all data")
plt.show()
# py.iplot_mpl(fig, filename='efficient_frontier', strip_style=True)


'''
# sve radi korektno
print(means)
print("--------")
print(stds)
print(weights)
print(returns)
print(risks)
'''

'''
fig = plt.figure()
plt.plot(stds, means, 'o', markersize=5)
plt.xlabel('std')
plt.ylabel('mean')
plt.title('Mean and standard deviation of returns of randomly generated portfolios')
plt.show()
'''
