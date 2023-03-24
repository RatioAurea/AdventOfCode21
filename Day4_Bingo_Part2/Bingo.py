class Bingo:

    def __init__(self, dim):
        self.dim = dim
        self.index = 0
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

    def transpose_bingo_marked(self):
        return [[self.marked[j][i] for j in range(len(self.marked))] for i in range(len(self.marked))]

    def check(self):
        winner_list = [True, True, True, True, True]
        result = False
        for i in range(self.dim):
            if self.marked[i] == winner_list or self.transpose_bingo_marked()[i] == winner_list:
                result = True
        return result
