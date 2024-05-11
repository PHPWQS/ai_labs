import matplotlib
import matplotlib.pyplot as plt
import numpy as np

""" configuration for matplotlib graphic interface that use pyQt5 """
matplotlib.use('Qt5Agg')
plt.xlabel("x")
plt.ylabel("y")

x_data = [1.4, 2.62, 2.83, 2.11, 1.64, 1.97, 2.46, 2.76, 1.87, 2.27]
y_data = [128, 179, 141, 166, 164, 183, 182, 165, 153, 192]

""" sum of all collection """
sums = {
  "x": 0, "x_2": 0, "x_3": 0, 
  "x_4": 0, "y": 0, "x_y": 0, "x_2_y": 0
}

sums["x"] = sum(x_data)
sums["x_2"] = sum(list(map(lambda i: pow(i, 2), x_data)))
sums["x_3"] = sum(list(map(lambda i: pow(i, 3), x_data)))
sums["x_4"] = sum(list(map(lambda i: pow(i, 4), x_data)))

for i in range(len(x_data)):
  sums["y"] += y_data[i]
  sums["x_y"] += x_data[i] * y_data[i]
  sums["x_2_y"] += pow(x_data[i], 2) * y_data[i]


""" calculate other parts """ 
l = np.array([
  [sums["x_4"], sums["x_3"], sums["x_2"]], 
  [sums["x_3"], sums["x_2"], sums["x"]], 
  [sums["x_2"], sums["x"], len(x_data)]
])
r = np.array([
  [sums["x_2_y"]], 
  [sums["x_y"]], 
  [sums["y"]]
])


# print(l)
# print(r)
x = np.linalg.solve(l, r)
[a, b, c] = [float(k[0]) for k in np.linalg.solve(l, r)]

new_x_data = []
new_y_data = []
x_state = 1.4

while x_state <= 2.83:
  new_y_data.append(a * pow(x_state, 2) + b * x_state + c)
  new_x_data.append(x_state)
  x_state += 0.1

plt.scatter(x_data, y_data, label = "points", color = "blue")
plt.plot(new_x_data, new_y_data, label = "line", color = "red")
plt.legend()
plt.show()