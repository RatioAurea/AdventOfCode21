from to_decimal import to_decimal

gamma_list = []

with open('report.txt') as f:
    length = len(f.readline().strip())

    zeros = [0] * length
    ones = [0] * length

    for line in f:
        for i in range(length):
            if int(line[i]) == 0:
                zeros[i] += 1
            if int(line[i]) == 1:
                ones[i] += 1

    for i in range(length):
        if ones[i] == max(zeros[i], ones[i]):
            gamma_list.append('1')
        else:
            gamma_list.append('0')

    gamma_str = ''.join(gamma_list)

    gamma = to_decimal(gamma_str)
    epsilon = pow(2, length) - 1 - gamma

print(f'Result: {gamma * epsilon}')

