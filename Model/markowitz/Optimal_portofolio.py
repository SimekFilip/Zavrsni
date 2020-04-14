import numpy as np
import chart_studio as plt
import cvxopt as opt
from cvxopt import blas, solvers
from markowitz import PrviProgram


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
    x1 = np.sqrt(m1[2] / m1[0])
    # CALCULATE THE OPTIMAL PORTFOLIO
    wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']
    return np.asarray(wt), returns1, risks1


weights, returns, risks = optimal_portfolio(PrviProgram.insert_data())  #return_vec

fig = plt.figure()
plt.plot(stds, means, 'o')
plt.ylabel('mean')
plt.xlabel('std')
plt.plot(risks, returns, 'y-o')
plt.show()
#py.iplot_mpl(fig, filename='efficient_frontier', strip_style=True)