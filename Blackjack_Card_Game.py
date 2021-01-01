# Blackjack Card Game
# By: Crystal Lin
#======================================================================
from random import shuffle

# Defined Dictionaries/Tuples for a deck of cards
suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 
         'ten', 'jack', 'queen', 'king', 'ace')
values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
            'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':11}


# New Class for a single card and its attributes/characteristics
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank.lower()]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other): 
        if not isinstance(other, Card):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.suit == other.suit and self.rank == other.rank

# New class for a deck of cards, contains "Card" instances
class Deck:
    
    # define empy list then make a deck from all combos of suit and rank
    def __init__(self):
        self.all_cards = []
        
        for num in range(7):
            for suit in suits:
                for rank in ranks:
                    self.all_cards.append(Card(suit,rank))
                
    # method to shuffle deck
    def shuffle(self):
        shuffle(self.all_cards)
    
    # method to deal one card from the deck
    def deal_card(self):
        return self.all_cards.pop()

# New class for player             
class Player:
    
    def __init__(self,name,money):
        self.name = name
        self.money = money
    
    def lose_money(self,loss):
        self.money -= loss
    
    def win_money(self,win):
        self.money += win 
        
    def __str__(self):
        return f'{self.name} has ${self.money}'

# function for data validation for bet input
def bet():
    valid = False
    
    # keeps asking for input until its valid
    while valid == False:
        print(f'{P1.name}, you have ${P1.money}')
        bet = input('How much do you want to bet?: ')
        
        if bet.isdigit() == False:
            print('Please Enter a integer')
            continue
        elif int(bet) > P1.money:
            print('Not enough money, choose a smaller bet...\n')
        else:
            print(f'You are betting ${bet}\n')
            break
        
    return int(bet)

# validation for hit and stay input, returns the str 'hit' or 'stay'
def hit_stay_validation():
    while True:
        
            # ensure that input is not a digit
            choice = input('Do you want to "hit" or "stay": ')
            if choice.isdigit() == True:
                print('Please type "hit" or "stay", not a number')
                continue
            
            # can take in any capitlization of the two words
            choice = choice.lower()
            
            # makes sure that the word is hit or stay
            if choice not in ['hit','stay']:
                print('Please type "hit" or "stay"')
                continue
            else:
                print(f'You choose to "{choice.upper()}"') 
                break
            
    return choice

def play_again_validation():
    
    while True:
            # ensure that input is not a digit
            choice = input('Do you want to keep playing? Type "y" or "n": ')
            if choice.isdigit() == True:
                print('Please type "Y" or "N", not a number')
                continue
            
            # can take in any capitlization of the two words
            choice = choice.lower()
            
            # makes sure that the word is hit or stay
            if choice not in ['y','n']:
                print('Please type "Y" or "N", not a number')
                continue
            else:
                if choice == 'y':
                    choice = True
                    break
                if choice == 'n':
                    choice = False
                    break
            
    return choice
    
# function to calculate total val of any hand
def total_val(hand): # input should be a list of the cards4
    hand_value = 0
    for i in range(len(hand)):
        hand_value += hand[i].value
    
    # makes a list of all the aces possible
    all_aces = []
    for i in range(4):
        all_aces.append(Card(suits[i],'ace'))
    
    # counts the number of aces in the hand
    hand_aces = 0
    for card in hand:
        if card in all_aces:
            hand_aces += 1
    
    # keeps subtracting 10 (change ace from 11 to 1) if it can prevent busting
    if hand_aces != 0:
        for i in range(hand_aces + 1):
            if hand_value > 21:
                hand_value -= 10
            else:
                break
         
    return hand_value

# function to print the dealer and player hand
def print_hand(dealer_hand, player_hand):
    print(f'\nYour Hand: {player_hand}, total value is {total_val(player_hand)}')
    print(f'Dealer: {dealer_hand}, total value is {total_val(dealer_hand)}')
    
