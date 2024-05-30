import matplotlib.pyplot as plt

plt.plot([2, 3, 4, 6], [2, 5, -2, 3], marker="o", linestyle="--", linewidth=1, color="g", markersize=20,
         markerfacecolor="r")
plt.title("Exemple 3")
plt.xlabel("Axe des x")
plt.ylabel("Axe des y")
plt.xlim([0, 10])
plt.ylim([-6, 6])
# plt.axis("equal")
plt.grid()
plt.savefig("exo4.pdf")
plt.show()
plt.close()
