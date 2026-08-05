#https://sudoku-solver-edon-hall.netlify.app
class Solution:
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize sets
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + c // 3].add(num)

        def backtrack(index):

            if index == len(empty):
                return True

            r, c = empty[index]
            box = (r // 3) * 3 + c // 3

            for num in "123456789":

                if num in rows[r]:
                    continue
                if num in cols[c]:
                    continue
                if num in boxes[box]:
                    continue

                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                if backtrack(index + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)

            return False

        backtrack(0)
