class NumMatrix:

    def __init__(self, mat):
        n = len(mat)
        m = len(mat[0])

        n
        self.pre = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # build prefix sum
        for i in range(n):
            for j in range(m):
                self.pre[i + 1][j + 1] = (
                    mat[i][j]
                    + self.pre[i][j + 1]
                    + self.pre[i + 1][j]
                    - self.pre[i][j]
                )

    def sumRegion(self, r1, c1, r2, c2):

        # shift because of extra padding row/column
        r1 += 1
        c1 += 1
        r2 += 1
        c2 += 1

        box = self.pre[r2][c2]
        left_box = self.pre[r2][c1 - 1]
        up_box = self.pre[r1 - 1][c2]
        overlap = self.pre[r1 - 1][c1 - 1]

        return box - left_box - up_box + overlap