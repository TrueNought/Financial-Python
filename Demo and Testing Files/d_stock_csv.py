import datetime as dt
import pandas_datareader.data as web

start = dt.datetime(2016, 1, 1)
end = dt.datetime.now()

df = web.DataReader('TSLA', 'yahoo', start, end)

df.to_csv('tesla.csv')