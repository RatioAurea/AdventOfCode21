with open('coordinates.txt') as f:
    coordinates = []
    for line in f:
        new_line = line.replace(" -> ", ",")
        line_coordinates = [int(x) for x in new_line.split(',')]
        coordinates.append(line_coordinates)

# coordinates_updated = [c for c in coordinates if (c[0] == c[2] or c[1] == c[3])]

maximum = 0
for c in coordinates:
    for el in c:
        if el > maximum:
            maximum = el

plane = [[0 for x in range(maximum + 1)] for y in range(maximum + 1)]


for c in coordinates:
    if c[1] == c[3]:
        for i in range(min(c[0], c[2]), max(c[0], c[2]) + 1):
            plane[c[1]][i] = plane[c[1]][i] + 1
    elif c[0] == c[2]:
        for i in range(min(c[1], c[3]), max(c[1], c[3]) + 1):
            plane[i][c[0]] = plane[i][c[0]] + 1
    elif c[0] < c[2] and c[1] < c[3]:
        for i in range(c[2] - c[0] + 1):
            plane[c[1] + i][c[0] + i] += 1
    elif c[0] < c[2] and c[1] > c[3]:
        for i in range(c[2] - c[0] + 1):
            plane[c[1] - i][c[0] + i] += 1
    elif c[0] > c[2] and c[1] < c[3]:
        for i in range(c[0] - c[2] + 1):
            plane[c[1] + i][c[0] - i] += 1
    elif c[0] > c[2] and c[1] > c[3]:
        for i in range(c[0] - c[2] + 1):
            plane[c[1] - i][c[0] - i] += 1


for p in plane:
    print(p)

result = 0
for p in plane:
    for el in p:
        if el >= 2:
            result = result + 1

print(f'Result: {result}')
