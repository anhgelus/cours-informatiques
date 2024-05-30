import matplotlib.pyplot as plt
import numpy as np


def create_cos(pas):
    x = np.arange(-np.pi, np.pi, pas)
    plt.plot(x, np.cos(x))
    plt.title(f"Cosinus au pas {pas}")
    plt.xlabel("x")
    plt.ylabel("cos(x)")
    plt.show()
    plt.savefig(f"exo6.cos.{pas}.png")
    plt.close()


# create_cos(1)
# create_cos(0.5)
# create_cos(0.1)
# create_cos(0.01)

x = np.arange(-10, 15, .01)
plt.plot(x, x**3-3*(x**2)+2*x+12)
plt.title(f"x^3-3x^2+2x+12")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
plt.savefig(f"exo6.cubique.png")
plt.close()
