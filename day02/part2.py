import numpy as np

with open("./day2.data") as data:
    lines = [l.split() for l in data.readlines()]
    reports = np.array([np.array([int(v) for v in line]) for line in lines])

safe = 0

def is_safe(report):
    diffs = report[:-1] - report[1:]

    if all(diffs>0) or all(diffs<0):
        ad = abs(diffs)
        if all(ad <= 3):
            return True
    return False

for report in reports:
    for i in range(len(report)):
        new_report = np.concatenate([report[:i],report[i+1:]])
        if is_safe(new_report):
            safe += 1
            break


print(safe)


