import numpy as np
import re

with open("./day3.data") as data:
    pattern = r"(do\(\))|(don't\(\))|((mul)\((\d+),(\d+)\))"
    string = data.read()
    muls = re.findall(pattern, string)

total = 0
enabled = True

for mul in muls:
    if "do()" in mul:
        enabled = True
    elif "don't()" in mul:
        enabled = False
    elif"mul" in mul:
        print(mul[:])
        if enabled:
            total += int(mul[4])*int(mul[5])
    
print(total)

