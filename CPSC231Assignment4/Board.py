# Manjot Khangura
# UCID: 30003843

#Constants for piece types
EMPTY = 0
X = 1
O = 2
class Board:

#   Purpose: constructor that creates a 2 dimensional list for rows and columns to be used later
#   Parameters:
#       rowLength: row command line argument for <rows>, the default value is 3
#       columnLength: column command line argument for <cols>, the default value is 3
#   Returns: Nothing
    def __init__(self, rowLength = 3, columnLength = 3):
#       Tuple for an empty list for columns and then a list which makes rows and completes board
        self.boardTuple = ([], [], rowLength, columnLength)
#       unpacks the tuple above into the columnList, the board list (the rows with columns in them) and the rows and cols arguments
        self.columnList, self.board, self.rowLength, self.columnLength = self.boardTuple
#       for loop where it goes through the rows and then columns and appends the columns into a list and then appends this list into the
#       boards list where all the rows are then made. The columnList is then reset into an empty list and the process repeats until all 
#       the list of rows and columns are made into self.board
        for i in range(self.rowLength):
            for k in range(self.columnLength):
                self.columnList.append(EMPTY)
            self.board.append(self.columnList)
            self.columnList = []

#   Purpose: return the number of rows for the board
#   Parameters: None
#   Returns:
#       len(self.board): returns the length of the board which are the rows
    def rows(self):
        return len(self.board)

#   Purpose: return the number of columns for the board
#   Parameters: None
#   Returns:
#       len(self.board[0]): returns the length of the boards first index which is within the list of the list. This is the columns in
#       the board for the first row but since they are the same for each index, we can just use the first index.
    def cols(self):
        return len(self.board[0])

#   Purpose: Returns a boolean value for if a spot on the tic tac toe board can have a piece played (it is an empty space)
#   Parameters:
#       row: the rows of the tic tac toe board
#       col: the columns of the tic tac toe board
#   Returns:
#       True if a piece can be placed at that row and column
#       False if a piece can not be played at that row and column
    def canPlay(self, row, col):
        if self.board[row][col] == EMPTY:       # Checks if that row and column is empty (EMPTY constant)
            return True
        else: 
            return False

#   Purpose: Plays a piece on the selected row and column
#   Parameters:
#       row: the rows of the tic tac toe board
#       col: the columns of the tic tac toe board
#       piece: the piece (X or O) being played
#   Return: Nothing
    def play(self, row, col, piece):
        self.board[row][col] = piece            # Plays the piece on that row and column

#   Purpose: Checks if there are any empty spots remaining on the board
#   Parameters: None
#   Returns:
#       False if there are any empty spaces on the board
#       True if the board is completely full (no empty spaces)
    def full(self):
        for rows in self.board:
            for columns in rows:
                if columns == EMPTY:            # for loop checks each column in a row for an empty space(EMPTY constant)
                    return False
        return True
    
#   Purpose: Checks if three pieces of one player are side by side consecutively in a row
#   Parameters:
#       row: the rows of the tic tac toe board
#       piece: the piece (X or O) being played
#   Returns:
#       True if there are three pieces of one player side by side in a row
#       False if there are not any three pieces of one player side by side consecutively in a row
    def winInRow(self, row, piece):
#       find number of columns - 2 because that's the number of ways to win based on how many columns there are
        columnValue = self.cols() - 2
        for col in range(columnValue):            # for loop iterates every possible way of winning based on number of columns
#           checks a column and then the next 2 consecutive columns of that row for a piece
            if self.board[row][col] ==  self.board[row][col + 1] == self.board[row][col + 2] == piece:
                return True
        return False

#   Purpose: Checks if three pieces of one player are side by side consecutively in a column
#   Parameters:
#       col: the columns of the tic tac toe board
#       piece: the piece (X or O) being played
#   Returns:
#       True if there are three pieces of one player side by side in a column
#       False if there are not any three pieces of one player side by side consecutively in a column
    def winInCol(self, col, piece):
#       find number of rows - 2 because that's the number of ways to win based on how many rows there are
        rowValue = self.rows() - 2
        for row in range(rowValue):               # for loop iterates every possible way of winning based on number of rows
#           checks a row and then the next 2 consecutive rows of that column for a piece
            if self.board[row][col] ==  self.board[row + 1][col] == self.board[row + 2][col] == piece:
                return True
        return False

#   Purpose: Checks if three pieces of one player are in a row diagonally
#   Parameters:
#       piece: the piece (X or O) being played
#   Returns:
#       True if there are three pieces of one player are in a row diagonally
#       False if there are not any three pieces of one player are in a row diagonally
    def winInDiag(self, piece):
        columnValue = self.cols() - 2
        rowValue = self.rows() - 2
#       for loop checks each column in a row
        for row in range(rowValue):
            for col in range(columnValue):
#               Checks a row and column and then the next two rows and columns diagonally have a consecutive piece going forwards
                if self.board[row][col] ==  self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == piece:
                    return True
#               Checks a the inverse of the last if statment to check if three consecutive pieces of a player are in a row diagonally
#               coming backwards
                if self.board[row][col + 2] ==  self.board[row + 1][col + 1] == self.board[row + 2][col] == piece:
                    return True
        return False

#   Purpose: Checks if the player (or computer AI) has won
#   Parameters:
#       piece: the piece (X or O) being played
#   Returns:
#       True if the player or computer has won in either rows, coumns, or diagonally
#       False if the player or computer has not won in either rows, coumns, or diagonally
    def won(self, piece):
        for rowWin in range(self.rows()):               # Checks every row
            if self.winInRow(rowWin, piece) == True:    # Checks winner in rows
                return True
        for colWin in range(self.cols()):               # Checks every column
            if self.winInCol(colWin, piece) == True:    # Checks winner in columns
                return True
        if self.winInDiag(piece) == True:               # Checks winner diagonally
            return True
        else: return False

#   Purpose: Gives basic hint to user when the next move they can win or when they can stop the opponent from winning
#   Parameters:
#       piece: the piece (X or O) being played
#   Return:
#       rowHint, columnHint: a row and column where a hint tells the user that they should put their piece there
#       -1, 1: Indicates that there is no hint
    def hint(self, piece):
        for rowHint in range(self.rows()):                      # Checks every row
            for columnHint in range(self.cols()):               # Checks every column
#               Checks if a spot is empty and then plays a piece there. If, from that piece being played, the user wins, it removes that
#               piece and then puts a hint for the user to play in that spot. Otherwise the piece if just removed and no hint is returned
                if self.board[rowHint][columnHint] == EMPTY:
                    self.play(rowHint, columnHint, piece)
                    if self.won(piece) == True:
                        self.board[rowHint][columnHint] = EMPTY
                        return rowHint, columnHint
                    else:
                        self.board[rowHint][columnHint] = EMPTY
        return -1, -1
    
#   Purpose: Tells the user if the game is over form either player winning or from a draw (full method)
#   Parameters: None
#   Returns:
#       True if the game ends from one player winning or a full board (a draw)
#       False if there are still pieces to play and neither player has won
    def gameover(self):
        if self.won(X) or self.won(O) or self.full():
            return True
        return False