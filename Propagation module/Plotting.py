import matplotlib.pyplot as plt
from Simulation import *

# Plotting

# Creating a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Creating the figure of the orbit with the obtained positions of the spacecraft
ax.plot(x_position, y_position, z_position, color="black", label="Spacecraft Propagation")

# Ploting the earth at the origin
ax.scatter(0, 0, 0, color="blue", s = 300 , label="Earth")

# Setting the labels of the plot
ax.set_xlabel("x (km)")
ax.set_ylabel("y (km)")
ax.set_zlabel("z (km)")
ax.set_title("Propagation of the spacecraft around the earth")

# Obtaining the points with the coordinates stored in debris
x_d = [i[0] for i in debris]
y_d = [j[1] for j in debris]
z_d = [k[2] for k in debris]

# Plotting al the locations of the debris data
ax.scatter(x_d, y_d, z_d, c='r', marker='.', label="Debris")
ax.legend()

# Showing the plot
plt.show()