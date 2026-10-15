import random
import math

n = input ("Enter the number of elements in the array: ")
n = int(n)

old_sum = 0
array = []

def makeArr(Nn):
    global old_sum
    global n
    sub_array = []
    sum = 0.0
    for i in range(3):
        val = round(random.uniform(Nn*1/n, (Nn+1)*1/n), 6)
        array.append(val)
        sum += val
    old_sum = sum
    return

for i in range(n):
    makeArr(i)

print(array)