import pandas as pd

from pricelevels.cluster import ZigZagClusterLevels
from pricelevels.visualization.levels_with_zigzag import plot_with_pivots

df = pd.read_csv('sample.txt')

zig_zag_percent = 0.75

zl = ZigZagClusterLevels(peak_percent_delta=zig_zag_percent, merge_distance=None,
                         merge_percent=0.4, min_bars_between_peaks=20, peaks='All')

zl.fit(df)

plot_with_pivots(df['Close'].values, zl.levels, zig_zag_percent)  # in case you want to display chart
# plot_with_pivots(df['Close'].values, zl.levels,  zig_zag_percent, path='image.png')  # in case you want to save chart to  image
