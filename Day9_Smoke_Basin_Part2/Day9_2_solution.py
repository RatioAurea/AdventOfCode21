from dataclasses import dataclass
from mimetypes import init

class Point:

    basinsize = 0

    data = []
    with open('input.txt') as file:
        dataHelp = [x.strip() for x in file.readlines()]
        n = len(dataHelp)
        m = len(dataHelp[0])
        for i in range(n):
            dataHelpDigits = [int(x) for x in dataHelp[i]]
            data.append(dataHelpDigits)
    
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def LookAround(self):
        if self.i == 0 and self.j == 0 and data[self.i][self.j] not in {9, '.'}:
            data[self.i][self.j] = '.'
            basinsize += 1
            if data[self.i+1][self.j] not in {9, '.'}:
                newPoint1 = Point(i+1, j)
                newPoint1.LookAround()
            if data[self.i][self.j+1] not in {9, '.'}:
                newPoint2 = Point(i, j+1)
                newPoint2.LookAround()
        if self.i > 0 and self.i < n - 1 and self.j == 0 and data[self.i][self.j] not in {9, '.'}:
            data[self.i][self.j] = '.'
            basinsize += 1
            if data[self.i-1][self.j] not in {9, '.'}:
                newPoint3 = Point(i-1,j)
                newPoint3.LookAround()
            if data[self.i+1][self.j] not in {9, '.'}:
                newPoint4 = Point(i+1,j)
                newPoint4.LookAround()
            if data[self.i][self.j+1] not in {9, '.'}:
                newPoint5 = Point(i,j+1)
                newPoint5.LookAround()
        if self.i == n - 1 and self.j == 0 and data[self.i][self.j] not in {9, '.'}:
            data[self.i][self.j] = '.'
            basinsize += 1
            if data[self.i-1][j] not in {9, '.'}:
                newPoint6 = Point(i-1,j)
                newPoint6.LookAround()
            if data[self.i][self.j+1] not in {9, '.'}:
                newPoint7 = Point(i,j+1)
                newPoint7.LookAround()
        
        if self.i == 0 and self.j > 0 and self.j < m - 1 and data[self.i][self.j] not in {9, '.'}:
            data[self.i][self.j] = '.'
            basinsize += 1
            
            



data = []
with open('input.txt') as file:
    dataHelp = [x.strip() for x in file.readlines()]
    n = len(dataHelp)
    for i in range(n):
        dataHelpDigits = [int(x) for x in dataHelp[i]]
        data.append(dataHelpDigits)

p = Point(2,3)
print(p.data)