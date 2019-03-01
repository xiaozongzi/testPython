import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# x = np.linspace(0, 10, 1000)
# y = np.sin(x)+1
# z = np.cos(x ** 2)+1
# m=np.tan(x)+1
# plt.figure(figsize=(8, 4))
# plt.plot(x, y, label='$\sin x+1$', color='red', linewidth=2)
# plt.plot(x, z, 'b--', label='$\cos x^2+1$')
# plt.plot(x, m, 'y--', label='$\ tan x+1$')
# plt.xlabel('Time(s) ')
# plt.ylabel('Volt')
# plt.title('A simple Example')
# plt.ylim(0,2.2)
# plt.legend()
# plt.show()

# n = np.linspace(1, 100, 100)
# y = (np.add(1, np.true_divide(1, n))) ** n
# plt.plot(n, y, 'b--', label='$\ n (1 + 1/n)^n$')
# plt.legend()
# plt.show()
# plt.plot(np.arange(10))
# plt.show()
# data=np.random.randn(30).cumsum()
# print(data)
from datetime import datetime

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

data = pd.read_csv('pydata-book/examples/spx.csv', index_col=0, parse_dates=True)
spx = data['SPX']

spx.plot(ax=ax, style='k-')

crisis_data = [
    (datetime(2007, 10, 11), 'Peak of bull market'),
    (datetime(2008, 3, 12), 'Bear Stearns Fails'),
    (datetime(2008, 9, 15), 'Lehman Bankruptcy')
]

for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 75),
                xytext=(date, spx.asof(date) + 225),
                arrowprops=dict(facecolor='black', headwidth=4, width=2,
                                headlength=4),
                horizontalalignment='left', verticalalignment='top')

# Zoom in on 2007-2010
ax.set_xlim(['1/1/2000', '1/1/2011'])
ax.set_ylim([600, 1800])

ax.set_title('Important dates in the 2008-2009 financial crisis')
plt.show()