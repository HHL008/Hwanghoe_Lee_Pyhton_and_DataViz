import matplotlib.pyplot as plt
import numpy as np

years = np.array([1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014])

wins = np.array([9, 12, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 37, 40, 49, 75, 68, 91, 90])

plt.bar(years, wins, width=1.3)
plt.xlabel("years")
plt.ylabel("Number of Wins")
plt.title("Wins for Canada", pad=20)

plt.show()