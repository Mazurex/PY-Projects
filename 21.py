import random

# Initialize game state for 7 players
scores = [0] * 7  # Stores each player's total score
stay = [False] * 7  # Tracks if each player has chosen to stay

# Function to deal a card to the player
def deal_card():
    card = random.randint(1, 14)  # Random card between 1-14
    if 1 <= card <= 10:
        return card  # Cards 1-10 have their face value
    elif 11 <= card <= 13:
        return 10  # Face cards (Jack, Queen, King) count as 10
    else:
        return int(input("You got an ACE! Choose 1 or 11: "))  # ACE choice by player

# Function to determine the winner once all players stay
def determine_winner():
    highest_score = 0
    winner = None
    for i, score in enumerate(scores):
        if score == 21:
            print(f"Player {i} wins with a perfect 21!")
            return  # Immediate win for player with exactly 21
        elif score > highest_score and score <= 21:
            highest_score = score
            winner = i

    if winner is not None:
        print(f"Player {winner} wins with the highest score of {highest_score}!")
    else:
        print("No winners this round, everyone busted!")

# Main game function
def blackjack():
    player = 0  # Start with Player 0
    while not all(stay):  # Continue until all players have chosen to stay
        if not stay[player]:  # If the current player hasn't stayed yet
            action = input(f"Player {player}: take or stay? ").lower()
            if action == "take":
                scores[player] += deal_card()  # Add the card value to their score
                print(f"Player {player}'s score is now {scores[player]}")
                if scores[player] >= 21:  # If the player's score reaches or exceeds 21, they must stay
                    stay[player] = True
            else:
                stay[player] = True  # Mark player as having stayed

        player = (player + 1) % 7  # Move to the next player, loop back to 0 after player 6

    determine_winner()  # Once all players have stayed, determine the winner

# Start the game
blackjack()