from Fish import Fish
import math

data = {}

with open('lanternfish.txt') as f:
    lanternfish = [int(x) for x in f.readline().split(',')]
    
    for value in range(max(9, max(lanternfish))):
        data[value] = 0
    for element in lanternfish:
        data[element] += 1

print(data)

for days in range(256):
    zeroes = data[0]
    data[0] = 0

    for index in range(1, len(data)):
        data[index - 1] = data[index] ##
        data[index] = 0
    data[6] += zeroes
    data[8] += zeroes
    print(data)

solution = 0
for key in data:
    solution += data[key]

print(f"Resenje: {solution}")
