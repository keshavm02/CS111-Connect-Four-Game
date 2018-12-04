#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ Intelligent computer player """

    def __init__(self, checker, tiebreak, lookahead):
        """ constructor for AIPlayer
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        return 'Player ' + str(self.checker) + ' (' + str(self.tiebreak) + \
               ', ' + str(self.lookahead) + ')'

    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board,
            and that returns the index of the column with the maximum score
        """
        maxscore = max(scores)
        indexlist = []
        for i in range(len(scores)):
            if scores[i] == maxscore:
                indexlist += [i]

        if self.tiebreak == 'LEFT':
            return indexlist[0]
        elif self.tiebreak == 'RIGHT':
            return indexlist[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(indexlist)
            
    def scores_for(self, board):
        """ takes a Board object board and determines the called AIPlayer‘s
            scores for the columns in board
        """
        scores = [50] * board.width
        for col in range(len(scores)):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opp = AIPlayer(self.opponent_checker(), \
                                           self.tiebreak, self.lookahead - 1)
                opp_scores = opp.scores_for(board)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif  max(opp_scores) == 100:
                    scores[col]  = 0
                elif  max(opp_scores) == 50:
                    scores[col] = 50
                board.remove_checker(col)
                
        return scores
                
    def next_move(self, board):
        """ return the called AIPlayer‘s judgment of its best possible move
        """
        nextmove = self.max_score_column(self.scores_for(board))
        self.num_moves += 1
        return nextmove
