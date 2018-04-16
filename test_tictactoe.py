import unittest
# import code to be tested

import tictactoe

class test_tictactoe(unittest.TestCase):
    

    def test_board(self):
        self.assertEqual(tictactoe.board(1), [1, 2, 3])
        self.assertEqual(tictactoe.board(2), [4, 5, 6])
        self.assertEqual(tictactoe.board(3), [7, 8, 9])
    #def test_draw_board(self):
    	#self.assertEqual(tictactoe.draw_board(), [1, 2, 3]+[4, 5, 6]+[7, 8, 9])
def main():
	unittest.main()

if __name__ == '__main__':
    main()