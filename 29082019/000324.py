import numpy as np

a = [1, 2, 3, 4]
b = [10, 11, 12, 13]

print(a + b)

output = []

for item1, temo2 in zip(a, b):
	output.append(item1 + item2)


print(output)
g = list(range(1000000))
timeit sum(g)


