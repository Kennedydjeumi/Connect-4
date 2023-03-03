class Connect4:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def print_board(self):
        print('-------------')
        for row in self.board:
            print('|', end='')
            for col in row:
                print(col + '|', end='')
            print('\n-------------')
        print(' 1 2 3 4 5 6 7')

    def get_move(self):
        while True:
            try:
                col = int(input('Player ' + self.current_player + ', enter a column number (1-7): '))
                if col < 1 or col > 7:
                    raise ValueError
                if self.board[0][col-1] != ' ':
                    raise ValueError
                return col-1
            except ValueError:
                print('Invalid input. Try again.')

    def play(self):
        while True:
            self.print_board()
            col = self.get_move()
            for row in range(5, -1, -1):
                if self.board[row][col] == ' ':
                    self.board[row][col] = self.current_player
                    break
            else:
                continue
            if self.check_win():
                self.print_board()
                print('Player ' + self.current_player + ' wins!')
                break
            if self.check_draw():
                self.print_board()
                print('It is a draw!')
                break
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        for row in range(6):
            for col in range(4):
                if (self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]) and (self.board[row][col] != ' '):
                    return True
        for row in range(3):
            for col in range(7):
                if (self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]) and (self.board[row][col] != ' '):
                    return True
        for row in range(3):
            for col in range(4):
                if (self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3]) and (self.board[row][col] != ' '):
                    return True
        for row in range(3, 6):
            for col in range(3):
                if (self.board[row][col] == self.board[row-1][col+1] == self.board[row-2][col+2] == self.board[row-3][col+3]) and (self.board[row][col] != ' '):
                    return True
        return False

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True


game = Connect4()
game.play()
