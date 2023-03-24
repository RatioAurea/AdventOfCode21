with open('depths.txt') as f:
    depths = [int(d.rstrip('\n')) for d in f.readlines()]

counter_one = 0
counter_two = 0

for i in range(len(depths) - 1):
    if depths[i+1] > depths[i]:
        counter_one += 1

for i in range(1, len(depths) - 2):
    if (depths[i] + depths[i + 1] + depths[i + 2]) > (depths[i - 1] + depths[i] + depths[i + 1]):
        counter_two += 1

print(f'First part solution: {counter_one}')
print(f'Second part solution: {counter_two}')
