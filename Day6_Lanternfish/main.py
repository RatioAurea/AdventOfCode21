from cgi import test
from adjust import adjust_lantenfish

testLanternfish = [1]
for i in range(256):
    adjust_lantenfish(testLanternfish)

print(f'TestResult: {len(testLanternfish)}')

with open('lanternfish.txt') as f:
    lanternfish = [int(x) for x in f.readline().split(',')]

    for i in range(80):
        adjust_lantenfish(lanternfish)

    print(f'Result: {len(lanternfish)}')

