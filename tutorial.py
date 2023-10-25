import numpy as np
import matplotlib.pyplot as plt

years = [2015 + x for x in range(8)]
weights = [78, 79, 80, 81, 80, 79, 80, 82]

plt.plot(years, weights, lw=3, linestyle=":")

plt.show()
