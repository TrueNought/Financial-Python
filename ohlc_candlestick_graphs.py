import pandas as pd
import mplfinance as mpf

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

ts = pd.read_csv('tesla.csv', index_col=0, parse_dates=True)
ts_2019_12 = ts.loc['2019-12-01':'2019-12-31']

mpf.plot(ts_2019_12, type='candle', mav=5, volume=True)

