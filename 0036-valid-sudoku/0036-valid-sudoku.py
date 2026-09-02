class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]

        squares = {
            0 : {
                0 : set(),
                1 : set(),
                2 : set()
            },
            1 : {
                0 : set(),
                1 : set(),
                2 : set()
            },
            2 : {
                0 : set(),
                1 : set(),
                2 : set()
            }
        }

        sq_row = 0

        for row in range(9):

            sq_col = 0

            if row % 3 == 0 and row:
                if row == 3:
                    sq_row = 1
                else:
                    sq_row = 2

            for el in range(9):

                if board[row][el] == ".":
                    continue
                else:
                    if el > 2:
                        if el < 6:
                            sq_col = 1
                        else:
                            sq_col = 2
                    
                    num = board[row][el]

                    if num in rows[row] or num in columns[el] or num in squares[sq_row][sq_col]:
                        return False
                    else:
                        rows[row].add(num)
                        columns[el].add(num)
                        squares[sq_row][sq_col].add(num)
        return True



        