from datetime import datetime
import pandas_datareader.data as web


def data_grabber(start, end, name):
    start = datetime.strptime(start, '%Y/%m/%d')
    end = datetime.strptime(end, '%Y/%m/%d')

    df = web.DataReader(name, 'yahoo', start, end)

    df.to_csv(name + '.csv')

    return name + '.csv'

