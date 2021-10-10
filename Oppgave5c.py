
def min_funksjon(n):
    sum = 0
    for n in range(2, n + 1):
        sum += (n-1)/n
    return sum + n/(n + 1)

n = int(input("Skriv inn n: "))
#n = 104
print(min_funksjon(n))


