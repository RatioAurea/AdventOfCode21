with open('input.txt') as file:
    data = [x.strip() for x in file.readlines()]
    n = len(data)
    m = len(data[0])
    result = 0
    for i in range(n):
        for j in range(m):
            if i == 0:
                if j == 0 and min(int(data[i+1][j]), int(data[i][j+1])) > int(data[i][j]):
                    result = result + int(data[i][j]) + 1
                elif j > 0 and j < m - 1 and min(int(data[i][j-1]), int(data[i][j+1]), int(data[i+1][j])) > int(data[i][j]):
                    result = result + int(data[i][j]) + 1
                elif j == m - 1 and min(int(data[i][j-1]), int(data[i+1][j])) > int(data[i][j]):
                    result = result + int(data[i][j]) + 1
            if i > 0 and i < n - 1:
                if j == 0 and min(int(data[i-1][j]), int(data[i][j+1]), int(data[i+1][j])) > int(data[i][j]):
                    result = result + int(data[i][j]) + 1
                elif j > 0 and j < m - 1 and min(int(data[i-1][j]), int(data[i][j-1]), int(data[i][j+1]), int(data[i+1][j])) > int(data[i][j]):
                    result = result + int(data[i][j]) + 1
                elif j == m - 1 and min(int(data[i][j-1]), int(data[i-1][j]), int(data[i+1][j])) > int(data[i][j]):
                    result = result + int(data[i][j]) + 1
            if i == n - 1:
                if j == 0 and min(int(data[i-1][j]), int(data[i][j+1])) > int(data[i][j]):
                    result = result + int(data[i][j]) + 1
                elif j > 0 and j < m - 1 and min(int(data[i][j-1]), int(data[i-1][j]), int(data[i][j+1])) > int(data[i][j]):
                    result = result + int(data[i][j]) + 1
                elif j == m - 1 and min(int(data[i][j-1]), int(data[i-1][j])) > int(data[i][j]):
                    result = result + int(data[i][j]) + 1
    print(result)