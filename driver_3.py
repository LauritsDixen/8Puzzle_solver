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
        return self.board[:]
    
    def __str__(self):
        # prints the boardstate in a fancy way, for debugging
        board = self.getBoard()
        return str(board[0:3]) + '\n' + str(board[3:6]) + '\n' + str(board[6:9])
       
    def getFreePosisition(self):
        # returns integer that is the free place at the board
        return self.getBoard().index(0)
    
    def getAvailMoves(self):
        # return a list of strings with available moves
        moves = []
        fP = self.getFreePosisition()
        
        if fP > 2:
            moves.append('Up')
        if fP < 6:
            moves.append('Down')
        if not fP % 3 == 0:
            moves.append('Left')
        if not fP % 3 == 2:
            moves.append('Right')
        return moves
    
    def move(self,move):
        # makes a move, take a string and outputs a list with the new boardstate
        
        board = self.getBoard()

        if move == 'Up':
            a, b = board.index(0), board.index(0) - 3
            board[b], board[a] = board[a], board[b]
            return board
        
        if move == 'Down':
            a, b = board.index(0), board.index(0) + 3
            board[b], board[a] = board[a], board[b]
            return board
            
        if move == 'Left':
            a, b = board.index(0), board.index(0) - 1
            board[b], board[a] = board[a], board[b]
            return board
        
        if move == 'Right':
            a, b = board.index(0), board.index(0) + 1
            board[b], board[a] = board[a], board[b]
            return board
        
        else:
            print("not a legal move") 
    
    def getChildren(self):
        # return a list of boardstates(class)
        # that can be generated from current state  
        children = []
        
        for m in self.getAvailMoves():
            children.append(Board(self.move(m)))
        
        return children

     
#if __name__ == "__main__":
#    # execute only if run as a script
#    main()      
#
#import sys
#
#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)   
        
        
