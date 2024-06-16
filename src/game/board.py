from src.game.piece import King, Pawn

class Board():

    def __init__(self, player_color):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.set_up_board(player_color)

    def set_up_board(self, player_color):
        if player_color == 'white':
            self.board[0][4] = King('white', (0,4))
            self.board[1][4] = Pawn('white', (1,4))
            self.board[1][5] = Pawn('black', (1,5))

    def move_piece(self, start_position, end_position):
        piece = self.get_piece(start_position)
        if piece and piece.is_valid_move(end_position):
            if self.is_free(end_position):
                print("position is free")
                self.set_piece(end_position, piece) # Sets the piece in the new position
                self.set_piece(start_position, None) # Clears the previous position of the piece
                piece.move(end_position) # Updates the information of the piece
                return True
            
            elif self.can_take(start_position, end_position):
                print("Eliminates the piece in the position")
                self.set_piece(end_position, None) # Clears the piece from the final position
                self.set_piece(end_position, piece) # Sets the piece in the new position
                self.set_piece(start_position, None) # Clears the previous position of the piece
                piece.move(end_position) # Updates the information of the piece
                return True
            
            elif self.collision(start_position, end_position):
                print("Collides with own piece")
                return False


    def set_piece(self, position, piece):
        row, col = position
        self.board[row][col] = piece

    def get_piece(self, position):
        row, col = position
        return self.board[row][col]

    def is_free(self, new_position):
        return self.get_piece(new_position) == None 
    
    def collision(self, start_position, new_position):
        return self.get_piece(start_position).color == self.get_piece(new_position).color

    def can_take(self, start_position, new_position):
        return self.get_piece(start_position).color != self.get_piece(new_position).color
    
    def out_of_bounds(self, new_position):
        row, col = new_position
        allowed_positions = [0,1,2,3,4,5,6,7]
        return row not in allowed_positions or col not in allowed_positions