import random
import pickle
import os

# Define the emojis for display
EMOJI_CLOSED = '🟦'
EMOJI_FLAG = '🚩'
EMOJI_BOMB = '💣'
EMOJI_EMPTY = '⬜'

EMOJI_NUMBERS = ['⬛', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣']

# A helper to convert number to alphabetic coordinates
def index_to_alpha(idx):
    alphabet = ''
    while idx >= 0:
        alphabet = chr(idx % 26 + ord('A')) + alphabet
        idx = idx // 26 - 1
    return alphabet

def alpha_to_index(alpha):
    idx = 0
    for char in alpha:
        idx = idx * 26 + (ord(char) - ord('A') + 1)
    return idx - 1

# Class for the Minesweeper game
class Minesweeper:
    def __init__(self, size=5, bomb_count=5):
        self.size = size
        self.bomb_count = bomb_count
        self.board = []
        self.visible = []
        self.flags = set()
        self.bombs = set()
        self.generate_board()

    def generate_board(self):
        """Initializes the game board with bombs and numbers."""
        # Create an empty board
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.visible = [[False for _ in range(self.size)] for _ in range(self.size)]
        
        # Place bombs randomly
        bomb_positions = random.sample(range(self.size * self.size), self.bomb_count)
        for pos in bomb_positions:
            row, col = divmod(pos, self.size)
            self.board[row][col] = -1  # Mark bomb position
            self.bombs.add((row, col))
            # Increment numbers around the bomb
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] != -1:
                        self.board[r][c] += 1

    def display_board(self):
        """Display the current state of the board with proper alignment."""
        # Define the width for each cell, adjust if necessary to accommodate emojis
        cell_width = 4

        # Display the header row with column numbers
        header = ' ' * 3 + ''.join(f'{i+1:<{cell_width}}' for i in range(self.size))  # Properly formatted column headers
        print(header)

        # Display each row
        for i in range(self.size):
            row_label = index_to_alpha(i)  # Convert index to alphabetic label
            row = [self.get_display_char(i, j) for j in range(self.size)]
            # Ensure each cell is center-aligned in its width
            formatted_row = ''.join(f'{cell:^{cell_width}}' for cell in row)  # Center-align each cell
            print(f'{row_label:<3} {formatted_row}')
    
    def get_display_char(self, row, col):
        """Return the emoji for a specific plot based on its state."""
        if (row, col) in self.flags:
            return EMOJI_FLAG
        elif not self.visible[row][col]:
            return EMOJI_CLOSED
        elif self.board[row][col] == -1:
            return EMOJI_BOMB
        elif self.board[row][col] == 0:
            return EMOJI_EMPTY
        else:
            return EMOJI_NUMBERS[self.board[row][col]]

    def open_plot(self, coord):
        """Opens the plot based on coordinates like 'A1'."""
        row, col = self.parse_coordinates(coord)
        if (row, col) in self.flags:
            print("Cannot open a flagged plot!")
            return
        
        if self.board[row][col] == -1:
            self.reveal_bombs()
            print("Game Over! You hit a bomb!")
            return False
        elif self.board[row][col] == 0:
            self.clear_empty_plots(row, col)
        else:
            self.visible[row][col] = True
        return True

    def clear_empty_plots(self, row, col):
        """Recursively clears empty plots and their surroundings."""
        if not (0 <= row < self.size and 0 <= col < self.size):
            return
        if self.visible[row][col]:
            return
        if self.board[row][col] != 0:
            self.visible[row][col] = True
            return
        self.visible[row][col] = True
        
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < self.size and 0 <= c < self.size:
                    self.clear_empty_plots(r, c)

    def flag_plot(self, coord):
        """Flags a plot to mark a suspected bomb."""
        row, col = self.parse_coordinates(coord)
        if not self.visible[row][col]:
            self.flags.add((row, col))
    
    def parse_coordinates(self, coord):
        """Parses coordinates like 'A1' into row and column indices."""
        row_str = ''.join([char for char in coord if char.isalpha()])
        col_str = ''.join([char for char in coord if char.isdigit()])
        row = alpha_to_index(row_str.upper())
        col = int(col_str) - 1
        return row, col

    def reveal_bombs(self):
        """Reveals all bomb locations when the game is over."""
        for bomb in self.bombs:
            self.visible[bomb[0]][bomb[1]] = True

    def is_win(self):
        """Check if the player has won the game."""
        opened_plots = sum(1 for row in self.visible for col in row if col)
        return opened_plots == self.size * self.size - self.bomb_count

    def reset(self, size, bomb_count):
        """Reset the game with new settings."""
        self.size = size
        self.bomb_count = bomb_count
        self.bombs.clear()
        self.flags.clear()
        self.generate_board()

    def save_game(self, filename="minesweeper_save.pkl"):
        """Save the current game state to a file."""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print(f"Game saved to {filename}.")

    @staticmethod
    def load_game(filename="minesweeper_save.pkl"):
        """Load a saved game state from a file."""
        if not os.path.exists(filename):
            print(f"No save file found with the name {filename}.")
            return None
        with open(filename, 'rb') as f:
            game = pickle.load(f)
        print(f"Game loaded from {filename}.")
        return game

# Game loop
def play_minesweeper():
    print("Welcome to Minesweeper!")
    load_option = input("Do you want to load a saved game? (yes/no): ").strip().lower()
    
    if load_option == "yes":
        game = Minesweeper.load_game()
        if not game:
            print("Starting a new game instead.")
            size = int(input("Enter board size (e.g., 5 for 5x5): "))
            bombs = int(input("Enter number of bombs: "))
            game = Minesweeper(size=size, bomb_count=bombs)
    else:
        size = int(input("Enter board size (e.g., 5 for 5x5): "))
        bombs = int(input("Enter number of bombs: "))
        game = Minesweeper(size=size, bomb_count=bombs)

    game.display_board()
    
    while True:
        command = input("Enter your move (e.g., A1 open, B2 flag, 00 for core commands): ").strip()
        if command == "00":
            core_command = input("Enter core command (start, reset, end, save, load, help): ").strip()
            if core_command == "end":
                print("Thanks for playing!")
                break
            elif core_command == "reset":
                size = int(input("Enter new board size: "))
                bombs = int(input("Enter new number of bombs: "))
                game.reset(size, bombs)
                game.display_board()
            elif core_command == "help":
                print("Help: Commands you can use:\n")
                print("A1 open   --> Opens the plot at A1")
                print("B2 flag   --> Flags the plot at B2")
                print("00 reset  --> Resets the game")
                print("00 end    --> Ends the game")
                print("00 save   --> Saves the game")
                print("00 load   --> Loads the game")
            elif core_command == "save":
                game.save_game()
            elif core_command == "load":
                loaded_game = Minesweeper.load_game()
                if loaded_game:
                    game = loaded_game
                game.display_board()
            elif core_command == "start":
                play_minesweeper()
        else:
            try:
                coord, action = command.split()
                if action == "open":
                    if not game.open_plot(coord):
                        game.display_board()
                        break
                elif action == "flag":
                    game.flag_plot(coord)
                game.display_board()
            except ValueError:
                print("Invalid command format. Try again.")

# Start the game
play_minesweeper()
