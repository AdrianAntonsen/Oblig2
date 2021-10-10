import matplotlib.pyplot as plt
import numpy as np

#def avstand(x_upper, y_upper, p1, p2):
   # return np.sqrt((x_upper - p1)**2 + (y_upper - p2)**2)
def avstand(p1, x_upper, p2, y_upper):
    return np.sqrt((p1 - x_upper)**2 + (p2 - y_upper)**2)

upper_curve = np.loadtxt('data_fil1.txt', delimiter = ' ')

x_upper = upper_curve[:, 0]
y_upper = upper_curve[:, 1]

p = [145, 227]
#px = 145
#py = 227

'''
plt.figure()
plt.plot(p[0], p[1], 'b*')
plt.plot(x_upper, y_upper, 'r*')
plt.axis('equal')
plt.show()
'''

min_distanse = np.inf
''''
for i in range(len(x_upper)):
    distanse = avstand(x_upper[i], p[0], y_upper[i], p[1])
    if min_distanse > distanse:
      min_distanse = distanse
'''
for i in range(len(x_upper)):
    distanse = avstand(p[0], x_upper[i], p[1], y_upper[i])
    if min_distanse > distanse:
      min_distanse = distanse

    
    

print("korteste avstand = ", min_distanse)