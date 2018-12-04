#
# ps9pr1.py  (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#

class Board:
    """ Board to play Connect Four
    """
    def __init__(self, height, width):
        """ contrsuctor for Board
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ returns a string representing a Board object
        """
        b = ''
        for r in range(self.height):
            for c in range(self.width):
                b += '|' + self.slots[r][c]
            b += '|' + '\n'
        b += '-' * ((self.width*2)+1) + '\n'
        n = 0
        count = 0
        while count <= self.width-1:
            if n > 9:
                n = 0
            b += ' ' + str(n)
            n += 1
            count += 1
        return b

    def add_checker(self, checker, col):
        """ accepts two inputs:

            1. checker, a one-character string that specifies the
            checker to add to the board (either 'X' or 'O')

            2. col, an integer that specifies the index of the column
            to which the checker should be added and that adds checker
            to the appropriate row in column col of the board
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width) 
        for r in range(self.height):
            if self.slots[r][col] != ' ':
                self.slots[r-1][col] = checker
                break
            elif r == self.height - 1:
                self.slots[r][col] = checker
                break

    def reset(self):
        """ reset the Board object on which it is called by setting all
            slots to contain a space character
        """
        self.slots = [[' '] * self.width for x in range(self.height)]
                
    def add_checkers(self, columns):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in columns:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column
            col on the calling Board object
        """
        if 0 <= col < self.width and self.slots[0][col] == ' ':
            return True
        else:
            return False

    def is_full(self):
        """ returns True if the called Board object is completely full of
            checkers, and returns False otherwise
        """
        for r in range(self.height):
            for c in range(self.width):
                if self.slots[r][c] == ' ':
                    return False
        return True
            
    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board
            object
        """
        for r in range(self.height):
            if self.slots[r][col] != ' ':
                self.slots[r][col] = ' '
                break
    def is_win_for(self, checker):
        """ accepts a parameter checker that is either 'X' or 'O', and
            returns True if there are four consecutive slots containing
            checker on the board
        """
        assert(checker == 'X' or checker == 'O')
        def is_horizontal_win(self, checker):
            """ Checks for a horizontal win for the specified checker.
            """
            for row in range(self.height):
                for col in range(self.width - 3):
                    # Check if the next four columns in this row
                    # contain the specified checker.
                    if self.slots[row][col] == checker and \
                       self.slots[row][col + 1] == checker and \
                       self.slots[row][col + 2] == checker and \
                       self.slots[row][col + 3] == checker:
                        return True
            # if we make it here, there were no horizontal wins
            return False

        def is_down_diagonal_win(self, checker):
            """ checks for a left diagonal win for the specific checker
            """
            for row in range(self.height - 3):
                for col in range(self.width - 3):
                    if self.slots[row][col] == checker and \
                       self.slots[row + 1][col + 1] == checker and \
                       self.slots[row + 2][col + 2] == checker and \
                       self.slots[row + 3][col + 3] == checker:
                        return True
            return False

        def is_up_diagonal_win(self, checker):
            """ checks for a right diagonal win for the specific checker
            """
            for row in range(3, self.height):
                for col in range(self.width - 3):
                    if self.slots[row][col] == checker and \
                       self.slots[row - 1][col + 1] == checker and \
                       self.slots[row - 2][col + 2] == checker and \
                       self.slots[row - 3][col + 3] == checker:
                        return True
            return False

        def is_vertical_win(self, checker):
            """ Checks for a vertical win for the specified checker.
            """
            for row in range(self.height - 3):
                for col in range(self.width):
                    # Check if the next four columns in this row
                    # contain the specified checker.
                    if self.slots[row][col] == checker and \
                       self.slots[row + 1][col] == checker and \
                       self.slots[row + 2][col] == checker and \
                       self.slots[row + 3][col] == checker:
                        return True
            # if we make it here, there were no horizontal wins
            return False

        if is_horizontal_win(self, checker) == True or \
           is_down_diagonal_win(self, checker) == True or \
           is_up_diagonal_win(self, checker) == True or \
           is_vertical_win(self, checker) == True:
            return True
        else:
            return False
