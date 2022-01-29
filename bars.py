import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A','B', 'C', 'D'])
y = np.array([200, 300, 400, 500])


plt.bar(x, y, color='hotpink', width=0.1)
plt.show()