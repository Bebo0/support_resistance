import matplotlib.dates as mdates
import pandas as pd
import mplfinance as mpf


def plot_levels_on_candlestick(df, levels, only_good=False, path=None,
                               formatter=mdates.DateFormatter('%y-%m-%d %H:%M:%S')):
    ohlc = df[['Datetime', 'Open', 'High', 'Low', 'Close']].copy()
    ohlc["Datetime"] = pd.to_datetime(ohlc['Datetime'])
    ohlc["Datetime"] = ohlc["Datetime"].apply(lambda x: mdates.date2num(x))
    ohlc.index = pd.DatetimeIndex(df['Datetime'])
    levels_prices = [l['price'] for l in levels]
    mpf.plot(ohlc, hlines=levels_prices, type='candle', style='charles')
    mpf.show()
    # f1, ax = plt.subplots(figsize=(10, 5))
    # mpf.plot(ax,
    #                   closes=ohlc.Close.values,
    #                   opens=ohlc.Open.values,
    #                   highs=ohlc.High.values,
    #                   lows=ohlc.Low.values,
    #                   colordown='red',
    #                   colorup='green'
    #                   )

    # _plot_levels(ax, levels, only_good)

    # if path:
    #     plt.savefig(path)
    # else:
    #     plt.show()
    # plt.close()
