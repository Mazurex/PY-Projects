import random
import time

# Initialize the board
board = {
    "A1": "_", "A2": "_", "A3": "_",
    "B1": "_", "B2": "_", "B3": "_",
    "C1": "_", "C2": "_", "C3": "_",
}


# Print the board
def print_board(board):
    time.sleep(0.2)
    print("\n   1   2   3")
    time.sleep(0.2)
    print(f"A  {board['A1']}   {board['A2']}   {board['A3']}")
    time.sleep(0.2)
    print("   ")
    print(f"B  {board['B1']}   {board['B2']}   {board['B3']}")
    time.sleep(0.2)
    print("   ")
    print(f"C  {board['C1']}   {board['C2']}   {board['C3']}")
    time.sleep(0.2)
    print("\n")

# Check if the position is valid and not taken
def valid_move(position):
    return position in board and board[position] == "_"

# Check if the current player has won
def check_winner(board, player):
    winning_combinations = [
        ["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"], # Horizontal
        ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"], # Vertical
        ["A1", "B2", "C3"], ["A3", "B2", "C1"] # Diagonal
    ]
    
    for combination in winning_combinations:
        if all(board[pos] == player for pos in combination):
            return True
    return False

# Check if the board is full (draw)
def board_full(board):
    return all(value != "_" for value in board.values())

# Reset the board
def reset_board():
    for key in board:
        board[key] = "_"

# AI move logic with improvements to block and prioritize winning
def ai_move(player):
    time.sleep(0.2)
    print(f"AI ({player}) is thinking.")
    time.sleep(0.35)
    print(f"AI ({player}) is thinking..")
    time.sleep(0.35)
    print(f"AI ({player}) is thinking...")
    time.sleep(0.35)

    # Define all winning combinations
    winning_combinations = [
        ["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"], # Horizontal
        ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"], # Vertical
        ["A1", "B2", "C3"], ["A3", "B2", "C1"] # Diagonal
    ]

    opponent = "X" if player == "O" else "O"

    # Step 1: Check for winning move for AI
    for position in board:
        if valid_move(position):
            # Simulate AI move to check for a win
            board[position] = player
            if check_winner(board, player):
                return  # AI wins with this move
            else:
                board[position] = "_"

    # Step 2: Block opponent's winning move
    for position in board:
        if valid_move(position):
            # Simulate opponent move to check if AI needs to block
            board[position] = opponent
            if check_winner(board, opponent):
                board[position] = player  # Block the opponent's winning move
                return
            else:
                board[position] = "_"

    # Step 3: Strategic move if no immediate win/block is needed
    preferred_moves = ["B2", "A1", "A3", "C1", "C3", "B1", "B3", "C2"]
    for move in preferred_moves:
        if valid_move(move):
            board[move] = player
            return

# PvP mode
def pvp_game():
    print("Player vs Player mode!")
    current_player = "X"
    while True:
        print_board(board)
        position = input(f"Player {current_player}, enter your move (e.g. B2): ").upper()
        
        if valid_move(position):
            board[position] = current_player
            time.sleep(0.5) # Pause before switching to next player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                return current_player # Return the winner
            if board_full(board):
                print("It's a draw!")
                return None
            current_player = "O" if current_player == "X" else "X" # Switch player
        else:
            print("Invalid move. Try again")

# PvE mode
def pve_game():
    print("Player vs AI mode!")
    current_player = "X"
    while True:
        print_board(board)
        if current_player == "X":
            position = input("Player X, enter your move (e.g. B2): ").upper()
            if valid_move(position):
                board[position] = "X"
                time.sleep(0.5) # Small pause after players move
                if check_winner(board, "X"):
                    print_board(board)
                    print("Player Wins!")
                    return "X"
                if board_full(board):
                    print_board(board)
                    print("Its a draw!")
                    return None
                current_player = "O" # AI turn
            else:
                print("Invalid move. Try again.")
        else:
            ai_move("O")
            if check_winner(board, "O"):
                print_board(board)
                print("AI Wins!")
                return "O"
            if board_full(board):
                print("It's a draw!")
                return None
            current_player = "X"

# EvE mode (AI vs AI)
def eve_game():
    print("AI vs AI mode!")
    current_player = "X"
    while True:
        print_board(board)
        ai_move(current_player)
        if check_winner(board, current_player):
            print_board(board)
            print(f"AI ({current_player}) wins!")
            return current_player
        if board_full(board):
            print("It's a draw!")
            return None
        current_player = "O" if current_player == "X" else "X" # Switch player

# Main game loop
def main():
    # PVP
    player_x_score = 0
    player_o_score = 0
    
    # PVE
    player_score = 0
    ai_score = 0
    
    while True:
        print("\nWelcome to Tic-Tac-Toe!")
        print("1. Player vs Player (PvP)")
        print("2. Player vs AI (PvE)")
        print("3. AI vs AI (EvE)")
        print("4. Exit")
        
        choice = input("Choose your mode (1/2/3/4/5): ")
        
        if choice == "1":
            reset_board()
            winner = pvp_game()
            if winner == "X":
                player_x_score += 1
                print(f"Player X score: {player_x_score} | Player O score: {player_o_score}")
            elif winner == "O":
                player_o_score += 1
                print(f"Player X score: {player_x_score} | Player O score: {player_o_score}")
            elif winner is None:
                print("It's a draw.")
                print(f"Current PvP scores - Player X: {player_x_score}, Player O: {player_o_score}")
        elif choice == "2":
            reset_board()
            winner = pve_game()
            if winner == "X":
                player_score += 1
            elif winner == "O":
                ai_score += 1
            print(f"Current PvE scores - Player: {player_score} | AI: {ai_score}")
        elif choice == "3":
            reset_board()
            winner = eve_game()
            if winner == "X":
                print("AI X wins the AI vs AI match!")
            elif winner == "O":
                print("AI O wins the AI vs AI match!")
            else:
                print("It's a draw!")
        elif choice == "4":
            # Display final scores and exit
            print(f"\nFinal PvP Scores - Player X: {player_x_score} | Player O: {player_o_score}")
            print(f"Final PvE Scores - Player: {player_score} | AI: {ai_score}")
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")
            continue
        
        # Ask if player wants to play again, unless in CEvE mode
        if choice not in ["4", "5"]:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print(f"\nFinal PvP Scores - Player X: {player_x_score} | Player O: {player_o_score}")
                print(f"Final PvE Scores - Player: {player_score} | AI: {ai_score}")
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    main()
