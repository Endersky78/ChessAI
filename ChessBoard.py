#!/usr/bin/env python3
import copy
from abc import ABC, abstractclassmethod

FILE = 0
RANK = 1
UPPERCASE_OFFSET = 65
LOWERCASE_OFFSET = 97

def GetFileAsInt(file):
    return ord(file)-UPPERCASE_OFFSET

class ChessPiece():

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
        if self.Color == "Black":
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
            elif toPos[RANK] == self.Position[RANK]-2 and self.Position[RANK] == 6:
                return True
            else:
                return False
        if self.Color == "White":
            print(f"To: {toPos[RANK]} From: {self.Position[RANK]}")
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
            elif toPos[RANK] == self.Position[RANK]+2 and self.Position[RANK] == 1:
                return True
            else:
                return False


class Chessboard():
    BOARD_SIZE = 8
    board = [[]]
    whiteTurn = True
    blackTurn = False
    turnNum = 1

    def __init__(self):
        for x in range(self.BOARD_SIZE):
            self.board.append([])
            for y in range(self.BOARD_SIZE):
                self.board[x].append(None)

    def PrintBoard(self):
        print(" ", end = " ")
        for rank in reversed(range(self.BOARD_SIZE+2)):
            for file in range(self.BOARD_SIZE+1):
                if rank == self.BOARD_SIZE+1:
                    if file != 0:
                        print(chr((file-1)+UPPERCASE_OFFSET), end = " ")
                    continue
                if rank == 0:
                    continue
                if file == 0:
                    print(rank, end = " ")
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
        self.board[position[RANK]][GetFileAsInt(position[FILE])] = copy.deepcopy(piece)
        self.board[position[RANK]][GetFileAsInt(position[FILE])].Position = position

    def MovePiece(self, origPos, newPos):
        piece = self.GetPieceAtPos(origPos)
        if (piece):
            if piece.IsMoveValid(self.board, newPos):
                self.PlacePiece(piece, newPos)
                self.DeletePieceAtPos(origPos)
            else:
                raise ValueError("This was not a valid move!")
        else:
            raise ValueError("No piece at this position!")

    def SetBoard(self):
        for x in range(8):
            pawn = Pawn((chr(x+UPPERCASE_OFFSET), 6), "Black", "P")
            self.PlacePiece(pawn, (chr(x+UPPERCASE_OFFSET), 6))

            pawn = Pawn((chr(x+UPPERCASE_OFFSET), 1), "White", "P")
            self.PlacePiece(pawn, (chr(x+UPPERCASE_OFFSET), 1))

    def ParseInput(self, input):
        #assuming pawn input
        inputTuple = (input[0].upper(), int(input[1])-1)
        if ord(inputTuple[FILE]) in range(UPPERCASE_OFFSET, UPPERCASE_OFFSET+8):
            if inputTuple[RANK] in range(0, 8):
                if self.whiteTurn:
                    if self.GetPieceAtPos((inputTuple[FILE], inputTuple[RANK]-1)):
                        self.MovePiece((inputTuple[FILE], inputTuple[RANK]-1), inputTuple)
                    else:
                        self.MovePiece((inputTuple[FILE], inputTuple[RANK]-2), inputTuple)
                    return
                else:
                    if self.GetPieceAtPos((inputTuple[FILE], inputTuple[RANK]+1)):
                        self.MovePiece((inputTuple[FILE], inputTuple[RANK]+1), inputTuple)
                    else:
                        self.MovePiece((inputTuple[FILE], inputTuple[RANK]+2), inputTuple)
                    return

        raise ValueError("This was not a valid move!")

def main():
    board = Chessboard()
    board.SetBoard()
    
    while True:
        board.PrintBoard()
        move = input("Enter your move: ")
        board.ParseInput(move)
        board.blackTurn = not board.blackTurn
        board.whiteTurn = not board.whiteTurn

if __name__ == "__main__":
    main()
