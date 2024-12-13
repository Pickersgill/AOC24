import numpy as np

with open("./day1.data") as data:
    lines = [l.split() for l in data.readlines()]
    vals = np.array([[int(line[0]), int(line[1])] for line in lines])
    vals = vals.T


vals1 = np.unique(vals[0])
vals2 = vals[1]

total = 0
for v in vals1:
    occurs = sum(vals2 == v)
    total += occurs * v

print(total)


