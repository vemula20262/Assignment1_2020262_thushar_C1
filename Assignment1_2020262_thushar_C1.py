import numpy
import numpy as np
import matplotlib.pyplot as plt
x1 = [1,-1,3,0]
x = [2,-3,1,4]
x2 = [element * 2 for element in x]
y1 = np.add(x1,x2)
print(y1)
y2=np.zeros(len(x1)+3)
print(y2)
for i in range(len(y1)):
    y2[i+3] = y1[i]
print("output = " , y2)

plt.title("y[n]")
plt.ylabel("y[n]")
plt.xlabel("n")
plt.stem(y2)
plt.show()
