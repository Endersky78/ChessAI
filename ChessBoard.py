#!/usr/bin/env python3
from abc import ABC, abstractclassmethod

FILE = 0
RANK = 1
UPPERCASE_OFFSET = 65
LOWERCASE_OFFSET = 97

def GetFileAsInt(file):
    return ord(file)-UPPERCASE_OFFSET

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
            if toPos[RANK] == self.Position[RANK]-1:
                if GetFileAsInt(self.Position[FILE]) == GetFileAsInt(self.Position[FILE]):
                    return True
                else: #en passant
                    if GetFileAsInt(self.Position[FILE]) == GetFileAsInt(self.Position[FILE]) + 1:
                        if type(board.GetPieceAtPos((chr(GetFileAsInt(self.Position[FILE])+1+UPPERCASE_OFFSET), self.Position[RANK]))) == Pawn:
                            if board.GetPieceAtPos((chr(GetFileAsInt(self.Position[FILE])+1+UPPERCASE_OFFSET), self.Position[RANK])).doubleMoved == True:
                                return True
                            else:
                                return False
                        if type(board.GetPieceAtPos((chr(GetFileAsInt(self.Position[FILE])-1+UPPERCASE_OFFSET), self.Position[RANK]))) == Pawn:
                            if board.GetPieceAtPos((chr(GetFileAsInt(self.Position[FILE])-1+UPPERCASE_OFFSET), self.Position[RANK])).doubleMoved == True:
                                return True
                            else:
                                return False
            else:
                return False
        if self.Color == "Black":
            if toPos[RANK] == self.Position[RANK]+1:
                if GetFileAsInt(self.Position[FILE]) == GetFileAsInt(self.Position[FILE]):
                    return True
                else: #en passant
                    if GetFileAsInt(self.Position[FILE]) == GetFileAsInt(self.Position[FILE]) + 1:
                        if type(board.GetPieceAtPos((chr(GetFileAsInt(self.Position[FILE])+1+UPPERCASE_OFFSET), self.Position[RANK]))) == Pawn:
                            if board.GetPieceAtPos((chr(GetFileAsInt(self.Position[FILE])+1+UPPERCASE_OFFSET), self.Position[RANK])).doubleMoved == True:
                                return True
                            else:
                                return False
                        if type(board.GetPieceAtPos((chr(GetFileAsInt(self.Position[FILE])-1+UPPERCASE_OFFSET), self.Position[RANK]))) == Pawn:
                            if board.GetPieceAtPos((chr(GetFileAsInt(self.Position[FILE])-1+UPPERCASE_OFFSET), self.Position[RANK])).doubleMoved == True:
                                return True
                            else:
                                return False
            else:
                return False


class Chessboard():
    BOARD_SIZE = 8
    board = [[]]
    whiteTurn = True
    blackTurn = False

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
                        print(f"{chr(file+UPPERCASE_OFFSET)}", end = " ")
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
        return self.board[position[RANK]][GetFileAsInt(position[FILE])]

    def DeletePieceAtPos(self, position):
        self.board[position[RANK]][GetFileAsInt(position[FILE])] = None

    def PlacePiece(self, piece, position):
        self.board[position[RANK]][GetFileAsInt(position[FILE])] = piece

    def MovePiece(self, origPos, newPos):
        if self.GetPieceAtPos(origPos).IsMoveValid(self.board, newPos):
            self.PlacePiece(self.GetPieceAtPos(origPos), newPos)
            self.DeletePieceAtPos(origPos)

    def SetBoard(self):
        for x in range(8):
            pawn = Pawn((chr(x+UPPERCASE_OFFSET), 1), "White", "P")
            self.PlacePiece(pawn, (chr(x+UPPERCASE_OFFSET), 1))

        for x in range(8):
            pawn = Pawn(("A", 1), "Black", "P")
            self.PlacePiece(pawn, (chr(x+UPPERCASE_OFFSET), 6))

    def ParseInput(self, input):
        #assuming pawn input
        if ord(input[0]) in range(LOWERCASE_OFFSET, LOWERCASE_OFFSET+7):
            if int(input[1] in range(1, 8)):
                if self.whiteTurn:
                    self.MovePiece((input[FILE], input[RANK]-1), input)
                    return
                else:
                    self.MovePiece((input[FILE], input[RANK]+1), input)
                    return

        print("ERROR: This was not a valid move!!")

def main():
    board = Chessboard()
    board.SetBoard()
    board.PrintBoard()
    board.MovePiece(("A", 1), ("A", 2))
    board.PrintBoard()

if __name__ == "__main__":
    main()
