import random
import math

n = input ("Enter the number of elements in the array: ")
n = int(n)

array = []

for i in range(n):
    x = round(random.uniform(-0.8, 0.8), 6)
    y = round(-1.0 + 2.0 * i / max(n - 1, 1), 6)
    array.extend((x, y, 0.0))

print(array)