position = 0
aim = 0
depth = 0

with open('course.txt') as file:
    for line in file:
        command = line.split()

        if command[0] == 'forward':
            position = position + int(command[1])
            depth = depth + aim * int(command[1])
        elif command[0] == 'up':
            aim = aim - int(command[1])
        elif command[0] == 'down':
            aim = aim + int(command[1])

result = position * depth
print(f'Result: {result}')
