import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from markowitz import PrviProgram


def portfolio_annualised_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns * weights) * 252
    r1 = np.asmatrix(weights)  # dodano
    r2 = np.dot(cov_matrix, np.transpose(np.asmatrix(weights)))  # dodano
    std = np.sqrt(np.dot(r1, r2)) * np.sqrt(252)  # dodano
    # std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    return std, returns


def random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate):
    results = np.zeros((3, num_portfolios))
    weights_record = []
    for i in range(num_portfolios):  # num_portfolios
        weights = np.random.random(10)
        weights /= np.sum(weights)
        weights_record.append(weights)
        portfolio_std_dev, portfolio_return = portfolio_annualised_performance(weights, mean_returns, cov_matrix)
        results[0, i] = portfolio_std_dev
        results[1, i] = portfolio_return
        results[2, i] = (portfolio_return - risk_free_rate) / portfolio_std_dev
    return results, weights_record


def display_simulated_ef_with_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate):
    results, weights = random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate)

    table = pd.DataFrame([[0.998, -0.548, 1.0, 1.0, 1.0, -0.838, -0.308, 0.998, 0.994, -0.926]]) # dodano
    table.columns = ['AET', 'AFG', 'AFL', 'AGN', 'AIG', 'AIN', 'AIR', 'AIT', 'AJG', 'AJRD'] # dodano

    max_sharpe_idx = np.argmax(results[2])
    sdp, rp = results[0, max_sharpe_idx], results[1, max_sharpe_idx]
    max_sharpe_allocation = pd.DataFrame(weights[max_sharpe_idx], index=table.columns, columns=['allocation'])
    max_sharpe_allocation.allocation = [round(i * 100, 2) for i in max_sharpe_allocation.allocation]
    max_sharpe_allocation = max_sharpe_allocation.T

    min_vol_idx = np.argmin(results[0])
    sdp_min, rp_min = results[0, min_vol_idx], results[1, min_vol_idx]
    min_vol_allocation = pd.DataFrame(weights[min_vol_idx], index=table.columns, columns=['allocation'])
    min_vol_allocation.allocation = [round(i * 100, 2) for i in min_vol_allocation.allocation]
    min_vol_allocation = min_vol_allocation.T

    print("-" * 80)
    print("Maximum Sharpe Ratio Portfolio Allocation\n")
    print("Annualised Return:", round(rp, 2))
    print("Annualised Volatility:", round(sdp, 2))
    print("\n")
    print(max_sharpe_allocation)
    print("-" * 80)
    print("Minimum Volatility Portfolio Allocation\n")
    print("Annualised Return:", round(rp_min, 2))
    print("Annualised Volatility:", round(sdp_min, 2))
    print("\n")
    print(min_vol_allocation)

    plt.figure(figsize=(10, 7))
    plt.scatter(results[0, :], results[1, :], c=results[2, :], cmap='YlGnBu', marker='o', s=10, alpha=0.3)
    plt.colorbar()
    plt.scatter(sdp, rp, marker='*', color='r', s=500, label='Maximum Sharpe ratio')
    # plt.scatter(sdp_min, rp_min, marker='*', color='g', s=500, label='Minimum volatility')
    plt.title('Simulated Portfolio Optimization based on Efficient Frontier')
    plt.xlabel('annualised volatility')
    plt.ylabel('annualised returns')
    plt.legend(labelspacing=0.8)
    plt.show()


def estimate_expected_returns(data):
    pr = []
    for row in data:
        pr.append(np.mean(row))
    return pr


# returns = table.pct_change()  # izbaceno
# mean_returns = returns.mean()  # izbaceno

data = PrviProgram.insert_data()  # dodano - ucitavanje podataka
mean_returns = estimate_expected_returns(data)  # dodano - racunanje skaliranih povrata
print("Skalirani povrati")
print(mean_returns)

# cov_matrix = returns.cov() # izbaceno
cov_matrix = np.asmatrix(np.cov(data))  # dodano - racunanje matrice kovarijance

num_portfolios = 1000  # pocetno 25000
risk_free_rate = 0.0178  # utjece samo na Sharpe ratio?

# results, weights_record = random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate)

display_simulated_ef_with_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate)

'''
df = data.set_index('date')
table = df.pivot(columns='ticker')
# By specifying col[1] in below list comprehension
# You can select the stock names under multi-level column
table.columns = [col[1] for col in table.columns]
table.head()
'''

