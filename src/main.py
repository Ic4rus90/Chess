from src.game.board import Board

def main():
    board = Board('white')
    current_position = (1,4)

    while True:
        user_input = input("Please enter new position separated by comma: ")
        row, col = map(int, user_input.split(','))
        if board.move_piece((current_position), (row,col)):
            current_position = (row,col)
        
        else:
            print('invalid move') 

if __name__ == "__main__":
    main()