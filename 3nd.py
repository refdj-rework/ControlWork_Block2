import numpy as np
import matplotlib.pyplot as plt #импортт библиотек

x = np.linspace(-np.pi, np.pi, 50) #координаты
y = x #координаты
z = np.cos(x) #координаты
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z) #координаты
plt.show() #вывод графика