#!/usr/bin/env python
# blackjack

import random

# global variables for blackjack module
Suits = ('Club', 'Spade', 'Heart', 'Diamond')
Ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
Values = range(1, 11) + [10, 10, 10]
rank2Values = {r:v for (r,v) in zip(Ranks, Values)}
SuitsRep = sum(([s]*rep for s,rep in zip(Suits, (13, 13, 13, 13))), [])

# classes
class Card(object):
	## define an initialization method for this class
	def __init__(self, suit, rank):
		if(suit in Suits) and (rank in Ranks): 
			self.suit = suit
			self.rank = rank
		else:
			self.suit = None
			self.rank = None
			print "You must specify a proper suit and rank." 
	
	## define a string method for this class
	def __str__(self):
		return self.suit + self.rank
		
	def getSuit(self):
		return self.suit
		
	def getRank(self):
		return self.rank
		
	def getValue(self):
		return rank2Values[self.rank]

class Deck(object):
	def __init__(self):
		self.deck = [Card(s, r) for s,r in zip(SuitsRep, Ranks*4)]
		self.shuffle()
	
	def __str__(self):
		return ''.join([str(card) + ' ' for card in self.deck])
		
	def shuffle(self):
		random.shuffle(self.deck)
		
	def dealCard(self):
		if(self.deckSize <= 1): print 'Game Over: no cards left in deck' 
		# ToDo: add actual error handling here
		return self.deck.pop()
	
	def deckSize(self):
		return len(self.deck)
		
class Hand(object):
	def __init__(self, deck):
		self.deal = []
		self.deal.append(deck.dealCard())	
	def __str__(self):
		return ''.join([str(card) + ' ' for card in self.deal])

	def addCard(self, deck):
		self.deal.append(deck.dealCard())	
			
	def getValue(self):
		return sum([card.getValue() for card in self.deal])
	def isBusted(self):
		if (self.getValue() > 21): 
			return True
		else: 
			return False
	def isTwentyOne(self):
		if(self.getValue() == 21):
			return True
		else:
			return False

class Round(object):
	def __init__(self, deck):
		self.deck = deck
		self.dealer = Hand(self.deck)
		self.player = Hand(self.deck)
		
	def hit(self):
		self.player.addCard(self.deck)
		print 'Player`s hand: ' + str(self.player)
		if (self.player.isBusted()): 
			print "Busted!"
			return 0
		elif (self.player.isTwentyOne() ):
			print 'twenty-one!'
			return 1
		else: 
			self.dealer.addCard(self.deck)
			print 'Dealer`s hand: ' + str(self.dealer)
			if (self.dealer.isBusted()): 
				print 'dealer is busted'
				return 1
			elif (self.dealer.isTwentyOne() ):
				print 'dealer has twenty-one!'
				return 0 

	def stand(self):
		self.dealer.addCard(self.deck)
		print 'Dealer`s hand: ' + str(self.dealer)
		if (self.dealer.isBusted()): 
			print 'dealer is busted'
			return 1
		elif (self.dealer.isTwentyOne() ):
			print 'dealer has twenty-one!'
			return 0 
	
class Game(object):
	def __init__(self):
		self.deck = Deck()
		self.outcomes = []
		self.roundCntr = 0
	
	def __str__(self):
		print self.roundCntr

	def getScore(self):
		playerScore = self.outcomes.count(1)
		dealerScore = self.outcomes.count(0)
		print 'player:' 
		print playerScore
		print 'dealer:'
		print dealerScore
		return playerScore - dealerScore

	def nextHand(self):
		self.currentRound = Round(self.deck)
		print 'The player`s hand: ' + str(self.currentRound.player)
		print 'The dealer`s hand: ' + str(self.currentRound.dealer)
		print 'hit or stand?'

	def endHand(self):
		self.player = None
		self.dealer = None
		
	def endGame(self):
		print 'rounds:'
		print self.roundCntr
		score = self.getScore(self)
		if(score > 0): print 'You win!'
		if(score < 0): print 'Game Over: you lose'
		if(score == 0): print 'Game Over: it`s a tie'
		self.endHand()
		self.deck = None
				
	def hit(self):
		outcome = self.currentRound.hit()
		self.outcomes.append(outcome)
		if(outcome != None): self.endHand()
		self.roundCntr = self.roundCntr + 1
		if(self.deck.deckSize <= 0): self.endGame()

	def stand(self):
		outcome = self.currentRound.stand()
		self.outcomes.append(outcome)
		if(outcome != None): self.endHand()
		self.roundCntr = self.roundCntr + 1
		if(self.deck.deckSize <= 0): self.endGame()

