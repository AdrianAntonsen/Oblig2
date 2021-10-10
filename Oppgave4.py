import numpy as np
import matplotlib.pyplot as plt

n = 10000
to = 0
en = 0
ingen = 0

for i in range(n):
    a = int(np.random.uniform(-5, 5.1))
    b = int(np.random.uniform(-5, 5.1))
    c = int(np.random.uniform(-5, 5.1))
    
    ligning = b**2 - 4*a*c

    if (ligning > 0):
        to +=1
    elif (ligning == 0):
        en +=1
    else:
        ingen +=1


sannsynlighet = (to/n)*100, (en/n)*100, (ingen/n)*100
løsninger = "To løsninger", "En løsning", "Ingen løsninger"

plt.title("Sannsynlighet for 2, 1 eller ingen løsninger")
plt.ylabel("Prosent")
plt.bar(løsninger, sannsynlighet, color=("red","blue","yellow"))
plt.show()
