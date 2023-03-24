class Bingo:

    def __init__(self, dim):
        self.dim = dim
        self.matrix = [[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]]
        self.marked = [[False, False, False, False, False],
                       [False, False, False, False, False],
                       [False, False, False, False, False],
                       [False, False, False, False, False],
                       [False, False, False, False, False]]

    def print(self):
        for i in self.matrix:
            print(i)
        print()

    def print_marked(self):
        for p in range(self.dim):
            print(self.marked[p])
        print()

    # Brana!
    def add_row1(self, r, k):
        for i in range(self.dim):
            (self.matrix[k])[i] = r[i]
            print(f'this {self.matrix[k]}')

    def add_row(self, r, k):
        self.matrix[k] = r

    def mark_bingo(self, number):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.matrix[i][j] == number:
                    self.marked[i][j] = True


def to_int(lt):
    return [int(x) for x in lt]


def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat))]


bingos = []

with open('bingo.txt') as f:

    numbers = [int(x) for x in f.readline().split(',')]
    f.readline()

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
            bingo.print()
            bingos.append(bingo)

winner_list = [True] * 5

for n in numbers:
    for b in bingos:
        b.mark_bingo(n)
        b.print_marked()

    for b in bingos:
        for i in range(b.dim):
            if b.marked[i] == winner_list:
                s = 0
                for k in range(b.dim):
                    for j in range(b.dim):
                        if not b.marked[k][j]:
                            s = s + b.matrix[k][j]
                print(f's={s}')
                print(f'n={n}')
                result = s * n
                print(f'Result: {result}')
                b.print()
                quit()

            else:
                new_matrix = transpose(b.marked)
                if new_matrix[i] == winner_list:
                    s = 0
                    for k in range(b.dim):
                        for j in range(b.dim):
                            if not b.marked[k][j]:
                                s = s + b.matrix[k][j]
                    print(f's={s}')
                    print(f'n={n}')
                    result = s * n
                    print(f'Result: {result}')
                    b.print()
                    quit()




