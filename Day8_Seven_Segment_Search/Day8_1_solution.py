with open('input.txt') as file:
    data = []
    for line in file.readlines(): 
        info = line.split('|')
        numbers = info[1].strip().split(' ')
        data.extend(numbers)

print(data)

result = 0
for number in data: 
    if len(number) in {2, 3, 4, 7}: result += 1

print(result)