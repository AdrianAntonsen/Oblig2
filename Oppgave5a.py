
n = 104
sum = 0

for i in range(1, n + 1):
    sum += (i - 1) / i
    print(sum)

print(sum + n/(n+1))