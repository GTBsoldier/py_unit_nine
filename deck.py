# deck.py
import random

class Deck:
    def __init__(self):
        """
        Initialize a deck of cards and shuffle it upon creation.

        The deck is represented as a list of tuples, where each tuple
        contains a card's rank and suit.
        """
        self.cards = [(rank, suit) for rank in range(2, 15) for suit in ['♣️', '♦️', '♥️', '♠️']]
        self.shuffle()

    def shuffle(self):
        """
        Shuffle the deck using the Fisher-Yates algorithm.
        This method shuffles the order of cards in the deck randomly.
        I still don't completely understand this, it is from ChatGPT.
        """
        for i in range(len(self.cards) - 1, 0, -1):
            j = random.randint(0, i)
            # Swap the positions of two cards in the deck
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def deal(self, num_cards):
        """
        Deal a specified number of cards from the deck.
        Parameters:
        - num_cards (int): The number of cards to be dealt.
        Returns:
        A list of tuples representing the dealt cards.
        """
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards


from deck import Deck

def get_num_cards():
    """
    Get the number of cards to deal from the player.
    The function prompts the player to enter a number between 1 and 26
    and keeps prompting until a valid input is provided.
    Returns:
    An integer representing the number of cards to deal.
    """
    while True:
        try:
            num_cards = int(input("How many cards should each player get? Enter a number between 1 and 26: "))
            if 1 <= num_cards <= 26:
                return num_cards
            else:
                print("Please enter a number between 1 and 26.")
        except ValueError:
            print("Invalid input. Please enter a NUMBER between 1 and 26.")

def play_round(player_card, computer_card):
    """
    Play a round of the game and determine the winner.
    Parameters:
    - player_card (tuple): The card played by the player.
    - computer_card (tuple): The card played by the computer.
    Returns:
    A string indicating the winner of the round ('Player' or 'Computer').
    """
    print("Round:")
    print(f"Player: {player_card}")
    print(f"Computer: {computer_card}")

    player_rank, player_suit = player_card
    computer_rank, computer_suit = computer_card

    if player_rank > computer_rank or (player_rank == computer_rank and player_suit > computer_suit):
        winner = "Player"
    else:
        winner = "Computer"

    print(f"{winner} wins this round!")

    return winner

def main():
    """
    Run the main game loop.
    Displays the welcome message, game rules, gets the number of cards
    from the player, initializes the deck, plays each round, and displays
    the final results of the game.
    """
    print("Welcome to the game of Compare. You will decide how many cards we get, and then we'll play them one by one.")
    print("Whoever has the higher card wins that round. Whoever wins the most rounds wins the game.")

    num_cards = get_num_cards()

    deck = Deck()

    player_wins = 0
    computer_wins = 0

    for round_num in range(1, num_cards + 1):
        print(f"Round {round_num}:")

        player_hand = deck.deal(1)
        computer_hand = deck.deal(1)

        print(f"Player: {player_hand[0]}")
        print(f"Computer: {computer_hand[0]}")

        round_winner = play_round(player_hand[0], computer_hand[0])

        if round_winner == "Player":
            player_wins += 1
        else:
            computer_wins += 1

    print("Game Over!")
    print(f"Player wins: {player_wins} rounds")
    print(f"Computer wins: {computer_wins} rounds")

if __name__ == "__main__":
    # Call the main function
    main()
