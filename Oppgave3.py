import numpy as np

n = 100000
antall_pos = 0
antall_neg = 0

for i in range(0, n):
    pos1 = np.random.uniform(-1, 1.1)
    pos2 = np.random.uniform(-1, 1.1)
    pos3 = np.random.uniform(-1, 1.1)

    if (pos1 > 0 and pos2 > 0 and pos3 > 0):
        antall_pos +=1
    elif (pos1 < 0 and pos2 < 0 and pos3 < 0):
        antall_neg +=1
    else:
        continue

#positive = (antall_pos/n)*100
positive = antall_pos
#negative = (antall_neg/n)*100
negative = antall_neg
pos_arr = [positive]
#print("Pos fortegn:", positive, "%")
#print("Neg fortegn:", negative, "%")
print("Pos fortegn:", positive, "av 100000 forsøk")
print("Neg fortegn:", negative, "av 100000 forsøk")

np.savetxt("TrePositive.txt", pos_arr)
