from Bingo import Bingo


def to_int(lt):
    return [int(x) for x in lt]


def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat))]


bingos = []

with open('bingo.txt') as f:

    numbers = [int(x) for x in f.readline().split(',')]
    f.readline()

    index = 0
    while True:
        s = f.readline()
        if s == '':
            break
        else:
            bingo = Bingo(5)
            j = 0
            while j < 5:
                bingo.add_row(to_int(s.split()), j)
                j = j + 1
                s = f.readline()
            bingo.index = index
            index = index + 1
            bingos.append(bingo)

for b in bingos:
    b.print()

for n in numbers:
    if len(bingos) > 1:
        for b in bingos:
            b.mark_bingo(n)

        for b in bingos:
            if b.check():
                bingos.remove(b)

    else:
        bingos[0].mark_bingo(n)
        if bingos[0].check():
            s = 0
            for i in range(bingos[0].dim):
                for j in range(bingos[0].dim):
                    if not bingos[0].marked[i][j]:
                        s = s + bingos[0].matrix[i][j]
            bingos[0].print()
            bingos[0].print_marked()
            print(f'n={n}')
            print(f's={s}')
            result = n * s
            print(f'Result={result}')
            quit()
