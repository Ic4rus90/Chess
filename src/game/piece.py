class Piece:
    def __init__(self, color, position):
        self.color = color # Sets the color of the piece
        self.position = position # Sets the position of the piece (row, column)

    def move(self, new_position):
        print(f'Moving from {self.position} to {new_position}')
        self.position = new_position # Moves the piece to a new position (row, column)
    

class King(Piece):
    def move(self, new_position):
        if self.is_valid_move(new_position):
            super().move(new_position)

    def is_valid_move(self, new_position):
        row_diff = abs(self.position[0] - new_position[0])
        col_diff = abs(self.position[1] - new_position[1])
        return max(row_diff, col_diff) == 1
    

class Pawn(Piece):
# TODO: Implement ability to move two in first move.
    def move(self, new_position):
        if self.is_valid_move(new_position):
            super().move(new_position)
    
    def is_valid_move(self, new_position):
        row_diff = self.position[0] - new_position[0]
        col_diff = self.position[1] - new_position[1]

        if row_diff != 1 or col_diff != 0:
            return False
        
        else: 
            return True


class Rook(Piece):
    def move(self, new_position):
        if self.is_valid_move(new_position):
            super().move(new_position)

    def is_valid_move(self, new_position):
        row_diff = abs(self.position[0] - new_position[0])
        col_diff = abs(self.position[1] - new_position[1])

        return (row_diff == 0 and col_diff > 0) or (row_diff > 0 and col_diff == 0)
            

class Knight(Piece):
    def move(self, new_position):
        if self.is_valid_move(new_position):
            super().move(new_position)

    def is_valid_move(self, new_position):
        row_diff = abs(self.position[0] - new_position[0])
        col_diff = abs(self.position[1] - new_position[1])

        return (row_diff == 1 and col_diff == 3) or (row_diff == 3 and col_diff == 1) 


class Queen(Piece):
    def move(self, new_position):
        if self.is_valid_move(new_position):
            super().move(new_position)

    def is_valid_move(self, new_position):
        row_diff = abs(self.position[0] - new_position[0])
        col_diff = abs(self.position[1] - new_position[1])

        # Rook like movement
        if (row_diff == 0 and col_diff > 0) or (row_diff > 0 and col_diff == 0):
            return True
        
        elif (row_diff == col_diff):
            return True
        
        else:
            return False

class Bishop(Piece):
    def move(self, new_position):
        if self.is_valid_move(new_position):
            super().move(new_position)

    def is_valid_move(self, new_position):
