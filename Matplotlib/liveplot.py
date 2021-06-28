from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import pandas as pd
import random


def animate(i):
    df = pd.read_csv("data.csv")
    x_values = df['x_value']
    y1_values = df['total_1']
    y2_values = df['total_2']

    plt.cla()
    plt.plot(x_values, y1_values, label="Channel 1")
    plt.plot(x_values, y2_values, label="Channel 2")
    plt.legend(loc="upper left")


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.style.use("seaborn")
plt.tight_layout()
plt.show()