# function to do the inital set up
def deal_setup(deck,dealer_hand,player_hand): # returns the two hand or
    if len(dealer_hand) != 0 or len(player_hand) != 0:
        return 'INPUT LIST NEED TO BE EMPTY'

    # deals two cards each to player and dealer
    player_hand.append(deck.deal_card())
    dealer_hand.append(deck.deal_card())
    player_hand.append(deck.deal_card())
    dealer_hand.append(deck.deal_card())  
        
    out = 0
    if total_val(dealer_hand) == total_val(player_hand) == 21:
        print('Both have 21...all bets returned')
        return 'TIE'
    elif total_val(dealer_hand) == 21:
        print_hand(dealer_hand,player_hand)
        out = False
    elif total_val(player_hand) == 21:
        print_hand(dealer_hand,player_hand)
        out = True   
    else:
        out = [player_hand,dealer_hand]
        
    return out

def dealer_play(deck,dealer_hand,player_hand): # returns True = Win or False = Lost
    # the dealer keeps getting cards until greater than player or busts
    while True: # must self break out
        dealer_hand.append(deck.deal_card())
        if total_val(dealer_hand) > 21:
            print('\nDealer BUSTED, you WIN.....................')
            return True
            break
        elif total_val(dealer_hand) > total_val(player_hand):
            print('\nDealer WON, you LOSE......................')
            return False
            break
# =================================================================
# GAME BEGINING
# =================================================================
game_on = True

big_deck = Deck()
big_deck.shuffle()

P1 = Player(input('Please Enter Your Name: '), 5000)
P1_hand = []
dealer_hand = []



# deal
while game_on:
    
    # game set up (deal cards and display with values)
    P1_hand = []
    P1_tot_value = 0
    
    dealer_hand = []
    dealer_tot_value = 0
    
    # deal to player and deal
    bet_amt = bet()
    after_deal = deal_setup(big_deck,dealer_hand,P1_hand)
    
    if after_deal == True: # True means player auto wins with 21
        P1.money += bet_amt
        print(f'\nYou got 21! You WIN {bet_amt}')
    elif after_deal == False: # False means dealer auto wins with 21
        P1.money -= bet_amt
        print(f'Dealer Wins with 21. You LOSE {bet_amt}')
    elif after_deal == 'TIE': # Both dealer and player got 21
        pass # no change in money, only play again
    else:
        print('Dealer is DEALING')
        print_hand(dealer_hand, P1_hand)
        
        # this part is analogous to one round btw player and dealer
        # loop to keep asking player to hit or stay
    
        win = False
    
        while True: # make sure to self break
            choice = hit_stay_validation()
            
            if choice == 'hit':
                P1_hand.append(big_deck.deal_card())
                    
                if total_val(P1_hand) == 21:
                    print(f'\nYou got 21! You WIN {bet_amt}')
                    print(f'{P1_hand}, total value is {total_val(P1_hand)}')
                    P1.win_money(bet_amt)
                    break       
                elif total_val(P1_hand) > 21:
                    print(f'\nSorry, you busted, you lose {bet_amt}')
                    print(f'{P1_hand}, total value is {total_val(P1_hand)}')
                    P1.lose_money(bet_amt)
                    break
            else:
                win = dealer_play(big_deck,dealer_hand,P1_hand)
                if win == True:
                    P1.win_money(bet_amt)
                    print_hand(dealer_hand, P1_hand)
                else:
                    P1.lose_money(bet_amt)
                    print_hand(dealer_hand, P1_hand)
                break
            
            print_hand(dealer_hand, P1_hand)       
    print(f'\n   !!! Your new total cash: {P1.money} !!!')  
    if P1.money == 0:
        print('You lost all your money...game over...come again soon')
        break
    
    game_on = play_again_validation()

print('\nHope you had fun, please come play again!')
 
    
    
# make deckkitty
# shuffle deck
# start game
# deal to player
# deal to dealer
# deal to player
# deal to dealer
# ask to hit or stop

# two while loop (one for keep playing, one for keep hitting)
# if hit, deal one card
    # if bust, lose money, ask to play again (yes = keep loop, no = break)
    # if no bust, as hit to stay
    # once stay then deal until greater than player or bust (two outcomes bust or win)
# win = add money
# ask play again
