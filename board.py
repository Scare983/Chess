# Chess board is a grid. 
# Has a display for the board, and is a controller to the pieces. 
from piece import *

class Board():
    def __init__(self, player1=None, player2=None):
        # create pieces 
        self.myBoard = {}
        self.p1 = player1
        self.p2 = player2
        for number in list("87654321"):
            self.myBoard[int(number)] = {}
            for val in list("abcdefgh"):
                self.myBoard[int(number)][val] =  None
        self.populateBoard()    



    # populate dictionary with row/cols.  Each row/col key holds a piece class or None
    def populateBoard(self):
        for row in self.myBoard.keys():
            for column in self.myBoard[row].keys():
                if row == 8 or row == 7:
                    # blk 
                    team = 1
                    if row == 7:
                        self.myBoard[row][column] = Pawn("Pawn", team, (row, column))
                    #populate with certain piece 
                    else:
                        self.myBoard[row][column] = evalPiece(self.getInitialPieceName(column), team, (row, column))


                elif row == 1 or row == 2:
                    # white
                    team = 0 
                    if row == 2:
                        self.myBoard[row][column] = Pawn("Pawn", team, (row, column))
                    # populate with certain piece
                    else:
                        self.myBoard[row][column] = evalPiece(self.getInitialPieceName(column), team, (row, column))


                else:
                    pass
    # helper function 
    def getInitialPieceName(self, col):

        if col == "a" or col == "h":
            return "Rook"
        elif col == "b" or col == "g":
            return "Knight"
        elif col == "c" or col == "f":
            return "Bishop"
        elif col == "d":
            return "Queen"
        elif col == "e":
            return "King"

        else:
            return None

    # return set of locations that are moveable to the current player
    def getLegalMoveablePieces(self, currentPlayer):
        myLocations = set()
        for row in self.myBoard.keys():
            for col in self.myBoard[row].keys():
                if self.myBoard[row][col] != None:
                    if self.myBoard[row][col].team == currentPlayer.team:
                        myLocations.add((row, col))
        return myLocations


    # return row/Col tuple
    def getTeamPiece(self, row, col, team):
        if self.myBoard[row][col] != None:
            piece = self.myBoard[row][col]
            if piece.team == team:
                return piece
            else:
                return False
        else:
            return None


    def getOpponentPiece():
        pass



    def getLegalMoves(self, piece):
        # if pawn, check diagnal locations 
        availableMoves = set()
        currentRow = piece.row
        currentCol = piece.column
        if isinstance(piece, Pawn ):

            # TODO: fix know issue where non moved pawn can attk enemy characters 2 up, 1 left/right. 
            for move in piece.movement:
                (col, row) = move
                newRow = currentRow + row 
                newCol = col + ord(currentCol)
                try:
                    # newCol should not change...
                    itemHere = self.myBoard[newRow][chr(newCol)]
                except:
                    continue 

                if itemHere == None:
                    availableMoves.add((newRow, chr(newCol)))
                # don't add.
                # check diagnals
                # white, aka North.  check diagnols if enemies
                if newRow - currentRow != 2 or newRow- currentRow != -2:
                    try:
                        diagItem = self.myBoard[newRow][chr(newCol+1)]
                        if diagItem != None:
                            if diagItem.team != piece.team:
                                availableMoves.add((newRow, chr(newCol+1)))
                    except:
                        continue

                    try:
                        diagItem2 = self.myBoard[newRow][chr(newCol-1)]
                        if diagItem2 != None:
                            if diagItem2.team != piece.team:
                                availableMoves.add((newRow, chr(newCol-1)))
                    except:
                        continue


        elif isinstance(piece, Knight ):
            for move in piece.movement:
                (col, row) = move
                try:
                    newRow = currentRow + row 
                    newCol = col + ord(currentCol)
                    print("Row: {}\t Col:{}".format(newRow, chr(newCol)))
                    itemHere = self.myBoard[newRow][chr(newCol)]
                    # TODO: add check to see if king is in Check before adding to avalibale moveset. 
                    if itemHere == None:
                        availableMoves.add((newRow, chr(newCol)))
                    else:
                        if itemHere.team != piece.team:
                            availableMoves.add((newRow, chr(newCol)))
                        else:
                            pass

                # if new row/col not found in dict, then it is is not on the board.  
                except Exception as e:
                    #print("Debug.  Found location that is not on board when caclulating legal moves.")
                    continue
                

        # not pawn or knight
        else:
            for move in piece.movement:
                #TODO: fix distance movement of peices
                (col, row) = move
                # dealing with diagnols
                if abs(col) == 99 and abs(row) == 99:
                    try:
                        print(piece.identity.name)
                        i = 1 
                        while True:
                            newRow = currentRow + i
                            newCol = ord(currentCol) + i
                            print("newRow{}".format(newRow))
                            print("newcol{}".format(newCol))
                            i+=1 
                            itemHere = self.myBoard[newRow][chr(newCol)]
                            if itemHere == None:
                                availableMoves.add((newRow, chr(newCol)))
                            else:
                                if itemHere.team == piece.team:
                                    pass
                                elif itemHere.team != piece.team:
                                    availableMoves.add((newRow, chr(newCol)))
                                break
                    except Exception as e:
                        #print(e)
                        continue     
                elif col != 1 or col != 2:
                    try:
                        i = 1
                        while True:
                            newRow = row
                            newCol = ord(currentCol) + i
                            i+=1
                            itemHere = self.myBoard[newRow][chr(newCol)]
                            if itemHere == None:
                                availableMoves.add((newRow, chr(newCol)))
                            if itemHere:
                                # cannot take own team piece.  skip.
                                if itemHere.team == piece.team:
                                    pass
                                elif itemHere.team != piece.team:
                                    availableMoves.add((newRow, chr(newCol)))
                                else:
                                    pass
                                break

                    # check each space until hits out of bounds
                    except:
                        continue
                elif row != 1 or row !=2:
                    try:
                        i = 1
                        while True:
                            newRow = currentRow + i
                            newCol = ord(currentCol)
                            i+=1
                            itemHere = self.myBoard[newRow][chr(newCol)]
                            if itemHere == None:
                                availableMoves.add((newRow, chr(newCol)))
                            if itemHere:
                                # cannot take own team piece.  skip.
                                if itemHere.team == piece.team:
                                    pass
                                elif itemHere.team != piece.team:
                                    availableMoves.add((newRow, chr(newCol)))
                                break


                    # check each space until hits out of bounds
                    except:
                        continue
                # king single movement. 
                else:
                    try:
                        newRow = currentRow + row
                        newCol = col + ord(currentCol)
                        itemHere = self.myBoard[newRow][chr(newCol)]
                        # TODO: check if king is near other king and dont add it to list.
                        if itemHere == None:
                            availableMoves.add((newRow, chr(newCol)))
                        elif itemHere:
                            if itemHere.team != piece.team:
                                availableMoves.add((newRow, chr(newCol)))
                            else:
                                pass
                        else:
                            pass
                    except:
                        continue

        return availableMoves
    
    def movePiece(self, piece, toRow, toCol):
        score = 0 
        if self.myBoard[toRow][toCol] != None:
            score  = self.myBoard[toRow][toCol].remove()
        # update spot on board.
        self.myBoard[piece.row][piece.column] = None
        self.myBoard[toRow][toCol] = piece 
        # update piece known location
        piece.updateLocation(piece.team, toRow, toCol) 
        return score 

    def prettyPrintBoard(self, movesToShow=None):
        
        firstCol = 1
        for row in self.myBoard.keys():
            print("")
            if firstCol:
                pass
            else:
                print('\33[33m' + str(row) + '\033[0m', end="")

            for column in self.myBoard[row].keys():
                if firstCol:
                    print("\t", end="")
                    print(*["\33[33m{}\033[0m\t".format(column) for column in self.myBoard[row].keys()])
                    print('\33[33m' + str(row) + '\033[0m', end="")
                    firstCol = 0
                if self.myBoard[row][column] != None:
                    if self.myBoard[row][column].team == 1: 
                        color = '\33[100m'
                    else:
                        color = '\33[101m'
                    print(color + "\t{}".format(self.myBoard[row][column].identity.name) + '\033[0m',end="")    
                else:
                    if movesToShow:
                        if (row, column) in movesToShow:
                            print("\t\33[35mo\33[0m", end="")
                        else:
                            print("\to", end="")                           
                    else:
                        print("\to", end="")




if __name__ == "__main__":
    p1 = Player(0)
    p2 = Player(1)
    newGame = Board(p1, p2)
    newGame.prettyPrintBoard()
