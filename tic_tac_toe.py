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


def three_in_a_row(board):
    player = tiar_horizontal(board)
    if player != ' ':
        return player
    player = tiar_vertical(board)
    if player != ' ':
        return player
    return tiar_diagonal(board)


def no_moves_left(board):
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row, col] == ' ':
                return False
    return True


def game_is_done(board):
    return three_in_a_row(board) != ' ' or no_moves_left(board)


def winner(board):
    return three_in_a_row(board)


def update_game(board, move, player):
    if move > -1 and move < 10:
        row = int(move / 3)
        col = move % 3
        print('board[{}, {}]={}'.format(row, col, player))
        if board[row, col] == ' ':
            board[row, col] = player
            return True
        else:
            return False
    else:
        return False



def print_winner(board):
    player = winner(board)
    if player == ' ':
        player = 'Nobody'
    print('{} wins!'.format(player))


class TicTacToe():
    board = {}

    def draw_game(self):
        print(' {} | {} | {} '.format(self.board[0, 0], self.board[0, 1], self.board[0, 2]))
        print('---+---+---')
        print(' {} | {} | {} '.format(self.board[1, 0], self.board[1, 1], self.board[1, 2]))
        print('---+---+---')
        print(' {} | {} | {} '.format(self.board[2, 0], self.board[2, 1], self.board[2, 2]))

    def init_board(self):
        for row in range(0, 3):
            for col in range(0, 3):
                self.board[row, col] = ' '

    def play(self):
        players = 'XO'
        player = 0
        self.draw_game()
        while not game_is_done(self.board):
            move = int(input('What is player {} move? [0-9]\n'.format(players[player])))
            while not update_game(self.board, move, players[player]):
                move = int(input('Invalid Move! What is player {} move? [0-9]\n'.format(players[player])))
            draw_game(self.board)
            player = (player + 1) % len(players)
        print_winner(self.board)

if __name__ == '__main__':
    tic_tac_toe()
