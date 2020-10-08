# controller 
from board import Board
from player import Player


gameInProgress = 0



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
                myBoard.prettyPrintBoard()
                pieceLocations = myBoard.getLegalMoveablePieces(currentTurn)
                print("\n{}".format(pieceLocations))
                # until we confirm the movement.  Let user pick different pieces to look at.  
                while True:

                    pieceCord =  input("Please input row/col piece to move.  ")
                    fakeList = list(pieceCord.lower())
                    row, col = [*fakeList]
                    
                    piece = myBoard.getTeamPiece(set(int(row), col))
                    if piece == False:
                        print("Enemy piece chosen")
                    elif piece == None:
                        print("Empty square detected")

                    movementSet = myBoard.getLegalMoves(piece)
                exit(1)

    


