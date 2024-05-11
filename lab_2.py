import matplotlib
import matplotlib.pyplot as plt
import numpy as np

""" configuration for matplotlib graphic interface that use pyQt5 """
matplotlib.use('Qt5Agg')
plt.xlabel("x")
plt.ylabel("y")

x_data = np.array([i for i in range(1, 11)])
y_data = np.array([7, 8, 15, 20, 32, 42, 60, 100, 120, 220])

sums = { "x": 0, "x_2": 0, "lny": 0, "x_lny": 0 }

sums["x"] = sum(x_data)
sums["x_2"] = sum(list(map(lambda i: pow(i, 2), x_data)))
sums["lny"] = sum(list(map(lambda i: np.log(i), y_data)))

for i in range(len(x_data)):
  sums["x_lny"] += x_data[i] * np.log(y_data[i])

l = np.array([
  [sums["x_2"], sums["x"]],
  [sums["x"], len(x_data)]
])
r = np.array([
  [sums["x_lny"]], [sums["lny"]]
])

[a, B] = [float(k[0]) for k in np.linalg.solve(l, r)]
b = pow(np.e, B)

new_x_data = []
new_y_data = []
x_state = 1

while x_state <= 10:
  new_y_data.append(b * pow(np.e, a * x_state))
  new_x_data.append(x_state)
  x_state += 1

plt.scatter(x_data, y_data, label = "points", color = "blue")
plt.plot(new_x_data, new_y_data, label = "line", color = "red")
plt.legend()
plt.show()