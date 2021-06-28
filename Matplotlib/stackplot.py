from matplotlib import pyplot as plt

plt.style.use("seaborn")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p1 = [1, 1, 1, 2, 2, 3, 4, 4, 8]
p2 = [0, 1, 1, 1, 1, 1, 1, 1, 1]
p3 = [0, 0, 1, 2, 3, 4, 5, 6, 7]

labels = ["Player 1", "Player 2", "Player 3"]

plt.stackplot(minutes, p1, p2, p3, labels=labels)

plt.legend(loc="upper left")
plt.title("Developers Salary in USD")
plt.xlabel("Minutes")
plt.ylabel("Goals")
plt.tight_layout()
plt.show()
