import random
import matplotlib.pyplot as plt
import numpy as np


def approx_pi(n):
    good_n = 0
    l = []
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        l.append((x, y))
        if x ** 2 + y ** 2 < 1:
            good_n += 1
    return 4 * good_n / n, l


def draw_circle(l: list):
    x = np.arange(-np.pi, np.pi, 0.01)
    plt.plot(np.sin(x), np.cos(x))
    x_shot = []
    y_shot = []
    for i, e in enumerate(l):
        x_shot.append(l[i][0])
        y_shot.append(l[i][1])
    plt.plot(x_shot, y_shot, color="r", linestyle="None", marker="o")
    plt.title(f"{len(l)} points tirés aléatoirement")
    plt.axis("equal")
    plt.show()
    plt.close()


pi, l = approx_pi(50)
draw_circle(l)
