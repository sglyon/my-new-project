import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0, 10, 100)
    y = np.cos(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, color="cyan")
    return fig


if __name__ == "__main__":
    fig = main()
    fig.savefig("output.png")
