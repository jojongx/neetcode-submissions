class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # one pass
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if board[row][col] != ".":
                    if (val in rows[row] or
                        val in cols[col] or
                        val in boxes[row // 3, col // 3]):
                        return False
                    rows[row].add(val)
                    cols[col].add(val)
                    boxes[row // 3, col // 3].add(val)
        return True