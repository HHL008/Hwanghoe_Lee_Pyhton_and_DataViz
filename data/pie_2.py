import matplotlib.pyplot as plt
import numpy as np

values = [457, 653, 360, 625, 263]
labels = ["Norway", "United States", "Germany", "Canada", "Russia"]

plt.pie(values, labels=labels, shadow = True)
plt.title("Comparison with other Country", pad=20)

plt.show()
