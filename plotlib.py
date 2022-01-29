import matplotlib.pyplot as plt
import numpy as np

#xpoints = np.array([0, 6])
#ypoints = np.array([0, 250])
#to plot and make a line
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
xxpoints = np.array([3, 4, 8, 9, 5])
yypoints = np.array([2, 7, 2, 7, 1])
tpoints = np.array([2, 4, 6])
bpoints = np.array([8, 16, 8])
xblinepoints = np.array([2, 6])
yblinepoints = np.array([8, 8])

#.plot(xxpoints, yypoints)
plt.plot(tpoints, bpoints)
plt.plot(xblinepoints, yblinepoints)
#to plot only the raw points
#plt.plot(xpoints, ypoints, 'o')


plt.show()



