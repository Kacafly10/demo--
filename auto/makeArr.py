import random
import math

n = input ("Enter the number of elements in the array: ")
n = int(n)

old_sum = 0.000001
array = []

def makeArr():
    global old_sum
    sub_array = []
    sum = 0.0
    for i in range(n):
        val = round(random.uniform(0, 1), 6)
        sub_array.append(val)
        sum += val
    if sum < old_sum:
        return makeArr()
    old_sum = sum
    return sub_array

for i in range(n):
    array.append(makeArr())

print(array)