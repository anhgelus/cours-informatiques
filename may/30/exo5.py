import matplotlib.pyplot as plt

plt.plot([i for i in range(10)], [0 for i in range(10)], color="b", linestyle=":")
plt.plot([i for i in range(10)], [i for i in range(10)], marker="o", color="orange", label="valeurs positives",
         linestyle="--")
plt.plot([i for i in range(10)], [-i for i in range(10)], marker="o", color="g", label="valeurs négatives",
         linestyle="-.")
plt.xlabel("Les abscisses")
plt.ylabel("Les images positives et négatives")
plt.xlim([-0.5, 9.5])
plt.ylim([-15, 15])
# plt.axis("equal")
plt.legend()
plt.show()
plt.close()
