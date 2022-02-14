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
        print(" ", end = " ")
        for rank in range(self.BOARD_SIZE+1):
            for file in range(self.BOARD_SIZE+1):
                if rank == 0:
                    if file != self.BOARD_SIZE:
                        print(f"{chr(file+65)}", end = " ")
                    continue
                if file == 0:
                    print(f"{rank}", end = " ")
                    continue
                elif self.board[rank-1][file-1] == None:
                    print("X", end = " ")
                    continue
                else:
                    print(self.board[rank-1][file-1].PieceChar, end = " ")
                    continue
            print()
                

    def GetPieceAtPos(self, position):
        return self.board[position[FILE]][position[RANK]]

    def DeletePieceAtPos(self, position):
        self.board[position[FILE]][position[RANK]] = None

    def PlacePiece(self, piece, position):
        self.board[position[FILE]][position[RANK]] = piece

    def MovePiece(self, origPos, newPos):
        if self.GetPieceAtPos(origPos).IsMoveValid(newPos):
            self.PlacePiece(self.GetPieceAtPos(origPos), newPos)
            self.DeletePieceAtPos(origPos)

    def SetBoard(self):
        for x in range(8):
            pawn = Pawn(("A", 1), "White", "P")
            self.PlacePiece(pawn, (1, x))

        for x in range(8):
            pawn = Pawn(("A", 1), "Black", "P")
            self.PlacePiece(pawn, (6, x))

def main():
    board = Chessboard()
    board.SetBoard()
    board.PrintBoard()
    board.MovePiece((1, 1), (1, 2))

if __name__ == "__main__":
    main()
