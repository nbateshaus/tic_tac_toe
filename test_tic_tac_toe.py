from unittest import TestCase

from tic_tac_toe import TicTacToe


class TestTicTacToe(TestCase):
    def test_game_is_done(self):
        ttt = TicTacToe('         ')
        ttt.draw()
        assert not ttt.game_is_done()

        print()

        ttt = TicTacToe('XXX      ')
        ttt.draw()
        assert ttt.game_is_done()

        print()

        ttt = TicTacToe('   XXX   ')
        ttt.draw()
        assert ttt.game_is_done()

        print()

        ttt = TicTacToe('      XXX')
        ttt.draw()
        assert ttt.game_is_done()

        print()

        ttt = TicTacToe('X  X  X  ')
        ttt.draw()
        assert ttt.game_is_done()

        print()

        ttt = TicTacToe(' X  X  X ')
        ttt.draw()
        assert ttt.game_is_done()

        print()

        ttt = TicTacToe('  X  X  X')
        ttt.draw()
        assert ttt.game_is_done()

        print()

        ttt = TicTacToe('X   X   X')
        ttt.draw()
        assert ttt.game_is_done()

        print()

        ttt = TicTacToe('  X X X  ')
        ttt.draw()
        assert ttt.game_is_done()

        print()

        ttt = TicTacToe('OXOXOXXO ')
        ttt.draw()
        assert not ttt.game_is_done()

        print()

        ttt = TicTacToe('OXOXOXXOX')
        ttt.draw()
        assert ttt.game_is_done()

        print()

        ttt = TicTacToe('OXOXXOOOX')
        ttt.draw()
        assert ttt.game_is_done()
