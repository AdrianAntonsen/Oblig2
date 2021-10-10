import matplotlib.pyplot as plt
import numpy as np

def avstand(x_lower, x_upper, y_lower, y_upper):
    return np.sqrt((x_lower - x_upper)**2 + (y_lower - y_upper)**2)

upper_curve = np.loadtxt('data_fil1.txt', delimiter = ' ')
lower_curve = np.loadtxt('data_fil2.txt', delimiter = ' ')


x_upper = upper_curve[:, 0]
y_upper = upper_curve[:, 1]

x_lower = lower_curve[:, 0]
y_lower = lower_curve[:, 1]



plt.figure()
plt.plot(x_upper, y_upper, 'r*')
plt.plot(x_lower, y_lower, 'b*')
plt.axis('equal')
plt.show()

min_distanse = np.inf

for i in range(len(x_upper)):
    for j in range(len(x_lower)):
        distanse = avstand(x_lower[j], x_upper[i], y_lower[j], y_upper[i])
        if min_distanse > distanse:
            min_distanse = distanse
            

    
    

print("korteste avstand = ", min_distanse)