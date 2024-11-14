import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0,     10,    100)
    y = np.sin(  x  )
    fig, ax = plt.subplots(figsize=(50, 32))
    ax.plot(x,y)
    ax.scatter(x,y,s=64,color="k")

    return fig


if __name__ == "__main__":
    fig = main()
    fig.savefig("output.png")
