import numpy as np
import matplotlib.pyplot as plt

def f(x):
    for i in x:
        funksjon = 2*np.sin(i) + 5/2

        if (funksjon > 4):
            y.append(4)
        elif (funksjon < 1):
            y.append(1)
        else:
            y.append(funksjon)



x = np.linspace(1, 20, 1000)    
y = []
f(x)

plt.figure()
plt.plot(x, y, linewidth = 3)
plt.show()