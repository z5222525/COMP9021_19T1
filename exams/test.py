from math import sqrt
from collections import defaultdict

n = 2 ** 13 * 13 ** 9 * 7 ** 6

m = n
results = defaultdict(int)
while m > 1:
    a, b = divmod(m, 2)
    if b == 0:
        results[2] += 1
        m = a
    else:
        break

for i in range(3, int(sqrt(n)) + 1, 2):
    while m > 1:
        a, b = divmod(m, i)
        if b == 0:
            results[i] += 1
            m = a
        else:
            break
    else:
        break

print(results.items(), sum(results.keys()))
