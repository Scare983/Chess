from pieceParent import Piece


#-----------------------------------------------#
# Each piece has a class

class Rook(Piece):
    def __init__(self, name, team, location):
        super().__init__(name, team, location)
        # row \ column movemnt
        moves = [(0, 99), (0, -99), (-99, 0), (99, 0)]
        self.movement = set()
        for item in moves:
            self.movement.add(item)

class Pawn(Piece):
    hasMoved = False
    def __init__(self, name, team, location):
        super().__init__(name, team, location) 
        if team == 0:
            # pawn can move 1 north or 2 north if white
            moves = [(0,1), (0,2)]
        else:
            moves = [(0,-1), (0,-2)]

        self.movement = set()
        for item in moves:
            self.movement.add(item)

    def remove(self):
        return self.identity.value

    def updateLocation(self, team, toRow, toCol):
        # pawn cannt move 2 spaces after being touched
        if not Pawn.hasMoved:
            if team == 0:
                self.movement.remove((0,2))
            else:
                self.movement.remove((0,-2)) 
            Pawn.hasMoved = True
        super().updateLocation(team, toRow, toCol)

class Knight(Piece):
    def __init__(self, name, team, location):
        super().__init__(name, team, location)
        moves = [(1,-2), (-1,-2), (1,2), (-1,2), (2, 1), (2,-1), (-2,1), (-2, -1)] 
        
        self.movement = set()
        for item in moves:
            self.movement.add(item)

    def remove(self):
        return self.identity.value


class Queen(Piece):
    def __init__(self, name, team, location):
        super().__init__(name, team, location)
        
        moves = [(0,99), (0,-99), (-99,0), (99,0),(99,99) ]

        self.movement = set()
        for item in moves:
            self.movement.add(item)

    def remove(self):
        return self.identity.value

class King(Piece):
    def __init__(self, name, team, location):
        super().__init__(name, team, location)
        moves = [(0,1), (0,-1), (-1,0), (1,0), (1,1), (-1,1), (-1,-1), (1, -1)]
        # TODO: add special case with castling

        self.movement = set()
        for item in moves:
            self.movement.add(item)

    def remove(self):
        return self.identity.value


class Bishop(Piece):
    def __init__(self, name, team, location):
        super().__init__(name, team, location)
        moves = [(99, 99), (-99, 99), (-99, -99), (99, -99)]

        self.movement = set()
        for item in moves:
            self.movement.add(item)

    def remove(self):
        return self.identity.value
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



