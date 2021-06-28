import numpy as np
from matplotlib import pyplot as plt

plt.style.use("seaborn")

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

x_indexes = np.arange(len(ages_x))
width = 0.25

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850]

plt.bar(x_indexes - width, py_dev_y, width=width, label="Python Devs")

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823]

plt.bar(x_indexes, js_dev_y, width=width, label="JS Devs Salary")

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752]

plt.bar(x_indexes + width, dev_y, width=width, label="All Devs")

plt.legend()
plt.title("Developers Salary in USD")
plt.xlabel("Ages")
plt.ylabel("Salary in USD")

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.tight_layout()

plt.show()
