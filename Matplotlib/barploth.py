import numpy as np
from matplotlib import pyplot as plt

plt.style.use("seaborn")

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850]

plt.barh(ages_x, py_dev_y, label="Python Devs")

plt.legend()
plt.title("Developers Salary in USD")
plt.xlabel("Ages")
plt.ylabel("Salary in USD")
plt.tight_layout()

plt.show()
