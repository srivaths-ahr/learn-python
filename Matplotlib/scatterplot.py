from matplotlib import pyplot as plt
import pandas as pd
import random

plt.style.use("seaborn")

df = pd.read_csv("2019-05-31-data.csv")
view_count = df['view_count']
likes = df['likes']
ratio = df['ratio']

color_maps = [
    'viridis', 'plasma', 'inferno', 'magma', 'cividis',
    'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
    'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
    'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
    'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
    'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
    'hot', 'afmhot', 'gist_heat', 'copper',
    'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
    'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',
    'twilight', 'twilight_shifted', 'hsv',
    'Pastel1', 'Pastel2', 'Paired', 'Accent',
    'Dark2', 'Set1', 'Set2', 'Set3',
    'tab10', 'tab20', 'tab20b', 'tab20c',
    'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
    'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
    'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'
]
color_map = random.choice(color_maps)
print("Chosen ColorMap = ", color_map)

plt.scatter(view_count, likes, c=ratio, cmap=color_map, edgecolors="black", linewidth=1, alpha=0.75)

plt.xscale('log')
plt.yscale('log')

c_bar = plt.colorbar()
c_bar.set_label('Satisfaction')

plt.title("Trending Youtube Videos")
plt.xlabel("View Count")
plt.ylabel("Total Likes")

plt.tight_layout()
plt.show()
