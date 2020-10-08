from pieceParent import Piece


#-----------------------------------------------#
# Each piece has a class

class Rook(Piece):
    def __init__(self, name, team, location):
        super().__init__(name, team, location)
        # row \ column movemnt
        movement = set((0, 99), (0, -99), (-99, 0), (99, 0))

class Pawn(Piece):
    def __init__(self, name, team, location):
        super().__init__(name, team, location) 
        if team == 0:
            # pawn can move 1 north or 2 north if white
            movement = set((0,1), (0,2))
        else:
            movement = set((0,-1), (0,-2))


    def updateLocation(self, location):
        # pawn cannt move 2 spaces after being touched
        if team == 0:
            movement.remove((0,2))
        else:
            movement.remove((0,-2))
        # TODO: 


class Knight(Piece):
    def __init__(self, name, team, location):
        super().__init__(name, team, location)
        movement = set((1,-2), (-1,-2), (1,2), (-1,2), (2, 1), (2,-1), (-2,1), (-2, -1)) 
        


class Queen(Piece):
    def __init__(self, name, team, location):
        super().__init__(name, team, location)
        
        movement = set((0,99), (0,-99), (-99,0), (99,0),(99,99) )



class King(Piece):
    def __init__(self, name, team, location):
        super().__init__(name, team, location)
        movement = set((0,1), (0,-1), (-1,0), (1,0), (1,1), (-1,1), (-1,-1), (1, -1))
        # TODO: add special case with castling

class Bishop(Piece):
    def __init__(self, name, team, location):
        super().__init__(name, team, location)
    
        movement = set((99, 99), (-99, 99), (-99, -99), (99, -99))


#-------------------------------------------------------------------#
# "static" global methods



def evalPiece(name, team, location):
    if name == "Rook":
        return Rook(name, team, location)

    elif name == "Queen":
        return Queen(name, team, location)
    elif name == "Knight":
        return Knight(name, team, location)
    elif name == "King":
        return King(name, team, location)
    elif name == "Bishop":
        return Bishop(name, team, location)
