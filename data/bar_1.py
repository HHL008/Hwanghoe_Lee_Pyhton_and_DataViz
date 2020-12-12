import matplotlib.pyplot as plt
import numpy as np

country = np.array(["Norway", "United States", "Germany", "Russia", "Canada"])
wins = np.array([457, 653, 360, 263, 625])

plt.bar(country, wins)
plt.xlabel("Country")
plt.ylabel("Number of Wins")
plt.title("Comparison with other Country", pad=20)

plt.show()