import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt

data = pandas.read_csv("C:\\data\\cost-revenue-clean.csv")

data.describe()

x = DataFrame(data, columns=['production_budget_usd'])
y = DataFrame(data, columns=['worldwide_gross_usd'])

plt.figure(figsize=(10, 6))
plt.scatter(x, y)  # , alpha=0.3)
plt.title('Film Making Cost vs Global Revenue')
plt.xlabel('Production Budget in $')
plt.ylabel('Worldwide Gross in $')
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()



