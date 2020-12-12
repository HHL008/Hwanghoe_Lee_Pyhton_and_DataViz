import matplotlib.pyplot as plt
import numpy as np

Medal = np.array(["Bronze", "Silver", "Gold"])
wins = np.array([107, 203, 315])

plt.plot(Medal, wins, color="grey")
plt.xlabel("Medal")
plt.ylabel("Number of Wins")
plt.title("Medal Statistics for Canada", pad=20)

plt.show()
