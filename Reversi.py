# Reversi

import random
import sys

def drawBoard(board):
    HLINE = '  +---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |'

    print('     1   2   3   4   5   6   7   8')
    print(HLINE)

    for y in range(8):
    	print(VLINE)
    	print(y+1, end=' ')
    	for x in range(8):  #zalozenie dla bledu przy None?
    		print('| %s' %(board[x][y]), end=' ')
    	print('|')
    	print(VLINE)
    	print(HLINE)


def resetBoard(board):
	for x in range(8):
		for y in range(8):
			board[x][y] = ' '

	board[3][3] = 'X'
	board[3][4] = 'O'
	board[4][3] = 'O'
	board[4][4] = 'X'


def getNewBoard():
	board = []
	for i in range(8):
		board.append([' '] * 8)

	return board


def isValidMove(board, tile, xstart, ystart):
	if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
		return False

	board[xstart][ystart] = tile

	if tile == 'X':
		otherTile = 'O'
	else:
		otherTile = 'X'

	tilesToFlip = []
	for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
		x += xdirection
		y += ydirection
		if not isOnBoard(x, y):
			continue
		if board[x][y] == tile:
			while True:
				x -= xdirection
				y -= ydirection
				if x == xstart and y == ystart:
					break
				tilesToFlip.append([x][y])

	board[xstart][ystart] = ' '
	if len(tilesToFlip) == 0:
		return False
	return tilesToFlip

def isOnBoard(x, y):
	return x >= 0 and x <= 7 and y >= 0 and y <= 7

def getBoardWithValidMoves(board, tile):
	dupeBoard = getBoardCopy(board)

	for x, y in getValidMoves(dupeBoard, tile):
		dupeBoard[x][y] = ' '
	return dupeBoard

def getValidMoves(board, tile):
	validMoves = []

	for x in range(8):
		for y in range(8):
			if isValidMove(board, tile, x, y) != False:
				validMoves.append([x, y])
	return validMoves

