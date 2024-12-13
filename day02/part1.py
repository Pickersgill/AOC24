import numpy as np

with open("./day2.data") as data:
    lines = [l.split() for l in data.readlines()]
    reports = np.array([np.array([int(v) for v in line]) for line in lines])

safe = 0
for report in reports:
    diffs = report[:-1] - report[1:]

    if all(diffs>0) or all(diffs<0):
        ad = abs(diffs)
        if all(ad <= 3):
            safe += 1


print(safe)


