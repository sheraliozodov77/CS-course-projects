
###
### Author: Sherali Ozodov
### Course: CSc 110
### Description: In this game, the board will measure 1 by 9. Each player will
### get one king, and two knights. White pieces go on the left, and
### black on the right.If a king moves left or right he can jump two pieces
### over, kill the opponent, and take his place. Knights can move
### left or right until they touch another piece or the edge of the
### board. When a king hits another piece, they kill them and take
### their place.
###

from graphics import graphics

W_KNIGHT = 'WKn'
W_KING = 'WKi'
B_KNIGHT = 'BKn'
B_KING = 'BKi'
EMPTY = '   '
WHITE = 'White'
BLACK = 'Black'
LEFT = 'l'
RIGHT = 'r'


def is_valid_move(board, position, player):
    '''This function has three parameter variables. The board
    (a list, representing the 1 by 9 board), the position
    (index) of the player to move, and player (WHITE or BLACK).
    This function should return a True if the position (index)
    is a valid index into the board list,otherwise it should return False.
    '''
    if position>=0 and position<=9 :
        if board[position][0]!=player[0]:
            return False
        return True
    return False

def move_knight(board, position, direction):
    '''This function has the same three parameters(board, position,
    direction). move_knight should move a knight on the board. A
    knight can move to the left or the right in this function. A
    knight moves two spaces. If it lands on a piece that is
    currently occupied, it kills that piece.
    '''
    if direction == 'r':
        board[position+2]= board[position]
        board[position]=EMPTY
    elif direction == 'l':
        board[position-2] = board[position]
        board[position]=EMPTY

def move_king(board, position, direction):
    '''This function has the same three parameters(board, position,
    direction).move_king should move a king on the board. In the
    game, a king can move either left or right. The king will move
    until either it reaches another piece (killing that piece and
    taking it's place), or an end of the board.
    '''
    if direction == 'l':
        while position>0:
            if board[position-1] == EMPTY:
                board[position-1] = board[position]
                board[position] = EMPTY
            else:
                board[position-1] = board[position]
                board[position] = EMPTY 
                return
            position -= 1
    elif direction == 'r':
        while (position)<8:
            if board[position+1] == EMPTY:
                board[position+1] = board[position]
                board[position] = EMPTY
            else:
                board[position+1] = board[position]
                board[position] = EMPTY
                return
            position += 1

def print_board(board):
    '''The function has one parameter, a board list, and it prints
    out the board.
    '''
    print('+' + '-'*53 + '+')
    for i in range(len(board)):
        print('|', board[i], end=' ')
    print('|')
    print('+' + '-'*53 + '+')

def draw_board(board, gui):
    '''This function should
    represents the board on the canvas. This function has two
    parameters,the board list and a graphics object.It checks whether
    it is white ir black, and then if it is king it prints out king
    on the canvas, if it is knight, it prints out knight on the board respectively
    '''
    gui.clear()
    gui.text(230, 20, '1 Dimensional Chess', 'green', 30)
    color_back = gui.get_color_string(150, 50, 8)
    i = 0
    while i < 9:
        gui.rectangle(70 * i + 40, 85, 70, 70, color_back)
        if board[i]==W_KING:
                gui.text(70 * i + 60, 112, 'king', 'white', 15)
        elif board[i]==W_KNIGHT:
                gui.text(70 * i + 60, 112, 'knight', 'white', 15)
        if board[i]==B_KING:
                gui.text(70 * i + 60, 112, 'king', 'black', 15)
        elif board[i]==B_KNIGHT:
                gui.text(70 * i + 60, 112, 'knight', 'black', 15)
        i += 1
    position_coord= 110
    while position_coord < 700:
        gui.line(position_coord, 85, position_coord, 154, 'black', 1)
        position_coord += 70
    gui.line(40, 85, 40, 154, 'black', 1.1)
    gui.line(40, 85, 670, 85, 'black', 1.3)
    gui.line(40, 154, 670, 154, 'black', 1.3)
    gui.update_frame(40)
def is_game_over(board):
        '''This function has one parameter board, If the white king
        does not exist on the board, then the game is over, and black
        wins. In this case, the function should print the board, print
        Black wins! and return true. If the black king does not exist
        on the board, then the game is over, and white wins.
        '''
        if B_KING not in board:
           print_board(board)
           print('White wins!')
           return True
        elif W_KING not in board:
            print_board(board)
            print('Black wins!')
            return True
        elif W_KING in board and B_KING in board:
            return False

def move(board, position, direction):
    '''This function has three parameter variables, representing
    the board (1 by 9), the position of the player to move (index),
    and a direction to switch between (l or r). This function
    should determine if the piece being moved is a king or a knight.
    '''
    if board[position] == W_KNIGHT or board[position] == B_KNIGHT:
       move_knight(board, position, direction)
    elif board[position] == W_KING or board[position] == B_KING:
       move_king(board, position, direction)

def main():
    # Create the canvas
    gui = graphics(720, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]
    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE

    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:

        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            # Draw the board again
            draw_board(board, gui)
            is_game_won = is_game_over(board)
main()
