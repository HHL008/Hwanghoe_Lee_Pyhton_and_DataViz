import matplotlib.pyplot as plt
import numpy as np

values = [107, 315, 203]
labels = ["Bronze", "Gold", "Silver"]
colors = ["#cd7f32", "gold", "silver"]

plt.pie(values, labels=labels, colors=colors, shadow = True)
plt.title("Medal Statistics for Canada", pad=20)

plt.show()
