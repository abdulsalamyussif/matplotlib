from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 6, 9, 18])
yypoints = np.array([2, 9, 5, 9])
yyypoints = np.array([2, 8, 4])
#using notations at the end of points
plt.plot(ypoints, marker = 'o', ms=20, mec='hotpink', mfc= 'hotpink')
#using fmt or formated strings
plt.plot(yypoints, 'o:g')
plt.plot(yyypoints, 'D-.r')
plt.show()