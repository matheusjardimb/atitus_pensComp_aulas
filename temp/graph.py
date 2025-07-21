import matplotlib.pyplot as plt

principal = 1000
taxa_1 = 1.01
taxa_2 = 1.015
meses = 12 * 30

x = []
y1 = []
y2 = []
for val in range(meses):
    x.append(val)
    y1.append(principal * (taxa_1**val))
    y2.append(principal * (taxa_2**val))

plt.plot(x, y1, label="1%")
plt.plot(x, y2, ".", label="1.5%")
plt.legend()
plt.show()
