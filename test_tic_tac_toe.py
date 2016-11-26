from unittest import TestCase

import tic_tac_toe

def make_board(s):
    board = {}
    for row in range(0, 3):
        for col in range(0, 3):
            board[row, col] = s[(row * 3) + col]
    return board

def print_winner(board):
    print('{} Wins!'.format(tic_tac_toe.winner(board)))

class TestTic_tac_toe(TestCase):
    def test_game_is_done(self):
        board = make_board('         ')
        tic_tac_toe.draw_game(board)
        assert not tic_tac_toe.game_is_done(board)

        board = make_board('XXX      ')
        print()
        tic_tac_toe.draw_game(board)
        assert tic_tac_toe.game_is_done(board)
        print_winner(board)

        board = make_board('   XXX   ')
        print()
        tic_tac_toe.draw_game(board)
        assert tic_tac_toe.game_is_done(board)
        print_winner(board)

        board = make_board('      XXX')
        print()
        tic_tac_toe.draw_game(board)
        assert tic_tac_toe.game_is_done(board)
        print_winner(board)

        board = make_board('X  X  X  ')
        print()
        tic_tac_toe.draw_game(board)
        assert tic_tac_toe.game_is_done(board)
        print_winner(board)

        board = make_board(' X  X  X ')
        print()
        tic_tac_toe.draw_game(board)
        assert tic_tac_toe.game_is_done(board)
        print_winner(board)

        board = make_board('  X  X  X')
        print()
        tic_tac_toe.draw_game(board)
        assert tic_tac_toe.game_is_done(board)
        print_winner(board)

        board = make_board('X   X   X')
        print()
        tic_tac_toe.draw_game(board)
        assert tic_tac_toe.game_is_done(board)
        print_winner(board)

        board = make_board('  X X X  ')
        print()
        tic_tac_toe.draw_game(board)
        assert tic_tac_toe.game_is_done(board)
        print_winner(board)

        board = make_board('OXOXOXXO ')
        print()
        tic_tac_toe.draw_game(board)
        assert not tic_tac_toe.game_is_done(board)

        board = make_board('OXOXOXXOX')
        print()
        tic_tac_toe.draw_game(board)
        assert tic_tac_toe.game_is_done(board)

        board = make_board('OXOXXOOOX')
        print()
        tic_tac_toe.draw_game(board)
        assert tic_tac_toe.game_is_done(board)
