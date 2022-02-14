#!/usr/bin/env python3
from abc import ABC, abstractclassmethod

FILE = 0
RANK = 1

class ChessPiece():
    Position = ()
    Color = ""
    PieceChar = ""

    @abstractclassmethod
    def __init__(self, currentPos, color, pieceChar):
        self.Position = currentPos
        self.Color = color
        self.PieceChar = pieceChar
    
    @abstractclassmethod
    def MovePiece(self):
        pass
    
    @abstractclassmethod
    def PossibleMoves(self):
        pass


class Pawn(ChessPiece):
    doubleMoved = False

    def MovePiece(self, toPos):
        pass

    def PossibleMoves(self):
        pass

    def IsMoveValid(self, board, toPos):
        if self.Color == "White":
            if toPos[RANK] == self.Position[RANK]+1:
                if toPos[FILE] == self.Position[FILE]:
                    return True
                else: #en passant
                    if toPos[FILE] == self.Position[FILE] + 1:
                        if type(board.GetPieceAtPos((self.Position[FILE]+1, self.Position[RANK]))) == Pawn:
                            if board.GetPieceAtPos((self.Position[FILE]+1, self.Position[RANK])).doubleMoved == True:
                                return True
                            else:
                                return False
                        if type(board.GetPieceAtPos((self.Position[FILE]-1, self.Position[RANK]))) == Pawn:
                            if board.GetPieceAtPos((self.Position[FILE]-1, self.Position[RANK])).doubleMoved == True:
                                return True
                            else:
                                return False
            else:
                return False
        if self.Color == "Black":
            if toPos[RANK] == self.Position[RANK]-1:
                if toPos[FILE] == self.Position[FILE]:
                    return True
                else: #en passant
                    if toPos[FILE] == self.Position[FILE] + 1:
                        if type(board.GetPieceAtPos((self.Position[FILE]+1, self.Position[RANK]))) == Pawn:
                            if board.GetPieceAtPos((self.Position[FILE]+1, self.Position[RANK])).doubleMoved == True:
                                return True
                            else:
                                return False
                        if type(board.GetPieceAtPos((self.Position[FILE]-1, self.Position[RANK]))) == Pawn:
                            if board.GetPieceAtPos((self.Position[FILE]-1, self.Position[RANK])).doubleMoved == True:
                                return True
                            else:
                                return False
            else:
                return False


class Chessboard():
    BOARD_SIZE = 8
    board = [[]]

    def __init__(self):
        for x in range(self.BOARD_SIZE):
            self.board.append([])
            for y in range(self.BOARD_SIZE):
                self.board[x].append(None)

    def PrintBoard(self):
        for rank in range(self.BOARD_SIZE):
            print(f"{chr(rank+65)}", end = " ")
            for file in range(self.BOARD_SIZE+1):
                if file == self.BOARD_SIZE:
                    print(f"{file}", end = " ")
                elif self.board[rank][file] == None:
                    print("X", end = " ")
                else:
                    print(self.board[rank][file].PieceChar, end = " ")
            print()
                

    def GetPieceAtPos(self, position):
        pass

    def PlacePiece(self, piece, position):
        self.board[position[RANK]][position[FILE]] = piece

def main():
    board = Chessboard()
    pawn = Pawn(("A", 1), "White", "P")
    board.PlacePiece(pawn, (1, 1))
    board.PrintBoard()

if __name__ == "__main__":
    main()
