from random import randint

scores = {'computer':0, 'player': 0}


class Board:
    """
    Main board class. Sets game board size, the player's name information, the number of
    ships, and the board type (computer or player). Includes methods for printing the board, 
    taking guesses and keeping the score
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        """
        joins columns and rows to print board to screen
        """
        for row in self.board:
            print("".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "*"

        if (x, y) in self.ships:
            return f"{self.name} has scored a direct hit!"
        else:
            return f"{self.name} has missed the mark!"

    
    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x,y))
            if self.type == "player":
                self.board[x][y] = "@"


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, board):
    pass


def populate_board(board):
    pass


def make_guess(board):
    pass


def play_game(computer_board, player_board):
    pass


def new_game():
    """
    Starts a new game. Sets the board size and number of ships,
     resets the scores and initialises the boards.
    """

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)


new_game()




