class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):

            for col in range(9):

                if board[row][col] == ".":
                    continue
                else:
                    num = board[row][col]
                    box = (col // 3) + (row // 3) * 3

                    rows[row].add(num)
                    columns[col].add(num)
                    boxes[box].add(num)
        
        def backtrack(row, col):

            if row == 9:
                return True

            if col == 9:
                return backtrack(row + 1, 0)
            
            if board[row][col] != ".":
                return backtrack(row, col + 1)

            box = (col // 3) + (row // 3) * 3

            for num in range(1, 10):

                num = str(num)

                if num not in rows[row] and num not in columns[col] and num not in boxes[box]:

                    board[row][col] = num
                    rows[row].add(num)
                    columns[col].add(num)
                    boxes[box].add(num)

                    if backtrack(row, col + 1):
                        return True

                    board[row][col] = "."
                    rows[row].remove(num)
                    columns[col].remove(num)
                    boxes[box].remove(num)

            return False

        backtrack(0, 0)
                    
