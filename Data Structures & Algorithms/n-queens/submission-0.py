class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        lowerDiag = set()
        upperDiag = set()
        rowSet = set()

        res = []

        def solve(col: int) -> None:
            if col == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return
            
            for row in range(n):
                if (
                    (row in rowSet) or 
                    ((row + col) in lowerDiag) or 
                    ((n - 1 + col - row) in upperDiag)
                ):
                    continue
                board[row][col] = 'Q'
                rowSet.add(row)
                lowerDiag.add(row + col)
                upperDiag.add(n - 1 + col - row)

                solve(col + 1)

                board[row][col] = '.'
                rowSet.remove(row)
                lowerDiag.remove(row + col)
                upperDiag.remove(n - 1 + col - row)
        
        solve(0)
        return res