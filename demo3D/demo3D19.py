import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#np.random.seed(0)  # For reproducibility
"""x = np.random.uniform(-5, 5, 1000)
y = np.random.uniform(-5, 5, 1000)
z = x**2 + y**2
"""
m = []
b = []
z = []

x = [0.0, 1.01, 2.02, 3.03, 4.04, 5.05, 6.06, 7.07, 8.08, 9.09, 10.10, 11.11, 12.12, 13.13, 14.14, 15.15, 16.16, 17.17, 18.18, 19.19, 20.20, 21.21, 22.22, 23.23, 24.24, 25.25, 26.26, 27.27, 28.28, 29.29, 30.30, 31.31, 32.32, 33.33, 34.34, 35.35, 36.36, 37.37, 38.38, 39.39, 40.40, 41.41, 42.42, 43.43, 44.44, 45.45, 46.46, 47.47, 48.48, 49.49, 50.50, 51.51, 52.52, 53.53, 54.54, 55.55, 56.56, 57.57, 58.58, 59.59, 60.60, 61.61, 62.62, 63.63, 64.64, 65.65, 66.66, 67.67, 68.68, 69.69, 70.70, 71.71, 72.72, 73.73, 74.74, 75.75, 76.76, 77.77, 78.78, 79.79, 80.80, 81.81, 82.82, 83.83, 84.84, 85.85, 86.86, 87.87, 88.88, 89.89, 90.90, 91.91, 92.92, 93.93, 94.94, 95.95, 96.96, 97.97, 98.98, 100.0]
y = [1.0, 3.23, 13.19, 17.51, 21.69, 20.00, 23.18, 28.94, 26.93, 31.20, 37.86, 45.04, 52.88, 30.96, 51.22, 51.12, 62.19, 62.30, 63.52, 72.42, 52.36, 65.95, 59.65, 58.01, 69.27, 90.95, 72.99, 89.39, 80.32, 77.01, 87.00, 93.60, 101.98, 87.82, 104.63, 109.14, 107.64, 105.52, 114.94, 126.65, 146.31, 127.82, 123.13, 124.87, 131.40, 136.43, 120.46, 140.10, 128.95, 151.84, 146.57, 134.42, 114.59, 146.12, 158.03, 140.11, 154.87, 151.58, 146.85, 164.07, 173.59, 171.39, 153.15, 170.57, 174.79, 171.12, 180.50, 182.32, 192.56, 159.98, 204.06, 201.41, 201.39, 211.08, 212.52, 201.44, 208.91, 212.37, 213.41, 209.81, 205.79, 222.62, 230.73, 216.20, 229.31, 231.18, 242.33, 238.11, 229.95, 238.34, 231.81, 262.22, 233.10, 267.21, 242.85, 253.29, 253.34, 262.84, 265.50, 264.51]

def abs_error (m, b, x, y):
    total = 0
    for i in range(len(x)):
        total += 0.5*(m*x[i] + b - y[i])**2
    return (total/len(x))

for val1 in range (0,100):
    for val2 in range (0,100):
        val1new = val1/10
        val2new = val2/10
        m.append (val1new)
        b.append (val2new)
        z.append (abs_error (val1new, val2new, x, y))
print (m)
print(b)
print(z)


m_arr = np.array(m)
b_arr = np.array(b)
z_arr = np.array(z)

m_vals = np.unique(m_arr)        # [1,2,…,9]
b_vals = np.unique(b_arr)        # [1,2,…,9]

M, B = np.meshgrid(m_vals, b_vals)

Z = z_arr.reshape(len(b_vals), len(m_vals))

fig = plt.figure(figsize=(10,7))
ax  = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(
    M, B, Z,
    cmap='viridis',
    edgecolor='k',
    linewidth=0.3
)
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='Error')
ax.set_xlabel('m (slope)')
ax.set_ylabel('b (intercept)')
ax.set_zlabel('Error')
ax.set_title('Error Surface over (m,b)')
plt.show()