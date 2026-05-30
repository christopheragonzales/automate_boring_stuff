import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
x_values = range(1, 5_001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=100)  ## type:ignore

# Set chart and label axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Values", fontsize=14)

# plt.savefig("./figures/small_cubes.png", bbox_inches="tight")

plt.savefig("./figures/large_cubes.png", bbox_inches="tight")

plt.show()
