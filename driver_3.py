#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:44:03 2017

@author: lauritsdixen
"""

class Board(object):
    # board class
    
    def __init__(self,board):
        # initiates a boardstate
        self.board = board
       
    def getBoard(self):
        # returns boardlist
        return self.board
    
    def __str__(self):
        # prints the boardstate in a fancy way, for debugging
        board = self.getBoard()
        out = str(board[0:3]) + '\n' + str(board[3:6]) + '\n' + str(board[6:9])
        
        return out
       
    def getFreePosisition(self):
        # returns integer that is the free place at the board
        return self.getBoard().index(0)
    
    def getAvailMoves(self):
        # return a list of strings with available moves
        moves = []
        fP = self.getFreePosisition()
        
        if fP - 3 <= 8:
            moves.append('Up')
        if fP + 3 >= 0:
            moves.append('Down')
        if not fP % 3 == 0:
            moves.append('Left')
        if not fP % 3 == 2:
            moves.append('Right')
        return moves
    
    def move(self,move):
        # makes a move, take a string and outputs a list with the new boardstate
        
        fP = self.getFreePosisition()
        board = self.getBoard()

        if move == 'Up':
            partnerValue = board[fP - 3]
            board[fP] = partnerValue
            board[board.index(partnerValue)] = 0
        
        if move == 'Down':
            partnerValue = board[fP + 3]
            board[fP] = partnerValue
            board[board.index(partnerValue)] = 0
            
        if move == 'Left':
            partnerValue = board[fP - 1]
            board[fP] = partnerValue
            board[board.index(partnerValue)] = 0
        
        if move == 'Right':
            partnerValue = board[fP + 1]
            board[fP] = partnerValue
            board[board.index(partnerValue)] = 0
            
        return board
        
    
    def getChildren(self):
        # return a list of boardstates(class)
        # that can be generated from current state  
        children = []
        
        for m in self.getAvailMoves():
            children.append(Board(self.move(m)))
        
        return children
        
b = Board([1,2,3,4,0,5,6,7,8])
print ("current state: ")
print(b)
print(" ")
b.move("Right")
print(b)


     
#if __name__ == "__main__":
#    # execute only if run as a script
#    main()      
        
        
        