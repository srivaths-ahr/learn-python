from matplotlib import pyplot as plt

plt.style.use("seaborn")

slices = [60, 40, 20, 10, 90]
labels = ["Sixty", "Forty", "Extra1", "Extra2", "Extra3"]
colors = ["blue", "green", "red", "yellow", "orange"]
explode = [0, 0.1, 0, 0, 0]

plt.pie(slices, labels=labels,
        colors=colors,
        explode=explode,
        startangle=260,
        wedgeprops={"edgecolor": "black"},
        autopct='%1.1f%%'
        )

plt.legend(loc="upper left")
plt.title("Developers Salary in USD")

plt.tight_layout()
plt.show()
