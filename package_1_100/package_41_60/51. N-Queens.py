"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
"""
class Solution2(object):
    def solveNQuees(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    DFS(queens + [q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        DFS([],[],[])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:
            return []
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()
        self.DFS(n, 0, [])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return
        for col in range(n):
            if col  in self.cols or row + col in self.pie or row - col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)
            self.DFS(n, row + 1, cur_state + [col])
            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)

    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i -1))
        return [board[i:i + n] for i in range(0, len(board), n)]




if __name__ == '__main__':
    solution = Solution().solveNQueens(4)
    print(solution)