def draw_game(board):
    print(' {} | {} | {} '.format(board[0, 0], board[0, 1], board[0, 2]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[1, 0], board[1, 1], board[1, 2]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[2, 0], board[2, 1], board[2, 2]))


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
    row = int(move / 3)
    col = move % 3
    print('board[{}, {}]={}'.format(row, col, player))
    board[row, col] = player


def print_winner(board):
    player = winner(board)
    if player == ' ':
        player = 'Nobody'
    print('{} wins!'.format(player))

def tic_tac_toe():
    board = {}
    for row in range(0, 3):
        for col in range(0, 3):
            board[row, col] = ' '

    players = 'XO'
    player = 0
    draw_game(board)
    while not game_is_done(board):
        move = int(input('What is player {} move? [0-9]\n'.format(players[player])))
        update_game(board, move, players[player])
        draw_game(board)
        player = (player + 1) % len(players)
    print_winner(board)

if __name__ == '__main__':
    tic_tac_toe()
