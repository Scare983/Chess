# controller 
from board import Board
from player import Player


gameInProgress = 0

def confirmPieceToMove(moveSet, name):
    # if piece has ability to move.  
    if moveSet:
        answer = input("\nWould you like to move your {} (Y|N)?\n".format(name))
        if answer.lower() == "y":
            
            location = input("To which location?(Row|Col):\n{}\n".format(moveSet))
            fakeList = list(location.lower())
            row, col = [*fakeList]
            row = int(row)
            myElement = (row, col)
            if myElement in moveSet:

                return myElement
            else:
                return False
        else:
            return False



def printTurn(team):
    if team == 1: 
        color = '\33[100m'
    else:
        color = '\33[101m'

    print("-"*20)
    print( color + "It is team"  + " {} ".format(team) + "turn\033[0m")
    print("-"*20)


if __name__ == "__main__":
    
    while True:
        # infinitely play chess 
        # inputs will be buttons eventually.  
        answer = input("play Chess?  Y|N ")
        if answer == "N":
            break
        else:
            gameInProgress = 1
            p1 = Player(0)
            p2 = Player(1)
            myBoard = Board(p1, p2)
            currentTurn = p1
            otherTurn = p2
            

            while gameInProgress:
                printTurn(currentTurn.team)
                myBoard.prettyPrintBoard()
                pieceLocations = myBoard.getLegalMoveablePieces(currentTurn)
                print("\nThese are your piece locations:\n{}".format(pieceLocations))
                # until we confirm the movement.  Let user pick different pieces to look at.  
                

                while True:

                    pieceCord =  input("Please piece location (row/col) piece to move.  ")
                    fakeList = list(pieceCord.lower())
                    row, col = [*fakeList]
                    row = int(row)
                    piece = myBoard.getTeamPiece(row, col, currentTurn.team)
                    if piece == False:
                        print("Enemy piece chosen")
                    elif piece == None:
                        print("Empty square detected")
                    
                    pieceMovementSet = myBoard.getLegalMoves(piece)
                    #print("Available moves from the {} at {}{} are: \n{}".format(piece.identity.name, row, col, pieceMovementSet))
                    myBoard.prettyPrintBoard(pieceMovementSet)
                    element = confirmPieceToMove(pieceMovementSet, piece.identity.name)
                    if element:
                        (toRow, toCol) = element
                        val =  myBoard.movePiece(piece, toRow, toCol)
                        currentTurn.score += val
                        temp = currentTurn 
                        currentTurn = otherTurn 
                        otherTurn = temp

                        break 
                        

 

    


