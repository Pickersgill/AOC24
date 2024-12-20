import numpy as np

with open("./day1.data") as data:
    lines = [l.split() for l in data.readlines()]
    vals = np.array([[int(line[0]), int(line[1])] for line in lines])
    vals = vals.T

vals1 = np.sort(vals[0])
vals2 = np.sort(vals[1])

print(sum(abs(vals2 - vals1)))

