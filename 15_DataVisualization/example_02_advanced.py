import matplotlib.pyplot as plt
import math

X = [x/100*2*math.pi for x in range(100)]
Y = [math.cos(x) for x in X]

fig, ax = plt.subplots()
ax.plot(X,Y,color="C1")
ax.set_title("Funkcija cos")

fig.savefig("figure.pdf")
plt.show()
