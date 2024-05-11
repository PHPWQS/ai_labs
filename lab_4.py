import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

""" configuration for matplotlib graphic interface that use pyQt5 """
matplotlib.use('Qt5Agg')
plt.xlabel("x")
plt.ylabel("y")

x_data = np.array([9, 12, 16, 17,  18, 23, 26, 27, 28, 29, 31, 33])
y_data = np.array([1570, 1676, 1188, 1188, 1389, 1261, 1231, 1074, 1179, 1071, 1097, 909])

sums = { "lnx": 0, "lny": 0, "lnx_2": 0, "lnx_lny": 0 }

""" sum of all collection """
sums["lnx"] = sum(list(map(lambda i: math.log(i), x_data)))
sums["lny"] = sum(list(map(lambda i: math.log(i), y_data)))
sums["lnx_2"] = sum(list(map(lambda i: pow(math.log(i), 2), x_data)))

for i in range(len(y_data)):
  sums["lnx_lny"] += x_data[i] * y_data[i]

""" calculate the other parts"""
l = np.array([[len(x_data), sums["lnx"]], [sums["lnx"], sums["lnx_lny"]]])
r = np.array([[sums["lny"]], [sums["lnx_lny"]]])

[A, b] = [float(k[0]) for k in np.linalg.solve(l, r)]
a = pow(math.e, A)

new_x_data = []
new_y_data = []
x_state = 9

while x_state <= 33:
  new_y_data.append(a * pow(x_state, b))
  new_x_data.append(x_state)
  x_state += 0.1

plt.scatter(x_data, y_data, color ="blue", label = "points")
plt.plot(new_x_data, new_y_data, color = "red", label = "line")
plt.legend()

plt.show()