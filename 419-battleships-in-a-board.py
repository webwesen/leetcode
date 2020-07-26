# https://leetcode.com/problems/battleships-in-a-board/

# === 1 ===

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        num_ships = 0
        if not board: 
            return num_ships
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.')):
                    num_ships += 1 
        return num_ships

# === 2 ===

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board: 
            return 0
        
        num_ships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print(i, j)
                if board[i][j] == "X":
                    num_ships += 1
                    self.sink_ship(board, i, j)
                
        return(num_ships)
    
    def sink_ship(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '.':
            return
        else:
            board[i][j] = "."
            self.sink_ship(board, i-1, j)
            self.sink_ship(board, i+1, j)
            self.sink_ship(board, i, j-1)
            self.sink_ship(board, i, j+1)
        return
