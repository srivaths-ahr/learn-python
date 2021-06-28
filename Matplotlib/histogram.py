import numpy as np
from matplotlib import pyplot as plt

plt.style.use("ggplot")

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

bins = [10, 20, 30, 40, 50, 60]
plt.hist(ages_x, bins=bins, edgecolor="black")

mean_val = np.array(ages_x).mean()
color = "#000000"

plt.axvline(mean_val, color=color, label="Mean Age")

plt.legend()
plt.title("Developer Ages")
plt.xlabel("Ages")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
