import math
import sys

def fuelUsed(k, memo):
    sum = 0
    for key in memo:
        sum += abs(key - k) * memo[key]
    return sum

with open('input.txt') as file:
    positions = [int(x) for x in file.readline().split(',')]
    n = len(positions)
    max = 0
    for i in range(n):
        if positions[i] > max:
            max = positions[i]
    
    memo = {}
    for i in positions:
        memo[i] = 0

    for i in positions:
        memo[i] += 1

    fuel_min = sys.maxsize
    for k in range(max + 1):
        current = fuelUsed(k, memo)
        if current < fuel_min:
            fuel_min = current

    print(fuel_min)