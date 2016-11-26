def tiar_horizontal(board):
    for row in range(0, 3):
        if board[row, 0] == board[row, 1] and \
           board[row, 0] == board[row, 2] and \
           board[row, 0] != ' ':
            return board[row, 0]
    return ' '


def tiar_vertical(board):
    for col in range(0, 3):
        if board[0, col] == board[1, col] and \
           board[0, col] == board[2, col] and \
           board[0, col] != ' ':
            return board[0, col]
    return ' '


def tiar_diagonal(board):
    if board[0, 0] == board[1, 1] and \
       board[0, 0] == board[2, 2] and \
       board[0, 0] != ' ':
        return board[0, 0]
    if board[0, 2] == board[1, 1] and \
       board[0, 2] == board[2, 0] and \
       board[0, 2] != ' ':
        return board[0, 2]
    return ' '


def no_moves_left(board):
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row, col] == ' ':
                return False
    return True


class TicTacToe():
    def __init__(self, s=None):
        self.board = {}
        self.players = 'XO'
        self.player = 0
        if s is None:
            s = '         '
        for row in range(0, 3):
            for col in range(0, 3):
                self.board[row, col] = s[(row * 3) + col]

    def draw(self):
        print(' {} | {} | {} '.format(self.board[0, 0], self.board[0, 1], self.board[0, 2]))
        print('---+---+---')
        print(' {} | {} | {} '.format(self.board[1, 0], self.board[1, 1], self.board[1, 2]))
        print('---+---+---')
        print(' {} | {} | {} '.format(self.board[2, 0], self.board[2, 1], self.board[2, 2]))
        player = self.winner()
        if player != ' ':
            print('{} wins!'.format(player))

    def game_is_done(self):
        return self.winner() != ' ' or no_moves_left(self.board)

    def winner(self):
        player = tiar_horizontal(self.board)
        if player != ' ':
            return player
        player = tiar_vertical(self.board)
        if player != ' ':
            return player
        return tiar_diagonal(self.board)

    def update_game(self, move):
        if -1 < move < 10:
            row = int(move / 3)
            col = move % 3
            print('board[{}, {}]={}'.format(row, col, self.current_player()))
            if self.board[row, col] == ' ':
                self.board[row, col] = self.current_player()
                return True
            else:
                return False
        else:
            return False

    def current_player(self):
        return self.players[self.player]

    def next_player(self):
        self.player = (self.player + 1) % len(self.players)

    def play(self):
        self.draw()
        while not self.game_is_done():
            move = int(input('What is player {} move? [0-9]\n'.format(self.current_player())))
            while not self.update_game(move):
                move = int(input('Invalid Move! What is player {} move? [0-9]\n'.format(self.current_player())))
            self.draw()
            self.next_player()

if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.play()
