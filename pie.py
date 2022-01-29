from curses import start_color
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels= mylabels, startangle=45)
plt.show()
