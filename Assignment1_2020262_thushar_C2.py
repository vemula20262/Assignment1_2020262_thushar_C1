
import numpy as np
import matplotlib.pyplot as plt
x1 = [1,4,6,7]
# y2 is a array with a time delay of 1

y1 = np.zeros(len(x1))
y1[0] = 2*x1[0]

for i in range(1,len(y1)):
    y1[i] = 3*y1[i-1]+2*x1[i]
print(y1)
plt.title("y[n]")
plt.ylabel("y[n]")
plt.xlabel("n")
plt.stem(y1)
plt.show()