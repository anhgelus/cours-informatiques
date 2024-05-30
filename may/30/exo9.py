import matplotlib.pyplot as plt
import numpy as np


def draw(start, stop, num, f_x, f_y):
    t = np.linspace(start, stop, num)
    plt.plot(f_x(t), f_y(t))
    plt.show()
    plt.close()


def lemniscate_x(t: np.ndarray):
    return np.sin(t) / (1 + np.cos(t) ** 2)


def lemniscate_y(t: np.ndarray):
    return np.sin(t) * np.cos(t) / (1 + np.cos(t) ** 2)


def spiral_x(t: np.ndarray):
    return np.cos(t) * t


def spiral_y(t: np.ndarray):
    return np.sin(t) * t


def heart_x(t: np.ndarray):
    return 16 * (np.sin(t) ** 3)


def heart_y(t: np.ndarray):
    return 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)


def cyclo_harmonique_x(t: np.ndarray):
    q = 7
    p = 5
    return (1 + np.cos((p / q) * t)) * np.cos(t)


def cyclo_harmonique_y(t: np.ndarray):
    q = 7
    p = 5
    return (1 + np.cos((p / q) * t)) * np.sin(t)


draw(0, 2 * np.pi, 100, lemniscate_x, lemniscate_y)
draw(0, 10 * np.pi, 100, spiral_x, spiral_y)
draw(0, 2 * np.pi, 100, heart_x, heart_y)
draw(0, 100, 1000, cyclo_harmonique_x, cyclo_harmonique_y)
