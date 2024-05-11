import matplotlib
import matplotlib.pyplot as plt
import numpy as np

""" configuration for matplotlib graphic interface that use pyQt5 """
matplotlib.use('Qt5Agg')
plt.xlabel("x")
plt.ylabel("y")

x_data = np.array([i for i in range(1, 11)])
y_data = np.array([70, 30, 20, 25, 17, 15, 12.9, 12.9, 11.7, 11.2])

sums = { "1/x_2": 0, "1/x": 0, "y/x": 0, "y": 0 }

""" sum of collection """
for i in range(10):
  sums["1/x_2"] += 1/pow(x_data[i], 2)
  sums["1/x"] += 1/x_data[i]
  sums["y/x"] += y_data[i]/x_data[i]
  sums["y"] += y_data[i]

""" calculate other parts """
l = np.array([[sums["1/x_2"], sums["1/x"]], [sums["1/x"], len(x_data)]])
r = np.array([[sums["y/x"]], [sums["y"]]])

[a, b] = [float(k[0]) for k in np.linalg.solve(l, r)]

x_state = 1
new_x_data = []
new_y_data = []

while x_state <= 10:
  state = (a / x_state) + b
  new_y_data.append(state)
  new_x_data.append(x_state)

  x_state += 0.1

plt.scatter(x_data, y_data, color = "blue", label = "points")
plt.plot(new_x_data, new_y_data, color="red", label = "line")
plt.legend()

plt.show()