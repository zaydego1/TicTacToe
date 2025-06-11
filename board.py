

class Board:
    def __init__(self, size: int, last_player: int = 0):
        self.size = size
        self.last_player = last_player
        self.board = [[None for _ in range(size)] for _ in range(size)]


    """
    Moves a player to the specified coordinates on the board.
    - Parameters: x (int): The x-coordinate (row) on the board.
    - Parameters: y (int): The y-coordinate (column) on the board.
    - Parameters: player (int): The player number (1 or 2).
    - Validates the move to ensure it is within bounds and the cell is empty.
    - Validates the correct player is making the move.
    - Place the player's number in the specified cell if the move is valid.
    - If the move is a winning move, set win to True.
    - If the move is a draw, set draw to True.
    """
    def move(self, x: int, y: int, player: int):
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return
        if self.board[x][y] is not None:
            return
        if player == self.last_player:
            return

        self.board[x][y] = player
        self.last_player = player
        print(f"Player {player} moved to ({x}, {y})")

        if self.check_win(x, y, player):
            print(f"Player {player} wins!")
        elif self.check_draw():
            print("The game is a draw!")


    def check_win(self, x: int, y: int, player:int) -> bool:
        if all(self.board[x][col] == player for col in range(self.size)):
            return True

        if all(self.board[row][y] == player for row in range(self.size)):
            return True

        if x == y and all(self.board[i][i] == player for i in range(self.size)):
            return True

        if x + y == self.size - 1 and all(self.board[i][self.size - 1 - i] == player for i in range(self.size)):
            return True

        return False

    def check_draw(self) -> bool:
        if all(self.board[x][y] is not None for x in range(self.size) for y in range(self.size)):
            return True
        return False





