# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 23:41:04 2021

@author: madhawa
"""

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection = '3d')
# Make data.
X = np.arange(1,11, 1)
Y = np.arange(0.2, 1.6, 0.1)
X, Y = np.meshgrid(X, Y)
Z1 = np.array([0.8845,0.8825,0.8922,0.8863,0.8863,0.8886,0.8816,0.8888,0.8825,0.8898,0.8254,0.8165,0.8266,0.8258,0.8266,0.8261,0.8246,0.8252,0.8244,0.8219,0.7677,0.7629,0.7665,0.7655,0.7669,0.7643,0.7610,0.7627,0.7623,0.7687,0.7330,0.7319,0.7350,0.7393,0.7320,0.7356,0.7407,0.7381,0.7390,0.7362,0.7305,0.7362,0.7337,0.7367,0.7294,0.7299,0.7277,0.7326,0.7323,0.7330,0.7233,0.7238,0.7248,0.7241,0.7243,0.7211,0.7244,0.7264,0.7252,0.7245,0.7276,0.7254,0.7223,0.7255,0.7258,0.7231,0.7217,0.7227,0.7270,0.7242,0.7215,0.7210,0.7238,0.7227,0.7221,0.7210,0.7188,0.7205,0.7215,0.7197,0.7157,0.7173,0.7183,0.7194,0.7158,0.7174,0.7166,0.7159,0.7155,0.7154,0.7154,0.7135,0.7136,0.7154,0.7136,0.7176,0.7137,0.7135,0.7166,0.7153,0.7140,0.7162,0.7125,0.7127,0.7134,0.7125,0.7135,0.7138,0.7152,0.7164,0.7140,0.7142,0.7139,0.7139,0.7139,0.7135,0.7164,0.7159,0.7132,0.7140,0.7141,0.7124,0.7148,0.7125,0.7120,0.7120,0.7147,0.7127,0.7133,0.7141,0.7113,0.7149,0.7111,0.7121,0.7114,0.7129,0.7111,0.7156,0.7133,0.7106 ])
Z=Z1.reshape(14,10)



# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.set_zlim3d(np.min(Z1,0),np.max(Z1,0))
ax.set_zlabel("Accuracy")


ax.view_init(40,30)
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()