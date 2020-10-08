# parent classf
# interface to be overidden by each piece
from enum import Enum
class Piece():
    def __init__(self, name, team, location):
        self.identity =  PieceConverter[name.upper()]
        #print(self.value.name)
        self.team = team  
        self.row = location[0]
        self.column = location[1]
    #override this method
    def movement():
        pass
    

class PieceConverter(Enum):
    PAWN = 1
    KNIGHT = 3
    BISHOP = 3 
    ROOK = 5 
    QUEEN = 9 
    KING = 100

if __name__ == "__main__":
    myPiece = Piece("queen", 0)
