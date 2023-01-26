#You are responsible for writing a program that allows a user to play casino Black Jack. The
#user will put a set amount of money onto the table and make a minimum $20 bet each hand.
#Each hand, the user will be dealt two cards and be given the option to hit or stay. If the user hits
#21 or goes over the round will end. The dealer will continue to hit until their hand has a
#minimum value of 17 as per casino guidelines. The user will be able to play as long as their
#total money is greater than or equal to the minimum bet of the table.

#Import required libraries
import random
import time

##Classes

#Card Class
class Card():
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.suit = suit
    #Method to print card attributes
    def display_card(self):
        print(f"{self.rank} of {self.suit}")


#Deck Class
class Deck():
    def __init__(self):
        self.cards = []
    #Method to generate all playing cards
    def build_deck(self):
        suits_list = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks_dic = {   "A":11,
                    "2":2,
                    "3":3,
                    "4":4,
                    "5":5,
                    "6":6,
                    "7":7,
                    "8":8,
                    "9":9,
                    "10":10,
                    "J":10,
                    "Q":10,
                    "K":10}
        for suit in suits_list:
            for rank, value in ranks_dic.items():
                card = Card(rank, value, suit)
                self.cards.append(card)
    #Method to shuffle the deck
    def shuffle_deck(self):
        random.shuffle(self.cards)
    #Method to draw a card
    def deal_card(self):
        dealt_card = self.cards.pop()
        return dealt_card

#Game class to hold game values
class Game:
    def __init__(self, money):
        self.money = money
        self.bet = 20
        self.winner = ""
    #Method to display money in play
    def display_money(self):
        print(f"\nCurrent Money: ${self.money}")
    #Method to display money in play and current bet
    def display_money_bet(self):
        print(f"\nCurrent Money: ${self.money}\tCurrent Bet: ${self.bet}")
    #Method to set bet
    def set_bet(self):
        betting = True
        while betting:
            user_bet = int(input("What would you like to bet (minimum bet of 20): "))
            if user_bet < 20:
                print("Please bet a minimum of $20")
            elif user_bet > self.money:
                print("You do not have that much money to bet!")
            else:
                self.bet = user_bet
                betting = False
    #Method to score the game
    def scoring(self, p_hand_value, d_hand_value):
        if p_hand_value == 21:
            print("You've got blackjack!")
            self.winner = "p"
        elif d_hand_value == 21:
            print("The dealer got blackjack...")
            self.winner = "d"
        elif p_hand_value > 21:
            print("You've went over 21...")
            self.winner = "d"
        elif d_hand_value > 21:
            print("The dealer went over 21!")
            self.winner = "p"
        else:
            if p_hand_value > d_hand_value:
                print(f"Dealer gets {d_hand_value}. You win!")
                self.winner = "p"
            elif d_hand_value > p_hand_value:
                print(f"Dealer gets {d_hand_value}. You lose!")
                self.winner = "d"
            else:
                print(f"Deader gets {d_hand_value}. It's a tie...")
                self.winner = "tie"
    #Method to record game payouts
    def payout(self):
        if self.winner == "p":
            game.money += game.bet
        elif self.winner == "d":
            game.money -= game.bet

#Class for the dealer
class Dealer():
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True
    #Method to draw initial hand
    def draw_hand(self, deck):
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)
    def hit(self, deck):
        self.get_hand_value()
    #Method to calculate sum of player's hand
    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == "A":
                ace_in_hand = True
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10
    #Method for dealer to hit
    def hit(self, deck):
        self.get_hand_value()
        while self.hand_value < 17:
            new_card = deck.deal_card()
            self.hand.append(new_card)
            self.get_hand_value()
        print(f"\nDealer is set with a total of {len(self.hand)} cards.")
    #Method for dealer to show hand in suspenseful manner
    def display_hand(self):
            input("\nPress enter to reveal the dealer's hand.")
            for card in self.hand:
                card.display_card()
                time.sleep(1)




#Class for the player
class Player():
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True
    #Method to draw initial hand
    def draw_hand(self, deck):
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)
    #Method to display hand
    def display_hand(self):
        print("\nPlayer's Hand:")
        for card in self.hand:
            card.display_card()
    #Method to calculate sum of player's hand
    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == "A":
                ace_in_hand = True
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10
        print(f"Total value: {self.hand_value}")
    #Method for player to hit or pass
    def update_hand(self, deck):
        if self.hand_value < 21:
            response = input("Would you like to hit (y/n): ").lower().strip()
            if response == "y":
                self.hit(deck)
            else:
                self.playing_hand = False
        elif self.hand_value >= 21:
            self.playing_hand = False
    #Method to let player hit
    def hit(self, deck):
        hit_card = deck.deal_card()
        self.hand.append(hit_card)

#Welcome message
print("Welcome to the Blackjack App.")
print("The minimum bet at this table is $20")

#Collect input on starting cash
starting_money = int(input("\nHow much money are you willing to play with today: "))
#Create game object
game = Game(starting_money)

#Game loop
while True:
    #Initialise required objects
    deck = Deck()

    #Build deck
    deck.build_deck()
    deck.shuffle_deck()

    #Initialise player and dealer
    dealer = Dealer()
    player = Player()

    #Draw initial 2 cards for round for both player and dealer
    dealer.draw_hand(deck)
    player.draw_hand(deck)

    #Ask for bet for this round
    game.display_money()
    game.set_bet()

    #Display current money and bet amount
    game.display_money_bet()
    
    #Show dealer's first card
    print(f"The dealer is showing a {dealer.hand[0].rank} of {dealer.hand[0].suit}.")

    #Player's move
    while player.playing_hand:
        player.display_hand()
        player.get_hand_value()
        player.update_hand(deck)
    
    #Have dealer hit until they reach 17 and then display hand
    dealer.hit(deck)
    dealer.display_hand()

    #Score the round
    game.scoring(player.hand_value, dealer.hand_value)
    
    #Record the round's payout
    game.payout()

    #End game if player has less than $20
    if game.money < 20:
        print("Sorry, you ran out of money. Please play again!")
        quit()

