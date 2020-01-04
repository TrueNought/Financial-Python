import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from pandas.plotting import register_matplotlib_converters
from data_to_csv import data_grabber


def read_csv(file):
    # Read data from the csv file, and set date as the index.
    df = pd.read_csv(file, parse_dates=True, index_col=0)

    # Creates new columns that shows the 20-day and 100-day moving average of the stock.
    df['20MA'] = df['Adj Close'].rolling(window=20, min_periods=0).mean()
    df['100MA'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

    return df


def graph_data(df, name):
    # Create 2 separate subplots to plot 2 graphs
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=4, colspan=1)
    ax2 = plt.subplot2grid((6, 1), (4, 0), rowspan=2, colspan=1, sharex=ax1)

    ax1.plot(df.index, df['Adj Close'], label='Adjusted Close')
    ax1.plot(df.index, df['20MA'], label='20MA')
    ax1.plot(df.index, df['100MA'], label='100MA')
    ax1.legend()

    ax2.bar(df.index, df['Volume'])
    ax2.set_title('Volume')

    plt.suptitle(name + '\'s Stocks')
    plt.tight_layout()
    plt.subplots_adjust(top=0.95)

    plt.show()


def main():
    register_matplotlib_converters()

    style.use('ggplot')

    # Optimizes the Python console's output of data when we are printing.
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    print(
        "Welcome to a program that lets you check stock data! Note that a data file will be created locally during "
        "the process")
    ticker = input("Enter the stock ticker symbol for any company:\n")
    start_date = input("Enter the starting date in YYYY/MM/DD format:\n")
    end_date = input("Enter the ending date in YYYY/MM/DD format:\n")

    csv_file = data_grabber(start_date, end_date, ticker)
    data_frame = read_csv(csv_file)

    print(data_frame.describe())

    graph_data(data_frame, ticker)


if __name__ == '__main__':
    main()
