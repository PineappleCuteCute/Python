import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Thông tin về các hành tinh
planets = {
    "Mercury": {"color": "gray", "radius": 0.38, "distance": 0.39, "speed": 0.1},
    "Venus": {"color": "yellow", "radius": 0.95, "distance": 0.72, "speed": 0.07},
    "Earth": {"color": "blue", "radius": 1, "distance": 1, "speed": 0.05},
    "Mars": {"color": "red", "radius": 0.53, "distance": 1.52, "speed": 0.03},
    "Jupiter": {"color": "orange", "radius": 11.21, "distance": 5.20, "speed": 0.01},
    "Saturn": {"color": "gold", "radius": 9.45, "distance": 9.58, "speed": 0.005},
    "Uranus": {"color": "lightblue", "radius": 4.01, "distance": 19.22, "speed": 0.002},
    "Neptune": {"color": "blue", "radius": 3.88, "distance": 30.05, "speed": 0.001}
}

# Khởi tạo subplot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Hàm để cập nhật vị trí của các hành tinh
def update_positions(planets, time):
    for planet, data in planets.items():
        angle = time * data["speed"]
        x = data["distance"] * np.sin(angle)
        y = data["distance"] * np.cos(angle)
        z = 0
        ax.scatter(x, y, z, color=data["color"], s=data["radius"] * 100)

# Hàm cập nhật plot
def update_plot(i):
    ax.clear()
    ax.set_xlim([-40, 40])
    ax.set_ylim([-40, 40])
    ax.set_zlim([-40, 40])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Solar System')
    update_positions(planets, i)

# Tạo animation
ani = plt.FuncAnimation(fig, update_plot, frames=np.arange(0, 100, 0.1), interval=50)
plt.show()
