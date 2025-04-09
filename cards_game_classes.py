suits = ('Hearts', 'Diamonds', 'Spades', 'clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three' :3, 'Four':4, 'Five': 5, 'Six': 6, 'Seven':7, 
					'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

import random

playing = True

# later also try to apply some unit testing here
class Card():
	'''This Class represents any Card and you use it to init a card for the Deck of cards'''
	def __init__(self, suit, rank):
		self.suit = suit # TBD replace later with classmethod (quick self init)
		self.rank = rank

	def __str__(self):
		return f"{self.rank} of {self.suit}"
		# return self.rank + "of" + self.suit

class Deck():
	def __init__(self):
		self.deck = [] # start with an empty list
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))

	def __str__(self) :
		deck_comp = "" # deck composition
		for card in self.deck:
			deck_comp += f'\n{card.__str__()}'
			# deck_comp += '\n' + card.__str__()
		return f'The deck has:\n {deck_comp}'

	def shuffle(self):
		random.shuffle(self.deck) # to shuffle any array

	def deal(self):
		return self.deck.pop() #removing a card from the deck and returning it upon request

class Hand():
	def __init__(self):
		self.cards = [] # start with an empty list as we did in the card class
		self.value = 0 # start with a zero value
		self.aces = 0 # add an attribute to keep track of aces

	def add_card(self, card):
		# card passed in
		# from Deck.deal() --> Single Card(suit, rank)
		self.cards.append(card)
		self.value += values[card.rank]

		# track aces
		if card.rank == 'Ace':
			self.aces += 1


	# def clear_cards(self):  # no need since you can always call __init__()


	# IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE 
	# THAN CHANGE MY ACETO BE A 1 INSTEAD OF AN 11
	def adjust_for_aces(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

		# while self.value > 21:
		# 	if self.aces > 0:
		# 		self.value -= 10
		# 		self.aces -= 1
		# 	else:
		# 		break




	def __str__(self) :
		hand_comp = "" # deck composition
		for card in self.cards:
			hand_comp += f'\n{card.__str__()}'
			# hand_comp += '\n' + card.__str__()
		return f'The hand has:\n {hand_comp}'


## testing so far
# >>> test_deck = Deck()
# >>> test_deck.shuffle()
# >>> test_player = Hand()
# >>> test_player.add_card(test_deck.deal())
# >>> print(test_player)
# The hand has:
 
# Queen of clubs
# >>> print(test_player.value)
# 16


# in addition to decks of cards and hands, we need to keep track of a Player's starting chips, bets, and ongoing winnings.
# This could be done using global variables, but in the spirit of object programming, let's make a Chips class instead!

class Chips():
	def __init__(self, total = 100):
		self.total = total # this can be set to a default value or supplied by a user input
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How many chips would you like to bet? "))
		except:
			print("Sorry please provide an integer")
		else:
			if chips.bet > chips.total:
				print(f"Sorry, you don't have enough chips! you have: {chips.total}")
			else:
				break

#Actually we're here only combining 2 python line that we did before as part of the test and are always goes one after the oter
def hit(deck, hand):
	hand.add_card(deck.deal())
	hand.adjust_for_aces()

def hit_or_stand(deck, hand):
	global playing

	while True:
		x = input("Hit or Stand? Enter 'h' or 's' ")

		if x[0].lower() == 'h':
			hit(deck, hand)
		elif x[0].lower() == 's':
			print("Player Stands Dealer Turn")
		else:
			print("Sorry, I did not understand that, please enter 'h' or 's' only!")
			continue
		break


def show_some(player, dealer):
	print('DEALERS HAND:')
	print('one card hidden!')
	print(dealer.cards[1])
	print('\n')
	print('PLAYERS HAND:')
	for card in player.cards:
		print(card)

def show_all(player, dealer):
	print('DEALERS HAND:')
	for card in dealer.cards:
		print(card)
	print(dealer.cards[1])
	print('\n')
	print('PLAYERS HAND:')
	for card in player.cards:
		print(card)


# functions to handle end of game scenarios
def player_busts(player, dealer, chips):
	print("BUST PLAYER!")
	chips.lose_bet()

def player_wins(player, dealer, chips):
	print("PLAYER WINS!")
	chips.win_bet()

def dealer_busts(player, dealer, chips):
	print("PLAYER WINS! DEALER BUSTED!")
	chips.win_bet()

def dealer_wins(player, dealer, chips):
	print("DEALER WINS!")
	chips.lose_bet()

def push(player, dealer, chips):
	print("Dealer and player tie! PUSH")



# and now the game itself
while playing:
# while True:
	print("WELCOME TO BLACKJACK")
	# create and shuffle the deck, deal 2 cards to each player
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())



	# set up the player's chips
	player_chips = Chips()

	# prompt the player for their bet
	take_bet(player_chips)

	#show cards (but keep one dealer card hidden)
	show_some(player_hand, dealer_hand)

	while playing: # recall this variable from our hit_or_stand function
		# prompt for Player to Hit or Stand
		hit_or_stand(deck, player_hand)

		# show cards (but keep one dealer card hidden)
		show_some(player_hand, dealer_hand)

		# if player's hand exceeds 21, run player_bust() and break out of loop
		if player_hand.value > 21:
			player_busts(player_hand, dealer_hand, player_chips)

			break


		# if player hasn't busted, play Dealer's hand until Dealer reaches 17
		if player_hand.value <= 21:
			while dealer_hand.value <= player_hand.value:
			# while dealer_hand.value <= 17: # dealer hits until he reach 17
				hit(deck, dealer_hand)


			# show all cards
			show_all(player_hand, dealer_hand)

			# Run differet winning scenarios
			if dealer_hand.value>21:
				dealer_busts(player_hand, dealer_hand, player_chips)
			elif dealer_hand.value>player_hand.value:
				dealer_wins(player_hand, dealer_hand, player_chips)
			elif dealer_hand.value<player_hand.value: # will come-up only if we use the 'until we reach 17' option
				player_wins(player_hand, dealer_hand, player_chips)
			else:
				push(player_hand, dealer_hand)


		# inform Player of their chips total
		print(f'\nPlayer total chips are at {player_chips.total}')

		# ask to play again
		new_game = input("Would you like to play another hand? [Yes/No] ")

		if new_game[0].lower()=='y':
			playing = True
			continue
		else:
			playing = False
			print('Thank you for playing!')
			break





