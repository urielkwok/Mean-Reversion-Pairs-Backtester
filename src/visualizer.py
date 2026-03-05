import matplotlib.pyplot as plt


def plot_z_values(z_values):
    plt.figure(figsize=(8,5))
    plt.plot(z_values)
    plt.xlabel("Time")
    plt.ylabel("Z-Values")
    plt.title("Z-Values vs Time")
    plt.savefig("z_values.png")
