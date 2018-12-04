#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
    """ player that would play the Connect Four game
    """
    def __init__(self, checker):
        """ constructor
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string representing a Player object
        """
        return 'Player ' + self.checker

    def opponent_checker(self):
        """ returns a one-character string representing the
            checker of the Player object’s opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """ accepts a Board object as a parameter and returns
            the column where the player wants to make the next move
        """
        while True:
            column = eval(input('Enter a column: '))
            if board.can_add_to(column) == False:
                print('Try again!')
            else:
                self.num_moves += 1
                return column
                
            
