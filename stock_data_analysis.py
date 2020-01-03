import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

style.use('ggplot')

# Optimizes the Python console's output of data when we are printing.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Read data from the csv file, and set date as the index.
ts = pd.read_csv('tesla.csv', parse_dates=True, index_col=0)

# Creates a new column that shows the 100 day moving average of the stock.
ts['100MA'] = ts['Adj Close'].rolling(window=100, min_periods=0).mean()

# Let's say we wanted to only look at the stock information in 2019,
ts_2019 = ts.loc['2019-01-01':'2019-12-31']

print(ts_2019.head())
print(ts_2019.shape)
print(ts_2019.describe())

# Create 2 separate subplots to plot 2 graphs
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=4, colspan=1)
ax2 = plt.subplot2grid((6, 1), (4, 0), rowspan=2, colspan=1, sharex=ax1)

ax1.plot(ts_2019.index, ts_2019['Adj Close'], label='Adjusted Close')
ax1.plot(ts_2019.index, ts_2019['100MA'], label='100MA')
ax1.legend()

ax2.bar(ts_2019.index, ts_2019['Volume'])
ax2.set_title('Volume')

plt.suptitle('Telsa\'s Stocks in 2019')
plt.tight_layout()
plt.subplots_adjust(top=0.95)

plt.show()


