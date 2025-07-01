"""
🔶 Problem Statement:
Given a 2D board of characters and a word, return True if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

🧩 Input:
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"
✅ Output:
True
🧠 Requirements:
Use backtracking to explore all possible paths.

Return early if the current path doesn’t match.

Mark visited cells (temporarily) to avoid reuse.

💡 Follow-up questions (Amazon-style):
Can you optimize the space complexity?

How would you handle large boards with a lot of repeated characters?

Can you build a Trie for multiple word searches?

🧪 Bonus Test Cases:
word = "SEE"     # True
word = "ABCB"    # False
word = "ABFSAB"  # True

"""

class Boarding:
    def __init__(self, board, word):
        self.board = board
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])

    def word_search(self):
        def backtracking(row, col, index):
            if index == len(self.word):
                return True

            if row < 0 or col < 0 or row >= self.rows or col >= self.cols:
                return False

            if self.board[row][col] != self.word[index]:
                return False

            temp = self.board[row][col]
            self.board[row][col] = '#'

            found = (
                backtracking(row+1, col, index+1) or
                backtracking(row-1, col, index+1) or
                backtracking(row, col+1, index+1) or
                backtracking(row, col-1, index+1)
            )

            self.board[row][col] = temp
            return found

        for i in range(self.rows):
            for j in range(self.cols):
                if backtracking(i, j, 0):
                    return True
        return False

if __name__ == "__main__":
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCCEDASF"
    checkword = Boarding(board, word)
    result = checkword.word_search()
    print(f"Result: {result}")