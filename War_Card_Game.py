# Card Game "War"
# By: Crystal Lin
#======================================================================
import random

# Defined Dictionaries/Tuples for a deck of cards
suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
            'nine':9, 'ten':10, 'jack':11, 'queen':12, 'king':13, 'ace':14}

# New Class for a single card and its attributes/characteristics
class Card:

    def __init__(self,suit,rank):
        self.suit = suit.lower()
        self.rank = rank
        self.value = values[rank.lower()]

    # Method for str output
    def __str__(self):
        return self.rank + ' of ' + self.suit

# New Class for a deck of cards (52 instances of Card)
class Deck:

    def __init__(self):
        # Starts deck with empty list
        self.all_cards = []

        # use double for loop to create all possible combo for suit and rank
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def draw_one(self):
        return self.all_cards.pop()
    
class Player:
    
    def __init__ (self,name):
        self.name = name
        self.hand = []

    def remove_card(self):
        return self.hand.pop(0)
        
    def add_cards(self,new_cards):
        
        # add a list of cards
        if type(new_cards) == type([list]):
            self.hand.extend(new_cards)
            
        # adds a single card
        else:
            self.hand.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards'
    
    
#======================================================================
# Game Logic
#====================================================================== 

# Sets up the game with two players and a full deck
player1 = Player('P1')
player2 = Player('P2')
deck = Deck()
deck.shuffle()

# Spliting the deck to each player
for card in range(26):
    player1.add_cards(deck.draw_one())
    player2.add_cards(deck.draw_one())

print(len(player1.hand))
print(len(player2.hand))

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f'Current Round: {round_num}')
    
    # Checks if either player has lost
    if len(player1.hand) == 0:
        print('Player 1 Out of Cards \nPlayer 2 Wins')
        break
    
    if len(player2.hand) == 0:
        print('Player 2 Out of Cards, Player 1 Wins!')
        break
    
    # New Round
    player1_in_play = []
    player2_in_play = []
    
    # Removes one card from each players current hand
    player1_in_play.append(player1.remove_card())
    player2_in_play.append(player2.remove_card())
    
    at_war = True
    
    while at_war:
        
        # checks if player 1 has higher value
        if player1_in_play[-1].value > player2_in_play[-1].value:
            player1.add_cards(player1_in_play)
            player1.add_cards(player2_in_play)
            at_war = False
            
         # checks if player 2  has higher value  
        elif player1_in_play[-1].value < player2_in_play[-1].value:
            player2.add_cards(player1_in_play)
            player2.add_cards(player2_in_play)
            at_war = False
        
        # enters WAR if neither has higher value
        else:
            print('WAR!')
            
            # Checks if both players have enough cards for war
            if len(player1.hand) < 5:
                print('Player 1 cannot declare war')
                print('\nPlayer 2 WINS!')
                game_on = False
                break
            
            elif len(player2.hand) < 5:
                print('Player 1 cannot declare war')
                print('\nPlayer 2 WINS!')
                game_on = False
                break
            
            # add cards onto the table
            else:
                for num in range(5):
                    player1_in_play.append(player1.remove_card())
                    player2_in_play.append(player2.remove_card())
                
                    
            

        
        
    
    
    
    
    
    
    
    
    

