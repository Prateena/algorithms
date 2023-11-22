import array as arr
from itertools import combinations

array_input = arr.array("i", [2,3,4,5,6])

i = 2 
sum_array = []
largest = ()

while i < len(array_input):
    comb = combinations(array_input, i)
    for n in comb:
        sum_array.append(sum(n))
        if max(array_input) > 0:
            largest = n
    i += 1

print("The largest sum of array {} is {}".format(largest, max(sum_array)))